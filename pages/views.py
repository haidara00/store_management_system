from django.shortcuts import render, get_object_or_404
from supplier.models import Supplier
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.views.generic import TemplateView
from .forms import UserCreateForm



@login_required
def homeView(request):
    allTheDebts = 0
    
    for supplier in Supplier.objects.all():
        allTheDebts += supplier.remainder
    
    
    return render(request, "home.html",{'sumDebt': allTheDebts,
        
    })
@login_required
def agentView(request):
    query = get_user_model().objects.all()
    return render(request,"agent_list.html",{"object_list":query})

@login_required
def agentDetail(request, agent_id):
    if request.user.is_superuser:
        agent = get_object_or_404(get_user_model(),id=agent_id)
        return render(request,"agent_detail.html",{"object":agent})


@login_required
def agentCreate(request):
    if request.user.is_superuser:
        is_save = None
        if request.method == "POST":
            form = UserCreateForm(request.POST)
            if form.is_valid():
                

                is_save = form.save()
                is_save.company = request.user.company
                is_save.save()
        else:
            form = UserCreateForm()
        return render(request,"agent_create.html",{"form":form, "is_save":is_save})


