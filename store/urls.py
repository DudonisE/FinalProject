from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from store import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products/<str:gender>/', views.products_by_gender, name='product_by_gender'),
    path('products/<str:gender>/<str:category_name>/', views.products_by_category, name='product_by_category'),
    path('products/<int:pk>/', views.one_product, name='product-view'),
    path('search', views.search_feature, name='search-view'),
    path('cart', views.show_cart, name='show_cart'),
]

urlpatterns = format_suffix_patterns(urlpatterns)