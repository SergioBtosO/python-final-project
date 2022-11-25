from django.shortcuts import render

# Create your views here.
def statics(request):
    return render(
        request=request, 
        context={}, 
        template_name='dashboard/statics.html'
    )