from django.urls import path

from configuration import views

app_name = 'configuration'

urlpatterns = [
    path("category-products/", views.CategoryProductListView.as_view(), name="category-product-list"),
    path("category-product/add/", views.CategoryProductCreateView.as_view(), name="category-product-add"),
    path("category-product/<int:pk>/detail/", views.CategoryProductDetailView.as_view(), name="category-product-detail"),
    path("category-product/<int:pk>/update/", views.CategoryProductUpdateView.as_view(), name="category-product-update"),
    path("category-product/<int:pk>/delete/", views.CategoryProductDeleteView.as_view(), name="category-product-delete"),
    path("order-state/", views.OrderStateListView.as_view(), name="order-state-list"),
    path("order-state/add/", views.OrderStateCreateView.as_view(), name="order-state-add"),
    path("order-state/<int:pk>/detail/", views.OrderStateDetailView.as_view(), name="order-state-detail"),
    path("order-state/<int:pk>/update/", views.OrderStateUpdateView.as_view(), name="order-state-update"),
    path("order-state/<int:pk>/delete/", views.OrderStateDeleteView.as_view(), name="order-state-delete"),

]