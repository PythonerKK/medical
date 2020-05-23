import json

from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.views.generic import DetailView, RedirectView, UpdateView
from rest_framework import mixins, viewsets, authentication, permissions
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.settings import api_settings

from config.auth import OpenId
from medical.users.serializers import UserDetailSerializer
from medical.utils.helpers import IsOwnerOrReadOnly

User = get_user_model()


class UserDetailView(LoginRequiredMixin, DetailView):

    model = User
    slug_field = "username"
    slug_url_kwarg = "username"


user_detail_view = UserDetailView.as_view()


class UserUpdateView(LoginRequiredMixin, UpdateView):

    model = User
    fields = ["name"]

    def get_success_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})

    def get_object(self):
        return User.objects.get(username=self.request.user.username)

    def form_valid(self, form):
        messages.add_message(
            self.request, messages.INFO, _("Infos successfully updated")
        )
        return super().form_valid(form)


user_update_view = UserUpdateView.as_view()


class UserRedirectView(LoginRequiredMixin, RedirectView):

    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})


user_redirect_view = UserRedirectView.as_view()


@require_http_methods(['POST'])
@csrf_exempt
def GetOpenIdView(request):
    data = json.loads(request.body)
    jscode = data['jscode']

    openid, session_key = OpenId(jscode).get_openid()
    return JsonResponse({
        'openid': openid,
        'session_key': session_key
    })


@require_http_methods(['POST'])
@csrf_exempt
def login_or_create_account(request):
    data = json.loads(request.body)
    print(data)
    openid = data['openid']
    #session_key = data['session_key']
    nickname = data['nickname']
    avatar_url = data['avatar_url']
    gender = data['gender']
    address = data['address']

    try:
        user = User.objects.get(username=openid)
    except User.DoesNotExist:
        user = None

    if not user:
        user = User.objects.create(
            username=openid,
            password=openid,
            nickname=nickname,
            avatar_url=avatar_url,
            gender=gender,
            address=address
        )

    jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
    jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
    payload = jwt_payload_handler(user)
    token = jwt_encode_handler(payload)
    res = {
        'status': 'success',
        'nickname': user.nickname,
        'user_id': user.id,
        'token': token
    }
    return JsonResponse(res)


class UserViewset(mixins.UpdateModelMixin, mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    '''
    update:
        更新用户资料
    Retrieve:
        检索用户
    '''
    serializer_class = UserDetailSerializer
    authentication_classes = (authentication.SessionAuthentication, JSONWebTokenAuthentication, )
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get_object(self):
        return self.request.user
