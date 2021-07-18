from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import UserProfileListAPIView, userProfileDetailView

urlpatterns = [
    #gets all user profiles and create a new profile
    path("profiles/",UserProfileListAPIView.as_view(),name="profiles"),
   # retrieves profile details of the currently logged in user
    path("profiles/<str:user_id>/",userProfileDetailView.as_view(),name="profiles"),
]