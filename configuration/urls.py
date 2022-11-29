from django.urls import path

from configuration import views

app_name = 'configuration'

urlpatterns = [
    path("category-products/", views.CategoryProductListView.as_view(), name="category-product-list"),
    path("category-product/add/", views.CategoryProductCreateView.as_view(), name="category-product-add"),
    path("category-product/<int:pk>/detail/", views.CategoryProductDetailView.as_view(), name="category-product-detail"),
    path("category-product/<int:pk>/update/", views.CategoryProductUpdateView.as_view(), name="category-product-update"),
    path("category-product/<int:pk>/delete/", views.CategoryProductDeleteView.as_view(), name="category-product-delete"),
    path("scores/", views.ScoresView.as_view(), name="score-list"),
    path("score/add/", views.ScoreCreateView.as_view(), name="score-add"),
    path("score/<int:pk>/detail/", views.ScoreDetailView.as_view(), name="score-detail"),
    path("score/<int:pk>/update/", views.ScoreUpdateView.as_view(), name="score-update"),
    path("score/<int:pk>/delete/", views.ScoreDeleteView.as_view(), name="score-delete"),
    path("order-state/", views.OrderStateListView.as_view(), name="order-state-list"),
    path("order-state/add/", views.OrderStateCreateView.as_view(), name="order-state-add"),
    path("order-state/<int:pk>/detail/", views.OrderStateDetailView.as_view(), name="order-state-detail"),
    path("order-state/<int:pk>/update/", views.OrderStateUpdateView.as_view(), name="order-state-update"),
    path("order-state/<int:pk>/delete/", views.OrderStateDeleteView.as_view(), name="order-state-delete"),

]