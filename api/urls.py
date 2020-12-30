from django.contrib import admin
from django.urls import path, re_path, include
from dj_rest_auth.registration.views import VerifyEmailView
from django.views.generic import TemplateView
from dj_rest_auth.views import PasswordResetConfirmView

# Swagger
from rest_framework import permissions, authentication
from drf_yasg2.views import get_schema_view
from drf_yasg2 import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Tournament API docs.",
        default_version='v1',
    ),
    public=False,
    permission_classes=(permissions.IsAuthenticated, permissions.IsAdminUser),
    authentication_classes=(
        authentication.TokenAuthentication, authentication.SessionAuthentication)
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),


    path('auth/registration/account-confirm-email/', VerifyEmailView.as_view(), name='account_email_verification_sent'),
    re_path(r'^auth/password/reset/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),

    re_path(r'^swagger(?P<format>.json|.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
