from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    description = RichTextField(max_length= 100)
    price = models.DecimalField(decimal_places=2,max_digits=11)
    size = models.CharField(max_length=100)
    weigth = models.DecimalField(decimal_places=2,max_digits=11)
    category_id = models.CharField(default= False)
    user_id = models.ForeignKey (primary_key=True)
    color = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products', null=True, blank=True)

    class Meta:
        ordering = ['id']


    def __str__(self):
        return f"product: {self.name}"


class Question(models.Model):
    id = models.AutoField(primary_key=True)
    user_from = models.CharField(max_length=30)
    comment = RichTextField(max_length= 100)
    date_coment = models.DateField(auto_now_add=True)
    question_id = models.ForeignKey(primary_key=True)
    product_id = models.ForeignKey(primary_key=True)
    

    class Meta:
        ordering = ['id']


    def __str__(self):
        return f"question: {self.name}"
