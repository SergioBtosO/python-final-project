from django.urls import path

from home import views

app_name = 'home'
urlpatterns = [
    path('', view=views.index, name='index'),
    path('contact', view=views.contact, name='contact'),
    path('register', view=views.register, name='register'),
    
]
