from django.contrib import admin
from hello.models import Company, Products


class CompanyAdmin(admin.ModelAdmin):
    """
    CompanyAdmin
        This will show all mentioned company
        fields on the admin panel.
    """

    fields = ["name", "company_id", "location"]


class ProductsAdmin(admin.ModelAdmin):
    """
    ProductsAdmin
        This will show all mentioned products
        fields on the admin panel.
    """

    fields = ["company", "product_id", "name"]


admin.site.register(Company, CompanyAdmin)
admin.site.register(Products, ProductsAdmin)
