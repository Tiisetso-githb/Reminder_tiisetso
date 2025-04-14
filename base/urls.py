from django.urls import path, include
from .views import authView, home, create_reminder

urlpatterns = [
 path("", home, name="home"),
 path('create_reminder/', create_reminder, name='create_reminder'),
 path("signup/", authView, name="authView"),
 path("accounts/", include("django.contrib.auth.urls")),
]
