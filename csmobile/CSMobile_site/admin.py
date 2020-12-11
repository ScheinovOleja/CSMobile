from django.contrib import admin
from CSMobile_site.models import Contact, Employee, Status, CostumerContact, Contractor, Request


# Register your models here.


@admin.register(Contact, Employee, Status, CostumerContact, Contractor, Request)
class CSAdmin(admin.ModelAdmin):
    pass
