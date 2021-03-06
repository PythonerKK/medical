from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from django.views import defaults as default_views
from django.views.generic import TemplateView
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.documentation import include_docs_urls
from rest_framework_jwt.views import obtain_jwt_token

from medical import xadmin
from medical.users.views import GetOpenIdView, login_or_create_account

urlpatterns = [
    path("", TemplateView.as_view(template_name="pages/home.html"), name="home"),
    path(
        "about/", TemplateView.as_view(template_name="pages/about.html"), name="about"
    ),
    path('xadmin/', xadmin.site.urls),
    # User management
    path("users/", include("medical.users.urls", namespace="users")),
    path("queue/", include("medical.queueup.urls", namespace="queueup")),
    path("accounts/", include("allauth.urls")),
    path('ckeditor/', include('medical.utils.ckeditor_urls')),
    # Your stuff: custom urls includes go here
    path('docs/', include_docs_urls(title="小程序大赛后端接口文档")),
    path('api-token-auth/', obtain_jwt_token),


    # 微信小程序登录
    path('api/v1/get-openid/', GetOpenIdView),
    path('api/v1/wx-login/', login_or_create_account),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# API URLS
urlpatterns += [
    # API base url
    path("api/", include("config.api_router")),
    # DRF auth token
    path("auth-token/", obtain_auth_token),
]

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
