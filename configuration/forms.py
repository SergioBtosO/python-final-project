from ckeditor.widgets import CKEditorWidget
from django import forms

from configuration.models import CategoryProduct
from configuration.models import UserInfo
from configuration.models import OrderState
from configuration.models import Orders
from configuration.models import Product
from configuration.models import Question


class CategoryProductform(forms.ModelForm):
    name = forms.CharField(
        label="Nombre categoria",
        max_length=30,
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Nombre categoria",
                "required": "True",
            }
        ),
    )

    description = forms.CharField(
        label="Descripción:",
        required=False,
        widget=CKEditorWidget(),
    )

    class Meta:
        model = CategoryProduct
        fields = ['name', 'description']     

class UserInfoform(forms.ModelForm):
    user_name = forms.CharField(
        label = "Nombre de usuario",
        max_length = 30,
        required = False,
        widget = forms.TextInput(
            attrs ={
                "placeholder": "Nombre de usuario",
                "required": "True",
            } 
        ),
    )

    email = forms.CharField(
        label = "Email",
        max_length = 30,
        required = False,
        widget = forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "required": "True",
            } 
        )
    )

    phone = forms.IntegerField(
        label = "numero de celular",
        required= False,
        widget= forms.NumberInput(
            attrs={
                "placeholder": "numero de celular",
                "required": "True",
            }
        )
    )

    document = forms.IntegerField(
        label = "numero de documento",
        required= False,
        widget= forms.NumberInput(
            attrs={
                "placeholder": "numero de documento",
                "required": "True",
            }
        )
    )



class OrderStateform(forms.ModelForm):
    name = forms.CharField(
        label="Nombre producto",
        max_length=30,
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Nombre producto",
                "required": "True",
            }
        ),
    )

    description = forms.CharField(
        label="Descripción:",
        required=False,
        widget=CKEditorWidget(),
    )

    state = forms.CharField(
        label="Descripción:",
        required=False,
        widget=CKEditorWidget(),
    )

    class Meta:
        model = OrderState
        fields = ['name', 'description', 'state']  


class Ordersform(forms.ModelForm):
    user_from = forms.CharField(
        label = "Nombre de usuario",
        max_length = 30,
        required = False,
        widget = forms.TextInput(
            attrs ={
                "placeholder": "Nombre de usuario",
                "required": "True",
            } 
        ),
    )

    date = forms.DateTimeField(
        label = "fecha",
        max_length = 30,
        required = False,
        widget = forms.DateInput(
            attrs={
                "placeholder": "fecha",
                "required": "True",
            } 
        )
    )

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

    status = forms.CharField(
        label = "estado",
        required= False,
        widget= forms.TextInput(
            attrs={
                "placeholder": "estado",
                "required": "True",
            }
        )
    )


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