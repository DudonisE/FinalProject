from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from store import views

urlpatterns = [
    path('', views.index, name='index'),
    path('product/', views.ProductList.as_view()),
    path('product/<int:pk>/', views.ProductDetail.as_view()),
    path('aboutus/', views.about_us, name='about_us'),
    path('products/<str:gender>/', views.products_by_gender, name='product_by_gender'),
    path('products/<str:gender>/<str:category_name>/', views.products_by_category, name='product_by_category'),
    path('<str:gender>/<int:pk>/', views.one_product, name='product-view'),
    path('search', views.search_feature, name='search-view'),
    path('cart/', views.view_cart, name='view_cart'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/update/<int:item_id>/', views.update_cart_item, name='update_cart_item'),
    path('checkout/', views.checkout, name='checkout'),
    path('purchase/<int:purchase_id>/', views.purchase, name='purchase'),
    path('order/', views.place_order, name='create_order'),
    path('order/success/', views.order_success, name='order_success'),
    path('review/delete/<int:review_id>/', views.delete_review, name='delete_review'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
