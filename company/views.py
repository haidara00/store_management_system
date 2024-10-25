from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from django import forms

# Create your views here.f


from .models import Company, CompanyInfo

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
        
def companyUpdateView(request):
    obj = get_object_or_404(Company, id=1) 
    form = CompanyUpdateForm(request.POST or obj.name, instance=obj)
    if form.is_valid():
        form.save()
        #return HttpResponse("<h1>Effectué avec Success!</h1>")
    # companyInfo create View
    if request.method == "POST":
        infoform = CompanyInfoCreateForm(request.POST)
        if infoform.is_valid() and infoform.cleaned_data["index"] != "" and infoform.cleaned_data["info"]!="" :
            info = infoform.save(commit=False)
            info.company = obj
            info.save()
            #return HttpResponse("<h1>Effectué avec Success!</h1>")
    else:
        infoform = CompanyInfoCreateForm()
    return render(request, "company/company_update.html",{"form":form, 'company':obj, "infoform":infoform} )


def companyInfoDeleteView(request, info_id):
    info = get_object_or_404(CompanyInfo, id=info_id)
    info.delete()
    return HttpResponseRedirect("company_update")




