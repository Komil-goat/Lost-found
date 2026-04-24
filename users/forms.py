from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        # Add any extra fields you put in your model here
        fields = UserCreationForm.Meta.fields + ("phone_number",)