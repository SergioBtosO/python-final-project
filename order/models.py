from django.db import models
from django.contrib.auth.models import User
from product.models import Product
from configuration.models import OrderState

# Create your models here.


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    user_from = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f"orders: {self.name}"
    
class OrderDetail(models.Model):
    id = models.AutoField(primary_key=True)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    status =  models.ForeignKey(OrderState, on_delete=models.CASCADE)
    user_to = models.ForeignKey(User, on_delete=models.CASCADE)
    price_order = models.DecimalField(decimal_places=2, max_digits=11)
