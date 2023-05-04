from django.contrib import admin

from store.models import Size, Category, Product


admin.site.register(Size)
admin.site.register(Category)
admin.site.register(Product)