from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

from stock.models import Stock

class Sale(models.Model):
    agent = models.ForeignKey(get_user_model(), on_delete=models.CASCADE )
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(null=True, blank=True)
    discount = models.PositiveIntegerField(default=0, null=True,blank=True)
    client = models.CharField(max_length=250, null=True, blank=True)
    sold_at = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=True, null=True, blank=True)
    is_substracted_from_stock = models.BooleanField(default=False)
    
    class Meta:
        ordering = ("-sold_at",)
        
    def __str__(self):
        return str(self.sold_at.strftime("%D,%H:%M:%S"))
    
    def get_absolute_url(self):
        return reverse("sale_detail", kwargs={"pk": self.pk})
    
    def get_sum_sale(self):
        if self.discount:
            return (self.quantity * self.stock.price) - self.discount
        return self.quantity * self.stock.price