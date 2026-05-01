from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('phone_number',)

    def clean(self):
        cleaned_data = super().clean()
        username = self.cleaned_data.get("username")
        phone_number = self.cleaned_data.get("phone_number")

        user_exists = CustomUser.objects.filter(username=username).exists()
        phone_exists = CustomUser.objects.filter(phone_number=phone_number).exists()

        if user_exists or phone_exists:
            raise ValidationError("Invalid credentials")

        return cleaned_data

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone_number', 'avatar']