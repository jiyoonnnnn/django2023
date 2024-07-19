from django.contrib import admin
from .models import Comwrite, Sale
# Register your models here.

class ComwriteAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(Comwrite,ComwriteAdmin)

class SaleAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(Sale,SaleAdmin)
