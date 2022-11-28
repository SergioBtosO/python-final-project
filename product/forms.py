from ckeditor.widgets import CKEditorWidget
from django import forms

from product.models import Product
from product.models import Question

class ProductForm(forms.Form):
    name = forms.CharField(
        label="Nombre",
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "product-name",
                "placeholder": "nombre del producto",
                "required": "True",
            }
        ),
    )
    category = forms.CharField(
        label="Categoria",
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "product-category",
                "placeholder": "categoria del producto",
                "required": "True",
            }
        ),
    )
    size = forms.CharField(
        label="Medidas",
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "product-size",
                "placeholder": "size",
                "required": "True",
            }
        ),
    )
    colors = forms.CharField(
        label="Colores",
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "product-colors",
                "placeholder": "colors",
                "required": "True",
            }
        ),
    )
    price = forms.DecimalField(
        label="Precio",
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "product-price",
                "placeholder": "price",
                "required": "True",
            }
        ),
    )
    weight = forms.DecimalField( 
        label="Peso",
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "product-weight",
                "placeholder": "weight",
                "required": "True",
            }
        ),
    )
    description = forms.CharField(
        label="Descripcion",
        required=True,
        widget=forms.Textarea(
            attrs={
                "class": "product-description",
                "placeholder": "description",
                "required": "True",
            }
        ),
    )

    photo = forms.ImageField

    class Meta:
        model = Product
        fields = ["name", "category", "size", "color", "description", "image"]

class QuestionForm(forms.Form):
    user_from = forms.CharField(
        label="usuario",
        required=True,
        widget=forms.TextInput(
            attrs={  
                "placeholder": "usuario",
                "required": "True",
            }
        ),
    )
   
    comment = forms.CharField(
        label="cometarios",
        required=True,
        widget=forms.Textarea(
            attrs={
                "placeholder": "cometarios",
                "required": "True",
            }
        ),
    )
    class Meta:
        model = Question