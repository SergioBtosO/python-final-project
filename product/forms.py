from ckeditor.widgets import CKEditorWidget
from django import forms

from product.models import Product
from product.models import Question


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "category", "size", "weigth",
                  "color", "price", "description", "image"]


class QuestionForm(forms.Form):
    question_text = forms.CharField(
        label="",
        required=False,
        max_length=500,
        min_length=10,
        strip=True,
        widget=forms.Textarea(
            attrs={
                "class": "question-text",
                "placeholder": "Ingrese su pregunta...",
                "required": "True",
                "max_length": 500,
                "min_length": 10,
                "rows": 2,
                "cols": 10,
                "style": "min-width: 100%",
            }
        ),
    )
