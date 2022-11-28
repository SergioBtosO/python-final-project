from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from dashboard.forms import UserInfoform
from dashboard.models import UserInfo

from dashboard.forms import UserQualification
from dashboard.models import UserQualification

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
    success_url = reverse_lazy("dashboard:user-info-list")

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

class UserInfoUpdateView(LoginRequiredMixin, UpdateView):
    model = UserInfo
    fields = ["name", "description", "state"]

    def get_success_url(self):
        User_Info_id = self.kwargs["pk"]
        return reverse_lazy("dashboard:User-Info-detail", kwargs={"pk": User_Info_id})


class UserInfoDeleteView(LoginRequiredMixin, DeleteView):
    model = UserInfo
    success_url = reverse_lazy("dashboard:User-Info-list")


class UserQualificationDetailView(DetailView):
    model = UserQualification
    fields = ["user-name", "email"]

class UserQualificationCreateView(LoginRequiredMixin, CreateView):
    model = UserQualification
    success_url = reverse_lazy("dashboard:User-Qualification-list")

    form_class = UserQualification

    def form_valid(self, form):
        """Filter to avoid duplicate Score"""
        data = form.cleaned_data
        actual_objects = UserQualification.objects.filter(name=data["name"]).count()
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

class UserQualificationUpdateView(LoginRequiredMixin, UpdateView):
    model = UserQualification
    fields = ["name", "description", "state"]

    def get_success_url(self):
        User_Qualification_id = self.kwargs["pk"]
        return reverse_lazy("dashboard:User-Qualification-detail", kwargs={"pk": User_Qualification_id})


class UserQualificationDeleteView(LoginRequiredMixin, DeleteView):
    model = UserQualification
    success_url = reverse_lazy("dashboard:User-Qualification-list")