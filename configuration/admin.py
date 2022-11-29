from django.contrib import admin

# Register your models here.
from configuration.models import CategoryProduct, Score, OrderState

admin.site.register(CategoryProduct)
admin.site.register(Score)
admin.site.register(OrderState)
