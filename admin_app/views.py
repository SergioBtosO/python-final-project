from django.shortcuts import render

from admin_app.models import Categorie

def categories(request):
    categories = Categorie.objects.all()

    context_dict = {"categories": categories}

    return render(
        request=request,
        context=context_dict,
        template_name="admin_app/categorie_list.html",
    )

    


