from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from medical.users.api.views import UserViewSet

router = DefaultRouter()

router.register("users", UserViewSet)


app_name = "api"
urlpatterns = router.urls
