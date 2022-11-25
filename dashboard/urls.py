from django.urls import path

from dashboard import views

app_name = 'dashboard'
urlpatterns = [
    path('', view=views.statics, name='statics'),
]
