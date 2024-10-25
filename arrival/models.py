from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


from stock.models import Stock

class Arrival(models.Model):
    agent = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    arrived_at = models.DateField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_added_to_stock = models.BooleanField(default=False)
    
    
    
    def __str__(self):
        return str(self.arrived_at)
    
    def get_absolute_url(self):
        return reverse("arrival_detail", kwargs={"pk": self.pk})
    
    