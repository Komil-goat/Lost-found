from django import forms
from .models import ItemPost


class FoundItemForm(forms.ModelForm):
    class Meta:
        model = ItemPost
        fields = ['title', 'description', 'location', 'date', 'image']