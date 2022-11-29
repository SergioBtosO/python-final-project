from django.urls import path

from product import views

app_name = 'product'

urlpatterns = [
    path("", views.ProductListView.as_view(), name="product-list"),
    path("add/", views.ProductCreateView.as_view(), name="product-add"),
    path("<int:pk>/detail/", views.ProductDetailView.as_view(), name="product-detail"),
    path("<int:pk>/update/", views.ProductUpdateView.as_view(), name="product-update"),
    path("<int:pk>/delete/", views.ProductDeleteView.as_view(), name="product-delete"),
]