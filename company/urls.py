from django.urls import path

from .views import companyUpdateView, InfoDeleteView, infoCreateView, InfoUpdateView, CompanyRealUpdateView


urlpatterns = [
    path('update/', companyUpdateView, name="company_update"),
    path('update/<int:pk>/', CompanyRealUpdateView.as_view(), name="company_real_update"),
    path('create/', infoCreateView, name="info_create"),
    path('delete/<int:pk>/', InfoDeleteView.as_view(), name="info_delete"),
    path('update/info/<int:pk>/', InfoUpdateView.as_view(), name="info_update"),

]
