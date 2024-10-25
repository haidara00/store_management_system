from django.contrib import admin

from .models import Supplier, Debt, Reinbourse

admin.site.register(Supplier)
admin.site.register(Debt)
admin.site.register(Reinbourse)
