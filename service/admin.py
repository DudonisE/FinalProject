from django.contrib import admin
from service.models import Order, Service, OrderReview

admin.site.register(Service)
admin.site.register(Order)
admin.site.register(OrderReview)
