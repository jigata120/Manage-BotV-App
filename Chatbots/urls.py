from django.urls import path

from . import views

urlpatterns = [
    path('chatbots/settings/data/<int:pk>', views.ChatbotContextDataView.as_view(), name='chatbots_settings_data_page'),
    path('chatbots/', views.ChatbotManageView.as_view(), name='chatbots_manage_page'),
    path('chatbot-settings/<uuid:pk>', views.ChatbotSettingsView.as_view(), name='chatbots_settings_page'),
    path('chatbot-usage/<uuid:pk>', views.ChatbotUsageView.as_view(), name='chatbot_usage_page'),
    path('chatbot-edit/<uuid:pk>', views.ChatbotEditView.as_view(), name='chatbot_edit_page'),
    path('chatbot-delete/<uuid:pk>', views.chatbot_delete, name='chatbot_delete'),
    path('chatbot-integration/<uuid:pk>', views.ChatbotIntegrationView.as_view(), name='chatbot_integration'),

    path('', views.IndexView.as_view(), name='index'),
    path('monitor-api/<int:pk>', views.update_monitoring_data, name='monitor-api'),
    path('playground/', views.playground, name='playground_page'),
    path('documentation/', views.DocumentationView.as_view(), name='documentation_page'),

]
