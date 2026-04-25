from django import forms
from .models import ItemPost


class FoundItemForm(forms.ModelForm):
    class Meta:
        model = ItemPost
        fields = ['title', 'description', 'location', 'date', 'image']

        widgets = {
            'date': forms.DateInput(attrs={
                'type': 'date'
            })
        }

    def clean_date(self):
        date = self.cleaned_data.get('date')

        if not date:
            raise forms.ValidationError("Date is required")

        return date