from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from configuration.forms import UserInfoform
from configuration.models import UserInfo

# Create your views here.
@login_required
def statics(request):
    return render(
        request=request, 
        context={}, 
        template_name='dashboard/statics.html'
    )

# Views User Info
class UserInfoDetailView(DetailView):
    model = UserInfo
    fields = ["user-name", "email"]

class UserInfoCreateView(LoginRequiredMixin, CreateView):
    model = UserInfo
    success_url = reverse_lazy("configuration:user-list")

    form_class = UserInfo

    def form_valid(self, form):
        """Filter to avoid duplicate UserInfo"""
        data = form.cleaned_data
        actual_objects = UserInfo.objects.filter(name=data["name"]).count()
        if actual_objects:
            messages.error(
                self.request,
                f"El usuario {data['name']} ya existe",
            )
            form.add_error("name", ValidationError("Acción no válida"))
            return super().form_invalid(form)
        else:
            messages.success(
                self.request,
                f"Usuario: {data['name']}. Creado exitosamente!",
            )
            return super().form_valid(form)