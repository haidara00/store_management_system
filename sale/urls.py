from django.urls import path

from . import views

urlpatterns = [
    path('', views.SaleListView, name='sale_list'),
    path('create/', views.saleCreateView, name='sale_create'),
    path('<int:pk>/', views.SaleDetailView.as_view(), name='sale_detail'),
    path('print/<int:sale_id>/', views.print_pdf, name='sale_print'),
    path('delete/<int:pk>/', views.SaleDeleteView.as_view(), name='sale_delete'),
    path('update/<int:pk>/', views.SaleUpdateView.as_view(), name='sale_update'),
]
