from django import forms
from .models import Organisation


class OrganisationForm(forms.ModelForm):
    class Meta:
        model = Organisation
        fields = [
            'organisation_name',
            'city',
            'category',
            'certificate',
        ]

        widgets = {
            'organisation_name': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'certificate': forms.FileInput(attrs={'class': 'form-control-file'}),
        }