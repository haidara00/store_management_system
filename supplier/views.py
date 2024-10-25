from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy





from .models import Supplier, Debt, Reinbourse

class SupplierCreateView(generic.CreateView):
    model = Supplier
    fields = "__all__"
    template_name = 'supplier/create.html'
    success_url = reverse_lazy("supplier_list")
 

class DebtCreateView(generic.CreateView):
    model = Debt
    fields = "__all__"
    template_name = 'supplier/debt/create.html'
    success_url = reverse_lazy("supplier_list")
class ReinbourseCreateView(generic.CreateView):
    model = Reinbourse
    fields = "__all__"
    template_name = 'supplier/reinbourse/create.html'
    success_url = reverse_lazy("supplier_list")
 
def SupplierListView(request): 
    for supplier in Supplier.objects.all():
        for debt in supplier.debt_set.all():
            if not debt.is_added_to_remainder:
                supplier.remainder += debt.amount
                debt.is_added_to_remainder = True
                debt.save()
                supplier.save()                
        for reinbourse in supplier.reinbourse_set.all():
            if not reinbourse.is_substracted_from_remainder:
                supplier.remainder -= reinbourse.amount
                reinbourse.is_substracted_from_remainder = True
                reinbourse.save()
                supplier.save()
                
    template_name = 'supplier/list.html'
    qset = Supplier.objects.all()
    context ={
        'object_list':qset,
        
        } 
    return render(request,template_name,context)
 
class SupplierDetailView(generic.DetailView):
    model = Supplier
    template_name = 'supplier/detail.html'
    
    

class SupplierUpdateView(generic.UpdateView):
    model = Supplier
    fields = "__all__"
    template_name = 'supplier/update.html'
    success_url = reverse_lazy("supplier_list")

class SupplierDeleteView(generic.DeleteView):
    model = Supplier
    template_name = 'supplier/delete.html'
    success_url = reverse_lazy("supplier_list")

    
    
    
    
