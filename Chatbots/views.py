from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.decorators.http import require_http_methods
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, TemplateView
)
from .mixins import UserDataOnlyMixin, ChatbotsContextsMixin
from asgiref.sync import sync_to_async

from .forms import (
    CreateChatbotForm, EditChatbotForm, EditChatbotSettingsForm, EditContextDataForm
)
from .models import Chatbot, Usage, Settings, ContextData
from .model_utils import custom_timesince


class IndexView(ChatbotsContextsMixin, ListView):
    model = Chatbot

    def get_template_names(self):
        user = self.request.user
        if (user.is_authenticated and user.subscription is not None or
                user.groups.filter(name__in=['Administrators', 'Support']).exists() or
                user.is_superuser):
            return ['chatbots/dashboard-page.html']
        return ['landing-page.html']


@require_http_methods(["GET"])
async def update_monitoring_data(request, pk):
    try:
        usage = await sync_to_async(get_object_or_404)(Usage, pk=pk)

        time_difference = timezone.now() - usage.updated_at
        time_in_minutes = time_difference.total_seconds() / 60

        if time_in_minutes < 1:
            is_now = False
        else:
            is_now = await sync_to_async(custom_timesince)(usage.updated_at)

        data = {
            'id': usage.pk,
            'interactions': usage.interactions,
            'daily_interactions': usage.daily_interactions,
            'monthly_interactions': usage.monthly_interactions,
            'tokens_usage': usage.tokens_usage,
            'daily_tokens_usage': usage.daily_tokens_usage,
            'monthly_tokens_usage': usage.monthly_tokens_usage,
            'updated_at': usage.updated_at.isoformat(),
            'time_since_update': is_now
        }

        return JsonResponse(data)

    except Exception as e:
        return JsonResponse({
            'error': 'Failed to retrieve monitoring data contact admin',
            'details': str(e)
        }, status=200)


class ChatbotSettingsView(LoginRequiredMixin, UserDataOnlyMixin, UpdateView):
    template_name = 'chatbots/chatbot-settings-page.html'
    model = Settings
    form_class = EditChatbotSettingsForm
    success_url = reverse_lazy('chatbots_manage_page')

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        self.bot = Chatbot.objects.filter(pk=pk).first()
        settings = self.bot.settings
        return settings

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bot'] = self.bot
        return context


class ChatbotContextDataView(LoginRequiredMixin, UserDataOnlyMixin, UpdateView):
    model = ContextData
    template_name = 'chatbots/chatbot-data-settings-page.html'
    form_class = EditContextDataForm

    def form_valid(self, form):
        self.object = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        url = reverse_lazy('chatbots_settings_page', kwargs={
            'pk': self.object.rel_context_data_settings.rel_chatbot_settings.pk
        })
        return url


class ChatbotManageView(LoginRequiredMixin, ChatbotsContextsMixin, CreateView):
    template_name = 'chatbots/chatbot-manage-page.html'
    model = Chatbot
    form_class = CreateChatbotForm
    success_url = reverse_lazy('chatbots_manage_page')

    def form_valid(self, form):
        user = self.request.user
        settings = Settings.objects.create()
        usage = Usage.objects.create()
        context_data = ContextData.objects.create()

        settings.context_data = context_data
        settings.save()
        chatbot = form.save(commit=False)
        chatbot.user = user
        chatbot.settings = settings
        chatbot.usage = usage
        chatbot.save()
        user.chatbots.add(chatbot)
        user.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))


class ChatbotEditView(LoginRequiredMixin, UserDataOnlyMixin, UpdateView):
    template_name = 'chatbots/chatbot-edit-page.html'
    model = Chatbot
    form_class = EditChatbotForm
    success_url = reverse_lazy('chatbots_manage_page')


@login_required
def chatbot_delete(request, pk):
    chatbot = get_object_or_404(Chatbot, pk=pk, user=request.user)
    chatbot.delete()
    success_url = reverse_lazy('chatbots_manage_page')
    return HttpResponseRedirect(success_url)


class ChatbotUsageView(LoginRequiredMixin, UserDataOnlyMixin, DetailView):
    model = Chatbot
    template_name = 'chatbots/chatbot-usage-page.html'


class ChatbotIntegrationView(LoginRequiredMixin, UserDataOnlyMixin, ChatbotsContextsMixin, DetailView):
    template_name = 'chatbots/chatbot-integration-page.html'
    model = Chatbot


def get_initial_data(request, apikey):
    bot = Chatbot.objects.filter(apikey=apikey).first()
    return JsonResponse({"name": bot.name, "image": bot.image}, status=200)


def playground(request):
    return render(request, 'index.html')


def chatbot_view(request):
    return render(request, 'chatbots/chatbot/chatbot-page.html')


class DocumentationView(TemplateView):
    template_name = 'chatbots/docs-page.html'
