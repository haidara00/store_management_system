from django.db import models
from django.urls import reverse, reverse_lazy
from django.utils import timezone

# Create your models here.
class Supplier(models.Model):
    # image field should be added.
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.PositiveIntegerField(null=True, blank=True)
    email = models.EmailField(max_length=254,null=True, blank=True)
    is_male = models.BooleanField(default=None, null=True, blank=True)
    remainder = models.DecimalField(default=0.00,max_digits=8, decimal_places=2)
    
    def __str__(self):
        return self.first_name.title() + " " + self.last_name.upper()
    
    def get_absolute_url(self):
        return reverse("supplier_detail", kwargs={"pk": self.pk})
     
    def get_gender(self):
        if self.is_male:
            return "Masculin"
        elif self.is_male == False:
            return "Feminin"
        return "Inconnu"
    
    def get_sum_of_debts(self):
        current_debt_list = self.debt_set.all()
        allDebt = 0
        if current_debt_list:
            for i in current_debt_list:
                allDebt += i.amount
        return allDebt
    
    def get_sum_of_reinbouse(self):
        current_reinbourse_list = self.reinbouse_set.all()
        allReinbourse = 0
        if current_reinbourse_list:
            for i in current_reinbourse_list:
                allReinbourse += i.amount
        return allReinbourse
    
    def get_balance(self):
        results = self.get_sum_of_debts - self.get_sum_of_reinbouse
        if results >= 0:
            return f"Il vous rest {results}FCFA."
        return f"Vous avez {-results}FCFA en avance chez {self.first_name.title()}."


class Debt(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    borrowed_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    is_added_to_remainder = models.BooleanField(default=False)

    
    def __str__(self):
        return str(self.amount) + "FCFA at " + str(self.borrowed_at.date())
    
    def get_absolute_url(self):
        return reverse("debt_detail", kwargs={"pk": self.pk})
    
    

class Reinbourse(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    paid_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    is_substracted_from_remainder = models.BooleanField(default=False)
    
    
    
    
    def __str__(self):
        return str(self.amount) + "FCFA at " + str(self.paid_at.date())
    
    
        
    