from django.urls import path

from product import views

app_name = 'product'

urlpatterns = [
    path("", views.ProductListView.as_view(), name="product-list"),
    path("add/", views.ProductCreateView.as_view(), name="product-add"),
    path("<int:pk>/detail/", views.ProductDetailView.as_view(), name="product-detail"),
    path("<int:pk>/update/", views.ProductUpdateView.as_view(), name="product-update"),
    path("<int:pk>/delete/", views.ProductDeleteView.as_view(), name="product-delete"),
    path("question/<int:pk>/add/", views.QuestionCreateView.as_view(), name="question-create"),
    path("question/<int:pk>/delete/", views.QuestionDeleteView.as_view(), name="question-delete"),
]
