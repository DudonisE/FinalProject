from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from store import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products/<int:pk>/', views.ProductDetail.as_view()),
    path('women_products/<int:pk>/', views.one_product, name='product-view'),
    path('women_products/', views.women_products, name='women-products-view'),
    path('men_products/', views.men_products, name='men-products-view'),
    path('search', views.search_feature, name='search-view'),
    path('cart/', views.show_cart, name='show_cart'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
