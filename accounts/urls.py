from django.urls import path, include
from .api import RegisterAPI, LoginAPI, UserAPI
from knox import views as knox_views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('api/auth', include('knox.urls')),
    path('api/auth/register', csrf_exempt(RegisterAPI.as_view())),
    path('api/auth/login', csrf_exempt(LoginAPI.as_view())),
    path('api/auth/user', csrf_exempt(UserAPI.as_view())),
    path('api/auth/logout', knox_views.LogoutView.as_view(), name='knox_logout')
]
