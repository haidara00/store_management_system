from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.forms import ModelForm
from django.contrib.auth.mixins import LoginRequiredMixin

from arrival.models import Arrival
from sale.models import Sale

from .models import Stock, Category

class CategoryCreateForm(ModelForm):
    class Meta:
        model = Category
        fields = ("name",)

@login_required
def categoryCreate(request):
    
    if request.method == "POST":
        form = CategoryCreateForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect(reverse_lazy("stock_list"))
            
    else:
        form = CategoryCreateForm()
    return render(request, "stock/category_create.html",{"form":form})
login = "account_login"   
class StockCreateView(LoginRequiredMixin, generic.CreateView):
    model = Stock
    fields = ("name", "initial_quantity", "price", "description", "categories")
    template_name = 'stock/create.html'
    def form_valid(self, form):
        
        form.instance.quantity = form.instance.initial_quantity
        return super().form_valid(form)
    
    success_url = reverse_lazy("stock_list")
    login_url = login
@login_required
def StockListView(request): 
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
    template_name = 'stock/list.html'
    qset = Stock.objects.order_by('quantity')
    context ={
        'object_list':qset,
        'categories': Category.objects.all()
        
        } 
    return render(request,template_name,context)
@login_required
def listCategoryView(request, category_name):
    template_name = "stock/category_filter.html"
    object_list = Stock.objects.filter(categories__name=category_name)
    return render(request, template_name, {
        'object_list': object_list,
        'category_name': category_name,
        'categories': Category.objects.all(),
    })
    
 
class StockDetailView(LoginRequiredMixin, generic.DetailView):
    model = Stock
    template_name = 'stock/detail.html'
    login_url = login
    
@login_required 
def stockDetailView(request, stock_id):
    stock = get_object_or_404(Stock, id=stock_id)
    
    total_arrival = 0
    for arrival in stock.arrival_set.all():
        total_arrival += arrival.quantity
    
    return render(request,'stock/detail.html',{'object':stock, "total_arrival":total_arrival} )
     
    

class StockUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Stock
    fields = "__all__"
    template_name = 'stock/update.html'
    success_url = reverse_lazy("stock_list")
    login_url = login

class StockDeleteView(LoginRequiredMixin,generic.DeleteView):
    model = Stock
    template_name = 'stock/delete.html'
    success_url = reverse_lazy("stock_list")
    login_url = login
    
def tableView(request):
    stocks = Stock.objects.all()

        
    return render(request,"stock/stock_table.html", {"stocks":stocks})

    
    
    
    
