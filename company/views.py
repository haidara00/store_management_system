from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.f


from .models import Company, CompanyInfo


login = "account_login"
class CompanyUpdateForm(forms.ModelForm):

    class Meta:
        model = Company
        fields = "__all__"

        
class CompanyInfoCreateForm(forms.ModelForm):
    index = forms.CharField(required=False)
    info = forms.CharField(required=False)
    class Meta:
        model = CompanyInfo
        fields = ("index", "info")

@login_required        
def companyUpdateView(request):
    company = Company.objects.get(id=1)
    infos = company.companyinfo_set.all()
    return render(request, "company/company_update.html",{"object":company, "infos":infos})

class InfoDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = CompanyInfo
    template_name = "company/info_delete.html"
    success_url = reverse_lazy("company_update")
    login_url = login
    
@login_required
def infoCreateView(request):
    if request.method == "POST":
        form = CompanyInfoCreateForm(request.POST)
        if form.is_valid():
            info = form.save(commit=False)
            info.company = request.user.company
            info.save()
            return HttpResponseRedirect(reverse_lazy("company_update"))
    else:
        form = CompanyInfoCreateForm()
    return render(request,"company/info_create.html", {"form":form})
            
class InfoUpdateView(LoginRequiredMixin,generic.UpdateView):
    model = CompanyInfo
    template_name = "company/info_update.html"
    success_url = reverse_lazy("company_update")
    fields = ("index", "info")
    login_url = login
class CompanyRealUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Company
    template_name = "company/company_real_update.html"
    success_url = reverse_lazy("company_update")
    fields = ("name", "logo")
    login_url = login
    
   
    

