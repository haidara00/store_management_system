from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from stock.models import Stock
from sale.models import Sale


from .models import Arrival
from .forms import ArrivalForm




class ArrivalCreateView(generic.CreateView):
    model = Arrival
    fields = ("agent","stock", "quantity")
    template_name = 'arrival/create.html'
    success_url = reverse_lazy("arrival_list")
    
def arrivalCreateView(request):
    arrival = None
    if request.method == "POST":
        
        form = ArrivalForm(request.POST)
        if form.is_valid():
            arrival = form.save(commit=False)
            arrival.agent = request.user
            arrival.save()
            for stock in Stock.objects.all():
                for arrival in stock.arrival_set.all():
                    if not arrival.is_added_to_stock:
                        stock.quantity += arrival.quantity
                        arrival.is_added_to_stock = True
                        arrival.save()
                        stock.save()
                for sale in stock.sale_set.all():
                    if not sale.is_substracted_from_stock:
                        stock.quantity -= sale.quantity
                        sale.is_substracted_from_stock = True
                        sale.save()
                        stock.save()
            
                      
    else:
        form = ArrivalForm()
    return render(request, 'arrival/create.html', {"form":form, "arrival":arrival})
   

def ArrivalListView(request):    
    template_name = 'arrival/list.html'
    qset = Arrival.objects.all()
    context = {
        'object_list':qset
        } 
    return render(request,template_name,context)
    

class ArrivalDetailView(generic.DetailView):
    model = Arrival
    template_name = 'arrival/detail.html'
    
    

class ArrivalUpdateView(generic.UpdateView):
    model = Arrival
    fields = "__all__"
    template_name = 'arrival/update.html'
    success_url = reverse_lazy("arrival_list")

class ArrivalDeleteView(generic.DeleteView):
    model = Arrival
    template_name = 'arrival/delete.html'
    success_url = reverse_lazy("arrival_list")

    
    
    
    
