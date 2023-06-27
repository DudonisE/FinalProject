from django.contrib import admin
from service.models import Order, Service, OrderReview


class OrderReviewAdmin(admin.ModelAdmin):
    list_display = ('order', 'date_created', 'user', 'content')


admin.site.register(Service)
admin.site.register(Order)
admin.site.register(OrderReview, OrderReviewAdmin)
