from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to="logo", null=True, blank=True)

class CompanyInfo(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    index = models.CharField(max_length=15)
    info = models.CharField(max_length=200)
