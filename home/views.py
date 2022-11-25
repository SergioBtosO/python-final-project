from django.contrib import messages
from django.shortcuts import redirect
from django.shortcuts import render

from home.forms import UserRegisterForm

# Create your views here.
def index(request):
    return render(
        request=request, 
        context={}, 
        template_name='home/index.html'
    )

def contact(request):
    return render(
        request=request, 
        context={}, 
        template_name='home/contact.html'
    )

def register(request):
    form = UserRegisterForm(request.POST) if request.POST else UserRegisterForm()
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Usuario creado exitosamente!")
            return redirect("/auth/login")

    return render(
        request=request,
        context={"form": form},
        template_name="registration/register.html",
    )
