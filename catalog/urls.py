from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import (ProductListView, ProductsDetailView, ContactsCreateView, BlogCreateView,
                           BlogDeleteView, BlogListView, BlogDetailView, BlogUpdateView)

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='products_list'),
    # path('contacts/', ContactsView.as_view(), name='contacts'),
    path('view/<int:pk>/', ProductsDetailView.as_view(), name='view_product'),
    path('contacts/', ContactsCreateView.as_view(), name='contacts'),
    path('blog/', BlogListView.as_view(), name='blogs_list'),
    path('blog/view_blog/<slug:the_slug>/', BlogDetailView.as_view(), name='view_blog'),
    path('delete_blog/<slug:the_slug>/', BlogDeleteView.as_view(), name='delete_blog'),
    path('update_blog/<slug:the_slug>/', BlogUpdateView.as_view(), name='update_blog'),
    path('create_blog/', BlogCreateView.as_view(), name='create_blog')
    ]
