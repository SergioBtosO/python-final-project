from django.db import models
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



class UserInfo(models.Model):
    id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    address = models.CharField(max_length=30)
    phone = models.CharField(max_length=20)
    document = models.IntegerField()
    document_type = models.CharField(max_length=30)
    password = models.CharField(max_length=50)
    role_id = models.CharField(max_length=30)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f'user: {self.user_name} | {self.id}'



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


class Orders(models.Model):
    id = models.AutoField(primary_key=True)
    user_from = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now_add=True)
    order_id = models.AutoField(primary_key=True)
    product_id = models.AutoField(primary_key=True)
    quantity = models.IntegerField()
    status = models.CharField(default= False)
    user_to = models.ForeignKey
    price_order = UserInfo

    class Meta:
        ordering = ['id']


    def __str__(self):
        return f"orders: {self.name}"


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

