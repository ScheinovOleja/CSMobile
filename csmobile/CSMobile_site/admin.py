from django.contrib import admin
from CSMobile_site.models import Contact, Employee, Status, CustomerContact, Contractor, Message


# Register your models here.


@admin.register(Contact, Employee, Status, CustomerContact, Contractor, Message)
class CSAdmin(admin.ModelAdmin):
    pass
