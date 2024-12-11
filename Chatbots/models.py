import uuid
from django.db import models
from django.utils import timezone

from .choices import LanguageChoices, PersonalityChoices
from .model_utils import is_day_gone, is_month_gone, reset_usage_if_needed
from django.db.models import JSONField

class Chatbot(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    image = models.URLField( blank=True, null=True)
    apikey = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    status = models.BooleanField(default=True)
    description = models.TextField(max_length=1000)
    user = models.ForeignKey('Users.Profile', on_delete=models.CASCADE, related_name='rel_chatbots')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    settings = models.OneToOneField('Settings', on_delete=models.CASCADE, related_name='rel_chatbot_settings',
                                    null=True,blank=True)
    usage = models.OneToOneField('Usage', on_delete=models.CASCADE, related_name='rel_chatbot_usage',
                                    null = True, blank = True)

    def __str__(self):
        return self.name


class Usage(models.Model):
    interactions = models.IntegerField(default=0)
    daily_interactions = models.IntegerField(default=0)
    monthly_interactions = models.IntegerField(default=0)
    tokens_usage = models.IntegerField(default=0)
    daily_tokens_usage = models.IntegerField(default=0)
    monthly_tokens_usage = models.IntegerField(default=0)
    chatbot = models.OneToOneField(Chatbot, on_delete=models.CASCADE, related_name='rel_usage',blank=True,null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def update_usage(self, interactions=None, tokens=None):
        print('---------------------------------------------------------------')
        if interactions:
            self.interactions += interactions
            self.daily_interactions += interactions
            self.monthly_interactions += interactions
        elif tokens:
            self.tokens_usage += tokens
            self.daily_tokens_usage += tokens
            self.monthly_tokens_usage += tokens
            print('__________________________________________________________________________________________-'+str(tokens))
        if is_day_gone(self.updated_at) or is_month_gone(self.updated_at):
            reset_usage_if_needed()
        else:
            self.save()

    def __str__(self):
        if self.chatbot:
            return f"{self.chatbot.name} Usage"
        return  f"Usage{self.id} "

class ContextData(models.Model):
    context_description = models.TextField()
    context_example = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Context Data {self.id}"

class Settings(models.Model):
    chatbot = models.OneToOneField(Chatbot, on_delete=models.CASCADE, related_name='rel_settings',
                                   blank=True, null=True)
    context_length = models.PositiveIntegerField(default=500)
    context_data = models.OneToOneField(ContextData, on_delete=models.CASCADE, related_name='rel_context_data_settings',
                                        blank=True,null=True)
    output_length = models.PositiveIntegerField(default=50)
    limit_summary = models.PositiveIntegerField(default=1000)
    conversation_timeout = models.IntegerField(default=10, help_text="Conversation Timeout in minutes")
    interaction_language = models.CharField(
        max_length=2,
        choices=LanguageChoices.choices,
        default=LanguageChoices.ENGLISH,
        help_text="Language for bot interactions"
    )
    bot_personality = models.CharField(
        max_length=4,
        choices=PersonalityChoices.choices,
        default=PersonalityChoices.PROFESSIONAL,
        help_text="Personality style of the bot"
    )
    rate_limit = models.IntegerField(default=60, help_text="Maximum requests allowed per minute")
    default_greeting= models.CharField(max_length=200,default='Hello! How can I help you today?')

    def __str__(self):
        if self.chatbot:
            return f"{self.chatbot.name} Settings"
        return f"{self.id} Settings"


class ChatbotSession(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    session_data = JSONField()  # Store entire session data, including messages
    all_messages = JSONField(null=True, blank=True)  # Allow this field to be null

    class Meta:
        db_table = 'chatbot_session'  # Specify the table name

    def __repr__(self):
        return f"<ChatbotSession(id={self.id})>"

    def __str__(self):
        return f"ChatbotSession(id={self.id})"

class AllowedHost(models.Model):
    domain = models.CharField(max_length=255)

    def __str__(self):
        return self.domain