from django import forms
from .models import ItemPost
from datetime import date, timedelta


class ItemForm(forms.ModelForm):
    class Meta:
        model = ItemPost
        fields = ['title', 'description', 'location', 'date', 'image']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }

    def clean_date(self):
        d = self.cleaned_data.get('date')
        today = date.today()

        
        if not d or d > today or d < today - timedelta(days=30):
            raise forms.ValidationError("Invalid date")

        return d