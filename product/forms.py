from ckeditor.widgets import CKEditorWidget
from django import forms

from product.models import Product

class ProductForm(forms.ModelForm):
      class Meta:
        model = Product
        fields = ["name", "category", "size", "weigth", "color","price", "description", "image"]
