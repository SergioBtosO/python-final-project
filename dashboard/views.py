from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def statics(request):
    return render(
        request=request, 
        context={}, 
        template_name='dashboard/statics.html'
    )