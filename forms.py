from django import forms
from .models import Enlace

class AcortadorForm(forms.ModelForm):

    class Meta:
        model = Enlace
        fields = ['Url']
        widget = {
            'url': forms.URLInput(attrs={'class':'input is-rounded is-medium', 'placeholder':'URL'})
        }