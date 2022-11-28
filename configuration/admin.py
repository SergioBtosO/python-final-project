from django.contrib import admin

# Register your models here.
from configuration.models import CategoryProduct
from configuration.models import OrderState
from configuration.models import score

admin.site.register(CategoryProduct)
admin.site.register(OrderState)
admin.site.register(score)