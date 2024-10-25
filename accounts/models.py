from django.db import models
from django.contrib.auth.models import AbstractUser

from company.models import Company

class CustomUser(AbstractUser):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
