from django.contrib import admin

from catalog.models import Categories, Products


# Register your models here.

# admin.site.register(Products)
# admin.site.register(Categories)
@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "category", "price")
    list_filter = ("category", "price",)
    search_fields = ("name", "description",)


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ("id", "category", "description")
    list_filter = ("category", "id",)
    search_fields = ("category", "description",)
