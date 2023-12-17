from django.urls import path
from . import views

urlpatterns = [path("<id>", views.profile, name="profile"),
               path("edit-profile/<id>", views.edit_profile, name="edit_profile")]

