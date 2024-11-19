from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views
from .views import RegisterView, LoginViewNew

urlpatterns = [
    path('profile/<int:pk>', views.ProfileView.as_view(), name='profile'),
    path('sign-in/', LoginViewNew.as_view(), name='login'),
    path('sign-up/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
