from django.forms import ModelForm, RadioSelect, Textarea, TextInput

from .models import Chatbot, Settings, ContextData


class CreateChatbotForm(ModelForm):
    class Meta:
        model= Chatbot
        fields = ('name','status','description')
        widgets = {
            'status': RadioSelect(choices=[(True, 'Active'), (False, 'Inactive')]),
            'description': Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'name': TextInput(attrs={'class': 'form-control'}),
        }
class EditChatbotForm(CreateChatbotForm):
    class Meta:
        model = Chatbot
        fields = ('name', 'status', 'description', 'image')
        widgets = {
            'status': RadioSelect(choices=[(True, 'Active'), (False, 'Inactive')]),
            'description': Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'name': TextInput(attrs={'class': 'form-control'}),
        }
class EditChatbotSettingsForm(ModelForm):
    class Meta:
        model=Settings
        fields = ('default_greeting','interaction_language','bot_personality',
                  'context_length','output_length','limit_summary','rate_limit')


class EditContextDataForm(ModelForm):
    class Meta:
        model= ContextData
        fields = ('context_description','context_example')
        widgets = {
            'context_description': Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'context_example': Textarea(attrs={
                'title': "Context",
                'class': 'form-control',
                'rows': 5
            }),
        }