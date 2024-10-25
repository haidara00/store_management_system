from django.urls import path

from .views import homeView, agentView, agentDetail, agentCreate
from sale.views import saleCreateView
from stock.views import categoryCreate

urlpatterns = [
    path('',saleCreateView, name="home"),
    path('accounts/agents/',agentView, name="agents"),
    path('accounts/agent/create/',agentCreate, name="agent_create"),
    path('accounts/agents/<int:agent_id>/',agentDetail, name="agent_detail"),
    
    path('category/create/',categoryCreate, name="category_create"),

    
]
