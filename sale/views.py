from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse_lazy
from stock.models import Stock
from arrival.models import Arrival
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from weasyprint import HTML
from company.models import Company
from django.contrib.auth import get_user_model



from .forms import SaleForm, Sale



class SaleCreateView(generic.CreateView):
    form_class = SaleForm
    template_name = 'sale/create.html'
    success_url = reverse_lazy("sale_create")
    
    def form_valid(self, form):
        form.instance.agent = self.request.user
        return super().form_valid(form)

@login_required
def saleCreateView(request):
    is_greater_than_total_quantity = False
    is_equal_to_0 = False
    is_all_done = False
    newsale = None
    if request.method == "POST":  
        form = SaleForm(request.POST)
        
        if form.is_valid():
            newsale = form.save(commit=False)
            if newsale.quantity > newsale.stock.quantity:
                is_greater_than_total_quantity = True
                #return HttpResponse(f"Operation Impossible!\n On a pas suffisament de stock pour ça. Il {sale.stock.quantity}")
            elif newsale.quantity == 0:
                is_equal_to_0 = True
                #return HttpResponse("Impossible d'effectuée tel operation")
            else:
                newsale.agent = request.user
                newsale.save()
                
                is_all_done = True
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
                
                
            #return HttpResponse("Effectuée Avec Success!")
    else:
        form = SaleForm()
        try:
            if Company.objects.get(id=1):
                company = Company.objects.get(id=1)
                agent = request.user
                if agent.company != company:
                    agent.company = company
        except:
            pass
            
            
    return render(request,"sale/create.html",{"form":form,"is_all_done":is_all_done, "is_greater_than_total_quantity":is_greater_than_total_quantity, "is_equal_to_O":is_equal_to_0,"sale":newsale})       
    
    
    
    
   
    
    
    
            
   
@login_required
def SaleListView(request):
    
    template_name = 'sale/list.html'
    qset = Sale.objects.filter(agent=request.user).order_by("-sold_at")
    context ={
        'object_list':qset
        } 
    return render(request,template_name,context)
    

class SaleDetailView(generic.DetailView):
    model = Sale
    template_name = 'sale/detail.html'
    

class SaleUpdateView(generic.UpdateView):
    model = Sale
    fields = SaleForm.Meta.fields
    template_name = 'sale/update.html'
    success_url = reverse_lazy("sale_list")

class SaleDeleteView(generic.DeleteView):
    model = Sale
    template_name = 'sale/delete.html'
    success_url = reverse_lazy("sale_list")
  
def print_pdf(request, sale_id):
    sale = get_object_or_404(Sale, id=sale_id)
    company = get_object_or_404(Company, id=1)
    sale.agent.company = company
    sale.save()
    
    
    html = render_to_string("sale/pdf.html",{"object":sale, 'companyinfos':company.companyinfo_set.all()[:4]})
    
    response = HttpResponse(content_type="application/pdf")
    response["Content-Dispositive"] = f"file_name=sale_{sale_id}.pdf"
    HTML(string=html).write_pdf(response)
    return response
    
    
    
    
    
    
