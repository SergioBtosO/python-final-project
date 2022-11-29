from django.urls import path

from product import views

app_name = 'product'

urlpatterns = [
    path("", views.ProductListView.as_view(), name="product-list"),
    path("add/", views.ProductCreateView.as_view(), name="product-add"),
    path("<int:pk>/detail/", views.ProductDetailView.as_view(), name="product-detail"),
    path("<int:pk>/update/", views.ProductUpdateView.as_view(), name="product-update"),
    path("<int:pk>/delete/", views.ProductDeleteView.as_view(), name="product-delete"),
    path("", views.QuestionListView.as_view(), name="question-list"),
    path("add/", views.QuestionCreateView.as_view(), name="question-add"),
    path("<int:pk>/detail/", views.QuestionDetailView.as_view(), name="question-detail"),
    path("<int:pk>/update/", views.QuestionUpdateView.as_view(), name="question-update"),
    path("<int:pk>/delete/", views.QuestionDeleteView.as_view(), name="question-delete"),
]
