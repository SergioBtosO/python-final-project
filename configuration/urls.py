from django.urls import path

from configuration import views

app_name = 'configuration'

urlpatterns = [
    path("category-products/", views.CategoryProductListView.as_view(), name="category-product-list"),
    path("category-product/add/", views.CategoryProductCreateView.as_view(), name="category-product-add"),
    path("category-product/<int:pk>/detail/", views.CategoryProductDetailView.as_view(), name="category-product-detail"),
    path("category-product/<int:pk>/update/", views.CategoryProductUpdateView.as_view(), name="category-product-update"),
    path("category-product/<int:pk>/delete/", views.CategoryProductDeleteView.as_view(), name="category-product-delete"),
    path("userinfo/", views.UserInfoListView.as_view(), name="user-info-list"),
    path("userinfo/add/", views.UserInfoCreateView.as_view(), name="user-info-add"),
    path("userinfo/<int:pk>/detail/", views.UserInfoDetailView.as_view(), name="user-info-detail"),
    path("order-state/", views.OrderStateListView.as_view(), name="order-state-list"),
    path("order-state/add/", views.OrderStateCreateView.as_view(), name="order-state-add"),
    path("order-state/<int:pk>/detail/", views.OrderStateDetailView.as_view(), name="order-state-detail"),
    path("order-state/<int:pk>/update/", views.OrderStateUpdateView.as_view(), name="order-state-update"),
    path("order-state/<int:pk>/delete/", views.OrderStateDeleteView.as_view(), name="order-state-delete"),
    path("orders/", views.OrdersListView.as_view(), name="orders-list"),
    path("orders/add/", views.OrdersCreateView.as_view(), name="orders-add"),
    path("orders/<int:pk>/detail/", views.OrdersDetailView.as_view(), name="orders-detail"),
    path("orders/<int:pk>/update/", views.OrdersUpdateView.as_view(), name="orders-update"),
    path("orders/<int:pk>/delete/", views.OrdersDeleteView.as_view(), name="orders-delete"),
]