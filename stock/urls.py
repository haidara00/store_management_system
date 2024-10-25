from django.urls import path

from . import views

urlpatterns = [
    path('', views.StockListView, name='stock_list'),
    path('category/<str:category_name>/', views.listCategoryView, name='category_list'),
    path('create/', views.StockCreateView.as_view(), name='stock_create'),
    path('<int:stock_id>/', views.stockDetailView, name='stock_detail'),
    path('delete/<int:pk>/', views.StockDeleteView.as_view(), name='stock_delete'),
    path('update/<int:pk>/', views.StockUpdateView.as_view(), name='stock_update'),
    path('table/', views.tableView, name="table_list"),
]
