from django.contrib import admin

from catalog.models import Categories, Products

# Register your models here.

admin.site.register(Products)
admin.site.register(Categories)
