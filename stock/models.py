from django.db import models
from django.urls import reverse

# stock: name, quantity, added_date, 

class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Stock(models.Model):
    name = models.CharField(max_length=255)
    initial_quantity = models.IntegerField(default=0, null=True, blank=True)
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=8, decimal_places=2,null=True, blank=True)
    added_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(null=True, blank=True)
    categories = models.ManyToManyField(Category)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("stock_detail", kwargs={"stock_id": self.pk})
    
    def get_total_sale(self):
        total = 0
        for sale in self.sale_set.all():
            total += sale.quantity
        return total
    def get_total_arrival(self):
        total = 0
        for arrival in self.arrival_set.all():
            total += arrival.quantity
        return total
    def get_initial_quantity(self):
        return self.initial_quantity
    


    
