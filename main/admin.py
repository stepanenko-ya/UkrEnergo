from django.contrib import admin
from. models import Catalog


@admin.register(Catalog)
class CatalogAdmin(admin.ModelAdmin):
    pass

