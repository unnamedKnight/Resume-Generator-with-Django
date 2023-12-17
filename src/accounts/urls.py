from django.urls import path
from . import views

urlpatterns = [
    path(
        "user-registration",
        views.user_registration,
        name="user_registration"),
    path("login", views.user_login, name="user_login"),
    path("logout", views.user_logout, name="user_logout"),
]
