from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('phone_number',)

    def clean(self):
        # 1. Run parent validation (this catches the duplicate username)
        cleaned_data = super().clean()
        
        username = cleaned_data.get("username")
        phone_number = cleaned_data.get("phone_number")

        # 2. Check if Django's internal check caught a username error 
        # OR if your manual phone check finds a duplicate
        user_error = 'username' in self._errors
        phone_exists = CustomUser.objects.filter(phone_number=phone_number).exists()

        if user_error or phone_exists:
            # 3. CRITICAL: Clear the individual field errors
            # This prevents the "invisible" field errors from blocking your UI
            if 'username' in self._errors:
                del self._errors['username']
            if 'phone_number' in self._errors:
                del self._errors['phone_number']
            
            # 4. Now this will show up in your auth-error-container
            raise ValidationError("Invalid credentials")

        return cleaned_data

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone_number', 'avatar']