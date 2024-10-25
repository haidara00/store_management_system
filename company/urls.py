from django.urls import path

from .views import companyUpdateView, companyInfoDeleteView


urlpatterns = [
    path('update/', companyUpdateView, name="company_update"),
    path('<int:info_id>/delete/', companyInfoDeleteView, name="company_delete")
]
