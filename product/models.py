from django.db import models
from ckeditor.fields import RichTextField
from configuration.models import CategoryProduct
from django.contrib.auth.models import User


# Create your models here.
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    description = RichTextField(max_length= 100)
    price = models.DecimalField(decimal_places=2,max_digits=11)
    size = models.CharField(max_length=100)
    weigth = models.DecimalField(decimal_places=2,max_digits=11)
    category = models.ForeignKey(CategoryProduct, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey (User, on_delete=models.CASCADE)
    color = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products', null=True, blank=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f"product: {self.name}"