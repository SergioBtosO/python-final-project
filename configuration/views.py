from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from configuration.forms import CategoryProductform

from configuration.models import CategoryProduct

# Create your views here.
class CategoryProductListView(ListView):
    model = CategoryProduct
    paginate_by = 5

class CategoryProductDetailView(DetailView):
    model = CategoryProduct
    fields = ["name", "description"]

class CategoryProductCreateView(LoginRequiredMixin, CreateView):
    model = CategoryProduct
    success_url = reverse_lazy("configuration:category-product-list")

    form_class = CategoryProductform

    def form_valid(self, form):
        """Filter to avoid duplicate CategoryProduct"""
        data = form.cleaned_data
        actual_objects = CategoryProduct.objects.filter(name=data["name"]).count()
        if actual_objects:
            messages.error(
                self.request,
                f"La categoria {data['name']} ya está creada",
            )
            form.add_error("name", ValidationError("Acción no válida"))
            return super().form_invalid(form)
        else:
            messages.success(
                self.request,
                f"Categoria: {data['name']}. Creada exitosamente!",
            )
            return super().form_valid(form)

class CategoryProductUpdateView(LoginRequiredMixin, UpdateView):
    model = CategoryProduct
    fields = ["name", "description"]

    def get_success_url(self):
        category_product_id = self.kwargs["pk"]
        return reverse_lazy("configuration:category-product-detail", kwargs={"pk": category_product_id})


class CategoryProductDeleteView(LoginRequiredMixin, DeleteView):
    model = CategoryProduct
    success_url = reverse_lazy("configuration:category-product-list")    