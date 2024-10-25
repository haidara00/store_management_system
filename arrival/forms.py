from django import forms 
from .models import Arrival

class ArrivalForm(forms.ModelForm):
    
    class Meta:
        model = Arrival
        fields = ("stock", "quantity")