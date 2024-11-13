from django.urls import path
from . import views



urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('sign-in/', views.login, name='login'),
    path('sign-up/', views.register, name='register'),

]
