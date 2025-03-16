from django import forms
from .models import Trainee

class LoginForm(forms.ModelForm):

    class Meta:
        model = Trainee
        fields = ['email', 'password']