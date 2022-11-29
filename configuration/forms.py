from ckeditor.widgets import CKEditorWidget
from django import forms

from configuration.models import CategoryProduct, OrderState


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
        widget=forms.BooleanField(),
    )

    class Meta:
        model = OrderState
        fields = ['name', 'description', 'state'] 
