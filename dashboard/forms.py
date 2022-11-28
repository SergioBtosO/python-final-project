from ckeditor.widgets import CKEditorWidget
from django import forms

from dashboard.models import UserInfo
from dashboard.models import UserQualification


class UserInfoform(forms.ModelForm):
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
    address = forms.IntegerField(
        label = "Direccion",
        required= False,
        widget= forms.CharField(
            attrs={
                "placeholder": "Direccion",
                "required": "True",
            }
        )
    )

    photo = forms.ImageField
        

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

    document_type = forms.CharField(
        label = "tipo de documento",
        required= False,
        widget= forms.CharField(
            attrs={
                "placeholder": "tipo de documento",
                "required": "True",
            }
        )
    )
    
    class Meta:
        model = UserInfo
        fields = ["phone", "address", "document", "document-type", "photo"]

class UserQualificationForm(forms.ModelForm):
    phone = forms.IntegerField(
        label = "Calificacion",
        required= False,
        widget= forms.NumberInput(
            attrs={
                "placeholder": "Calificacion",
                "required": "True",
            }
        )
    )
    class Meta:
        model = UserQualification
        fields = ["UserQualification"]