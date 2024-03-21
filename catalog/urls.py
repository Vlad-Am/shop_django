from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import (ProductsListView, ProductsDetailView, ContactsCreateView, BlogCreateView,
                           BlogDeleteView, BlogListView, BlogDetailView, BlogUpdateView, ProductsCreateView,
                           ProductsUpdateView, ProductsDeleteView)

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductsListView.as_view(), name='products_list'),
    path('update/<int:pk>/', ProductsUpdateView.as_view(), name='update_product'),
    path('view/<int:pk>/', ProductsDetailView.as_view(), name='view_product'),
    path('create/', ProductsCreateView.as_view(), name='create_product'),
    path('delete/<int:pk>/', ProductsDeleteView.as_view(), name='product_confirm_delete'),


    path('contacts/', ContactsCreateView.as_view(), name='contacts'),


    path('create_blog/', BlogCreateView.as_view(), name='create_blog'),
    path('blog/view_blog/<slug:the_slug>/', BlogDetailView.as_view(), name='view_blog'),
    path('update_blog/<slug:the_slug>/', BlogUpdateView.as_view(), name='update_blog'),
    path('blog/', BlogListView.as_view(), name='blogs_list'),
    path('delete_blog/<slug:the_slug>/', BlogDeleteView.as_view(), name='delete_blog')
    ]
