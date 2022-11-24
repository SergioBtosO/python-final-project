from django.urls import path

from admin_app import views

app_name = 'admin_app'
urlpatterns = [
    path('', view=views.categories, name='categorie-list'),
    
]
