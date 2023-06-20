from django.contrib import admin

from store.models import Size, Category, Product, Order, CartItem


admin.site.register(Size)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(CartItem)
