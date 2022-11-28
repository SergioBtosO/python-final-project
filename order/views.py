from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.
from order.forms import Orderform
from order.models import Order

from order.forms import OrderDetailform
from order.models import OrderDetail


class OrderListView(ListView):
    model = Order
    paginate_by = 5

class OrdersDetailView(DetailView):
    model = Order
    fields = ["name", "description", "state"]

class OrderCreateView(LoginRequiredMixin, CreateView):
    model = Order
    success_url = reverse_lazy("configuration:order-list")

    form_class = Orderform

    def form_valid(self, form):
        """Filter to avoid duplicate orders"""
        data = form.cleaned_data
        actual_objects = Order.objects.filter(name=data["name"]).count()
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

class OrderUpdateView(LoginRequiredMixin, UpdateView):
    model = Order
    fields = ["name", "description", "state"]

    def get_success_url(self):
        order_id = self.kwargs["pk"]
        return reverse_lazy("configuration:order-detail", kwargs={"pk": order_id})


class OrderDeleteView(LoginRequiredMixin, DeleteView):
    model = Order
    success_url = reverse_lazy("configuration:order-list")



class OrderDetailListView(ListView):
    model = OrderDetail
    paginate_by = 5

class OrderDetailDetailView(DetailView):
    model = OrderDetail
    fields = ["name", "description", "state"]

class OrderDetailCreateView(LoginRequiredMixin, CreateView):
    model = OrderDetail
    success_url = reverse_lazy("configuration:order-detail-list")

    form_class = OrderDetailform

    def form_valid(self, form):
        """Filter to avoid duplicate order detail"""
        data = form.cleaned_data
        actual_objects = Order.objects.filter(name=data["name"]).count()
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

class OrderDetailUpdateView(LoginRequiredMixin, UpdateView):
    model = OrderDetail
    fields = ["name", "description", "state"]

    def get_success_url(self):
        OrderDetail_id = self.kwargs["pk"]
        return reverse_lazy("configuration:order-detail-detail", kwargs={"pk": OrderDetail_id})


class OrderDetailDeleteView(LoginRequiredMixin, DeleteView):
    model = OrderDetail
    success_url = reverse_lazy("configuration:order-detail-list")