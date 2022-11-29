from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


from product.forms import ProductForm
from product.models import Product

# Create your views here.
class ProductListView(ListView):
    model = Product
    paginate_by = 5

class ProductDetailView(DetailView):
    model = Product
    fields = ["name", "description"]

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    success_url = reverse_lazy("product:product-list")

    form_class = ProductForm

    def form_valid(self, form):
        """Filter to avoid duplicate Product"""
        data = form.cleaned_data
        actual_objects = Product.objects.filter(name=data["name"]).count()
        if actual_objects:
            messages.error(
                self.request,
                f"Producto {data['name']} ya está creada",
            )
            form.add_error("name", ValidationError("Acción no válida"))
            return super().form_invalid(form)
        else:
            messages.success(
                self.request,
                f"Producto: {data['name']}. Creado exitosamente!",
            )
            return super().form_valid(form)

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    fields = ["name", "description"]

    def get_success_url(self):
        product_id = self.kwargs["pk"]
        return reverse_lazy("product:product-detail", kwargs={"pk": product_id})


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy("product:product-list")