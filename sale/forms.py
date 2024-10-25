from django import forms

from .models import Sale

class SaleForm(forms.ModelForm):
    
    
    
    quantity = forms.IntegerField(
        label="Quantité",
      
    )

    
    
    class Meta:
        model = Sale
        fields = ["stock", "quantity", "discount","client","is_paid"]