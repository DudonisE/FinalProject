from django.urls import path
from . import views


urlpatterns = [
    path('orders/', views.MyOrderListView.as_view(), name='orders'),
    path('orders/<int:pk>', views.OrderDetailView.as_view(), name='my-order'),
    path('orders/new/', views.OrderCreateView.as_view(), name='new-order'),
    path('orders/<int:pk>/delete', views.OrderDeleteView.as_view(), name='order-delete'),
    path('orders/<int:pk>/update', views.OrderUpdateView.as_view(), name='order-update'),

    path('services/', views.ServiceListView.as_view(), name='services'),
    path('services/<int:pk>', views.ServiceDetailView.as_view(), name='my-service'),
    path('services/new/', views.ServiceCreateView.as_view(), name='new-service'),
    path('services/<int:pk>/delete', views.ServiceDeleteView.as_view(), name='service-delete'),
    path('services/<int:pk>/update', views.ServiceUpdateView.as_view(), name='service-update'),
]
