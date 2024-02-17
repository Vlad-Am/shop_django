from django.urls import path

from catalog.views import contacts, product, product_details

urlpatterns = [
    path('', product),
    path('product/<int:pk>/', product_details, name='product_details'),
    path('contacts/', contacts),
]
