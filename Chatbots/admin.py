
from django.contrib import admin
from .models import Chatbot, Usage, ContextData, Settings, ChatbotSession
admin.site.site_header = "Chatbot Administration"
admin.site.site_title = "Chatbot Administration"
admin.site.index_title = "Welcome to the Chatbot Administration"
@admin.register(Chatbot)
class ChatbotAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'description', 'user', 'created_at', 'updated_at','usage__interactions')
    list_filter = ('status', 'created_at', 'updated_at',)
    search_fields = ('name', 'user__username')
    readonly_fields = ('apikey', 'created_at', 'updated_at')
    ordering = ('usage__interactions',)
    date_hierarchy = 'updated_at'
    list_editable = ('status',)


@admin.register(Usage)
class UsageAdmin(admin.ModelAdmin):
    list_display = ('chatbot', 'interactions', 'daily_interactions', 'monthly_interactions',
                    'tokens_usage', 'daily_tokens_usage', 'monthly_tokens_usage', 'updated_at')
    list_filter = ('updated_at',)
    search_fields = ('chatbot__name',)
    readonly_fields = ('updated_at',)

@admin.register(ContextData)
class ContextDataAdmin(admin.ModelAdmin):
    list_display = ('context_description', 'updated_at')
    search_fields = ('context_description',)
    readonly_fields = ('updated_at',)

@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ('chatbot','context_data__id', 'context_length', 'output_length', 'limit_summary',
                    'conversation_timeout', 'interaction_language', 'bot_personality', 'rate_limit')
    list_filter = ('interaction_language', 'bot_personality')
    search_fields = ('chatbot__name',)

@admin.register(ChatbotSession)
class ChatbotSessionAdmin(admin.ModelAdmin):
    list_display = ('id', 'session_data', 'all_messages')
    search_fields = ('id',)
    readonly_fields = ('id',)
