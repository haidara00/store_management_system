from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)

class CompanyInfo(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    index = models.CharField(max_length=15)
    info = models.CharField(max_length=200)
