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



from configuration.forms import OrderStateform
from configuration.models import OrderState

from configuration.forms import Ordersform
from configuration.models import Orders

from configuration.forms import ProductForm
from configuration.models import Product

from configuration.forms import QuestionForm
from configuration.models import Question



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





class OrderStateListView(ListView):
    model = OrderState
    paginate_by = 5

class OrderStateDetailView(DetailView):
    model = OrderState
    fields = ["name", "description", "state"]

class OrderStateCreateView(LoginRequiredMixin, CreateView):
    model = OrderState
    success_url = reverse_lazy("configuration:order-state-list")

    form_class = OrderStateform

    def form_valid(self, form):
        """Filter to avoid duplicate OrderState"""
        data = form.cleaned_data
        actual_objects = OrderState.objects.filter(name=data["name"]).count()
        if actual_objects:
            messages.error(
                self.request,
                f"La orden {data['name']} ya está creada",
            )
            form.add_error("name", ValidationError("Acción no válida"))
            return super().form_invalid(form)
        else:
            messages.success(
                self.request,
                f"orden: {data['name']}. Creada exitosamente!",
            )
            return super().form_valid(form)

class OrderStateUpdateView(LoginRequiredMixin, UpdateView):
    model = OrderState
    fields = ["name", "description", "state"]

    def get_success_url(self):
        order_state_id = self.kwargs["pk"]
        return reverse_lazy("configuration:order-state-detail", kwargs={"pk": order_state_id})


class OrderStateDeleteView(LoginRequiredMixin, DeleteView):
    model = OrderState
    success_url = reverse_lazy("configuration:order-state-list")



class OrdersListView(ListView):
    model = Orders
    paginate_by = 5

class OrdersDetailView(DetailView):
    model = Orders
    fields = ["name", "description", "state"]

class OrdersCreateView(LoginRequiredMixin, CreateView):
    model = Orders
    success_url = reverse_lazy("configuration:orders-list")

    form_class = Ordersform

    def form_valid(self, form):
        """Filter to avoid duplicate orders"""
        data = form.cleaned_data
        actual_objects = Orders.objects.filter(name=data["name"]).count()
        if actual_objects:
            messages.error(
                self.request,
                f"La orden {data['name']} ya está creada",
            )
            form.add_error("name", ValidationError("Acción no válida"))
            return super().form_invalid(form)
        else:
            messages.success(
                self.request,
                f"orden: {data['name']}. Creada exitosamente!",
            )
            return super().form_valid(form)

class OrdersUpdateView(LoginRequiredMixin, UpdateView):
    model = Orders
    fields = ["name", "description", "state"]

    def get_success_url(self):
        orders_id = self.kwargs["pk"]
        return reverse_lazy("configuration:orders-detail", kwargs={"pk": orders_id})


class OrdersDeleteView(LoginRequiredMixin, DeleteView):
    model = Orders
    success_url = reverse_lazy("configuration:orders-list")


class ProductListView(ListView):
    model = Product
    paginate_by = 5

class ProductDetailView(DetailView):
    model = Product
    fields = ["name", "description"]

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    success_url = reverse_lazy("configuration:product-list")

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
        return reverse_lazy("configuration:product-detail", kwargs={"pk": product_id})


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy("configuration:product-list")  


class QuestionListView(ListView):
    model = Question
    paginate_by = 5

class QuestionDetailView(DetailView):
    model = Question
    fields = ["name", "description"]

class QuestionCreateView(LoginRequiredMixin, CreateView):
    model = Question
    success_url = reverse_lazy("configuration:Question-list")

    form_class = QuestionForm

    def form_valid(self, form):
        """Filter to avoid duplicate Question"""
        data = form.cleaned_data
        actual_objects = Question.objects.filter(name=data["name"]).count()
        if actual_objects:
            messages.error(
                self.request,
                f"La pregunta {data['name']} ya fue formulada",
            )
            form.add_error("name", ValidationError("Acción no válida"))
            return super().form_invalid(form)
        else:
            messages.success(
                self.request,
                f"pregunta: {data['name']}. enviada!",
            )
            return super().form_valid(form)

class QuestionUpdateView(LoginRequiredMixin, UpdateView):
    model = Question
    fields = ["name", "description"]

    def get_success_url(self):
        Question_id = self.kwargs["pk"]
        return reverse_lazy("configuration:Question-detail", kwargs={"pk": Question_id})


class QuestionDeleteView(LoginRequiredMixin, DeleteView):
    model = Question
    success_url = reverse_lazy("configuration:Question-list")    

