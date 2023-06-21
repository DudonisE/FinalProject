from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('orders/', views.MyOrderListView.as_view(), name='orders'),
    path('orders/new/', views.OrderCreateView.as_view(), name='new-order'),
]
