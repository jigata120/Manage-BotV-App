
from django.db import models
from django.contrib.auth.models import User, AbstractUser
from Chatbots.models import Chatbot
from Subscriptions.models import Subscription



class Profile(AbstractUser):
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE,blank=True,null=True,related_name='subs_user')
    chatbots = models.ManyToManyField(Chatbot,blank=True)
    profile_image = models.URLField( blank=True, null=True)


    def __str__(self):
        return f"{self.username}'s Profile"