from django.contrib import admin

# Register your models here.
from dashboard.models import UserInfo, UserQualification

admin.site.register(UserInfo)
admin.site.register(UserQualification)
