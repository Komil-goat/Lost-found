from django import forms
from .models import ItemPost


class ItemForm(forms.ModelForm):
    class Meta:
        model = ItemPost
        fields = ['title', 'description', 'location', 'date', 'image', 'tags']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'tags': forms.CheckboxSelectMultiple()
        }