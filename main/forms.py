from django.forms.widgets import TextInput
from .models import City
from django.forms import ModelForm

class CityForm(ModelForm):

    class Meta:
        model = City
        fields = "__all__"

        widgets = {
            'name': TextInput(attrs={
                'class': 'field',
                'placeholder': 'Enter city'
            })
        }