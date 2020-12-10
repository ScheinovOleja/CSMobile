from django.contrib import admin
from CSMobile_site.models import FinalDB

# Register your models here.


@admin.register(FinalDB)
class CSAdmin(admin.ModelAdmin):
    pass
