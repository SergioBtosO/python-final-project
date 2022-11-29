from ckeditor.widgets import CKEditorWidget
from django import forms

from product.models import Product
from product.models import Question

class ProductForm(forms.ModelForm):
      class Meta:
        model = Product
        fields = ["name", "category", "size", "weigth", "color","price", "description", "image"]

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