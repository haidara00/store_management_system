from django.urls import path

from . import views

urlpatterns = [
    path('', views.SupplierListView, name='supplier_list'),
    path('create/', views.SupplierCreateView.as_view(), name='supplier_create'),
    path('<int:pk>/', views.SupplierDetailView.as_view(), name='supplier_detail'),
    path('delete/<int:pk>/', views.SupplierDeleteView.as_view(), name='supplier_delete'),
    path('update/<int:pk>/', views.SupplierUpdateView.as_view(), name='supplier_update'),
    path('debt/create/', views.DebtCreateView.as_view(), name='debt_create'),
    path('reinbourse/create/', views.ReinbourseCreateView.as_view(), name='reinbourse_create'),
]
