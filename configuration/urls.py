from django.urls import path

from configuration import views

app_name = 'configuration'

urlpatterns = [
    path("category-products/", views.CategoryProductListView.as_view(), name="category-product-list"),
    path("category-product/add/", views.CategoryProductCreateView.as_view(), name="category-product-add"),
    path("category-product/<int:pk>/detail/", views.CategoryProductDetailView.as_view(), name="category-product-detail"),
    path("category-product/<int:pk>/update/", views.CategoryProductUpdateView.as_view(), name="category-product-update"),
    path("category-product/<int:pk>/delete/", views.CategoryProductDeleteView.as_view(), name="category-product-delete"),

]