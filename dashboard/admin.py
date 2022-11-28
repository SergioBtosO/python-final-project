from django.contrib import admin

# Register your models here.
from dashboard.models import UserInfo, Score

admin.site.register(UserInfo)
admin.site.register(Score)
