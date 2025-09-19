from django import forms
from cars.models import Car

class CarForm(forms.ModelForm):
    class MEta:
        model = Car
        fields = ['type', 'owner', 'price']
