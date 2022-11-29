from ckeditor.widgets import CKEditorWidget
from django import forms

from configuration.models import CategoryProduct, Score, OrderState 


class CategoryProductForm(forms.ModelForm):
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


class ScoreForm(forms.ModelForm):
    name = forms.CharField(
        label="Nombre",
        max_length=30,
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Nombre",
                "required": "True",
            }
        ),
    )

    value = forms.IntegerField(
        label="Valor:",
        required=False,
        widget=forms.NumberInput(
            attrs={
                "placeholder": "Valor",
                "placeholder": "Nombre producto",
                "required": "True",
            }
        ),
    ) 
    

    description = forms.CharField(
        label="Descripción:",
        required=False,
        widget=CKEditorWidget(
            attrs={
                "placeholder": "Descripción",
                "required": "True",
            }
        ),
    )

    class Meta:
        model = Score
        fields = ['name', 'value', 'description']
        widget=CKEditorWidget(),
    
 


class OrderStateform(forms.ModelForm):
    name = forms.CharField(
        label="Nombre",
        max_length=30,
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Nombre",
                "required": "True",
            }
        ),
    )

    description = forms.CharField(
        label="Descripción:",
        required=False,
        widget=CKEditorWidget(
            attrs={
                "placeholder": "Descripción",
                "required": "True",
            }
        ),
    )

    
    state = forms.BooleanField(
        label="Habilitado:",
        required=False,
        widget=forms.CheckboxInput(),
    )

    class Meta:
        model = OrderState
        fields = ['name', 'description', 'state'] 
