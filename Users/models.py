
from django.db import models
from django.contrib.auth.models import AbstractUser




class Profile(AbstractUser):
    subscription = models.ForeignKey('Subscriptions.Subscription', on_delete=models.SET_NULL,blank=True,null=True,related_name='subs_user')
    chatbots = models.ManyToManyField('Chatbots.Chatbot',blank=True)
    profile_image = models.URLField( blank=True, null=True)


    def __str__(self):
        return f"{self.username}'s Profile"