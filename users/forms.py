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
        
        username = cleaned_data.get("username")
        phone_number = cleaned_data.get("phone_number")
        user_error = 'username' in self._errors
        phone_error = 'phone_number' in self._errors
        phone_exists = CustomUser.objects.filter(phone_number=phone_number).exists()

        if user_error or phone_error or phone_exists:
            if 'username' in self._errors:
                del self._errors['username']
            if 'phone_number' in self._errors:
                del self._errors['phone_number']
            
            raise ValidationError("Invalid credentials")

        return cleaned_data

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone_number', 'avatar']