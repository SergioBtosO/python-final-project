from django.contrib import admin

# Register your models here.
from product.models import Product
from product.models import Question

admin.site.register(Product)
admin.site.register(Question)

