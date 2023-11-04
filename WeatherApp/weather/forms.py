from .models import City
from django.forms import ModelForm, TextInput

class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['name']
        widgets = {'name' : TextInput(attrs={
            'class':'form-control',
            'placeholder': 'Введите город',
            'name': 'city',
            'id': 'city',
            'type': 'text'
        })}
