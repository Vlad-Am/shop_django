from django.urls import path

from catalog.views import body, contacts

urlpatterns = [
    path('', body),
    path('contacts/', contacts),
]
