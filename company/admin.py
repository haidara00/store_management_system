from django.contrib import admin
from django.contrib.admin import StackedInline
from .models import Company, CompanyInfo

class CustomStackedInline(StackedInline):
    model = CompanyInfo
class CustomCompanyAdmin(admin.ModelAdmin):
    list_display = ["name"]
    inlines = [
        CustomStackedInline
    ]

admin.site.register(Company, CustomCompanyAdmin)
admin.site.register(CompanyInfo)

