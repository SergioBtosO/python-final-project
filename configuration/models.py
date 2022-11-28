from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class CategoryProduct(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    description = RichTextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['id']


    def __str__(self):
        return f"Category product: {self.name}"

class Score (models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10)
    description = RichTextField(max_length=50)
    value = models.IntegerField(max_length=10)

    def __str__(self):
        return f"Score: {self.value} - {self.name}"

class OrderState(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    description = RichTextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    state = models.BooleanField(default=False)

    class Meta:
        ordering = ['id']


    def __str__(self):
        return f"order state: {self.name}"
