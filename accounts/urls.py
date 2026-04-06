from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .views import UserProfileView, RegisterView, profile_edit

urlpatterns = [
    path('profile/', UserProfileView.as_view(), name='profile'),
    # path('profile/edit/', UserProfileUpdateView.as_view(), name='profile_edit'),
    path('profile/edit/', profile_edit, name='profile_edit'),
    path('', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
