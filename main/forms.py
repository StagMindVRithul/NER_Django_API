from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from .models import Medical

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ["username","email","password1","password2"]

class MedicalForm(forms.ModelForm):
    entities = forms.CharField(widget=forms.HiddenInput(), required=False)
    class Meta:
        model = Medical
        fields = ["text","entities"]