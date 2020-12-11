from django.contrib import admin
from CSMobile_site.models import Client, Employee, Status, CostumerContact, Contractor, Application


# Register your models here.


@admin.register(Client, Employee, Status, CostumerContact, Contractor, Application)
class CSAdmin(admin.ModelAdmin):
    pass
