from django.contrib import admin

# Register your models here.
from configuration.models import CategoryProduct
from configuration.models import UserInfo
from configuration.models import OrderState
from configuration.models import Orders
from configuration.models import Product
from configuration.models import Question

admin.site.register(CategoryProduct)
admin.site.register(UserInfo)
admin.site.register(OrderState)
admin.site.register(Orders)
admin.site.register(Product)
admin.site.register(Question)
