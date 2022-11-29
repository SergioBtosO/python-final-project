from django.contrib import admin

# Register your models here.
from configuration.models import CategoryProduct, OrderState


admin.site.register(CategoryProduct)
admin.site.register(OrderState)
