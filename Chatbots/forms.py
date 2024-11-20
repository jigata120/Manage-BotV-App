from django.forms import ModelForm, RadioSelect, Textarea, TextInput

from .models import Chatbot


class CreateChatbotForm(ModelForm):
    class Meta:
        model= Chatbot
        fields = ('name','status','description')
        widgets = {
            'status': RadioSelect(choices=[(True, 'Active'), (False, 'Inactive')]),
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