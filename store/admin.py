from django.contrib import admin

from store.models import Size, Category, Product, Purchase, CartItem, Cart

admin.site.register(Size)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Purchase)
admin.site.register(Cart)
admin.site.register(CartItem)
