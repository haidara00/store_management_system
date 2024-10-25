from django.urls import path

from . import views

urlpatterns = [
    path('', views.ArrivalListView, name='arrival_list'),
    path('create/', views.arrivalCreateView, name='arrival_create'),
    path('<int:pk>/', views.ArrivalDetailView.as_view(), name='arrival_detail'),
    path('delete/<int:pk>/', views.ArrivalDeleteView.as_view(), name='arrival_delete'),
    path('update/<int:pk>/', views.ArrivalUpdateView.as_view(), name='arrival_update'),
]
