from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from django.contrib.auth import get_user_model

class RegisterForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username','email')