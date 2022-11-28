from ckeditor.widgets import CKEditorWidget
from django import forms

from order.models import Order
from order.models import OrderDetail


class Orderform(forms.ModelForm):
    date = forms.DateTimeField(
        label="fecha",
        max_length=30,
        required=False,
        widget=forms.DateInput(
            attrs={
                "placeholder": "fecha",
                "required": "True",
            }
        )
    )

    class Meta:
        model= Order
        fields=["date"]

    
    

class OrderDetail(forms.ModelForm):
    quantity = forms.IntegerField(
        label = "cantidad",
        required= False,
        widget= forms.NumberInput(
            attrs={
                "placeholder": "cantidad",
                "required": "True",
            }
        )
    )
    class Meta:
        model=OrderDetail
   
