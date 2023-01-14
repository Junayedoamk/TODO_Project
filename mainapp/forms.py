from mainapp.models import User,TODO
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['email', 'password1', 'password2']

class TodoForm(ModelForm):
    class Meta:
        model = TODO
        fields = ['todo', 'status']