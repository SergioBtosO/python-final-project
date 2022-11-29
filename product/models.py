from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

from configuration.models import CategoryProduct

# Create your models here.
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    description = RichTextField(max_length= 100)
    price = models.DecimalField(decimal_places=2,max_digits=11)
    size = models.CharField(max_length=100)
    weigth = models.DecimalField(decimal_places=2,max_digits=11)
    category_id = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    color = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products', null=True, blank=True)

    class Meta:
        ordering = ['id']


    def __str__(self):
        return f"product: {self.name}"


class Question(models.Model):
    id = models.AutoField(primary_key=True)
    user_from = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = RichTextField(max_length= 100)
    date_coment = models.DateField(auto_now_add=True)
    question = models.OneToOneField('questions.id', on_delete=models.CASCADE, related_name='inventory')
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    

    class Meta:
        ordering = ['id']


    def __str__(self):
        return f"question: {self.name}"
