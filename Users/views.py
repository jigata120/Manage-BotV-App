from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from requests import request

from datetime import datetime, timedelta
from .forms import RegisterForm
from .models import Profile
from Chatbots.models import Chatbot,Settings,ContextData,Usage
from Subscriptions.models import Plan,Subscription
 

class ProfileView(DetailView):
     template_name = 'users/profile-page.html'
     model = get_user_model()
     context_object_name = 'user'

class LoginViewNew(LoginView):
     template_name = 'users/login-page.html'
     success_url = reverse_lazy('index')


class RegisterView(CreateView):

     form_class = RegisterForm
     template_name = 'users/register-page.html'
     success_url = reverse_lazy('login')

     def form_valid(self, form):

          self.object = form.save()
          settings = Settings.objects.create()
          usage = Usage.objects.create()
          context_data = ContextData.objects.create()
          settings.context_data =context_data
          settings.save()

          chatbot = Chatbot.objects.create(
               name=f'{self.object.username}\'s Free Chatbot',
               description='Free Trial Chatbot.',
               settings=settings,
               user=self.object,
               usage=usage,

          )

          self.object.chatbots.add(chatbot)

          self.object.save()
          return super().form_valid(form)

