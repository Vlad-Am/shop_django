from django.contrib import admin

from catalog.models import Categories, Products, Contacts, Blog


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


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ("name", "phone_number", "message")
    list_filter = ("name", "phone_number",)
    search_fields = ("name", "phone_number",)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "content", "preview", "view_count")
    list_filter = ("title", "view_count",)
    search_fields = ("title", "content",)

