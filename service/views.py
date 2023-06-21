from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from service.models import Order


class MyOrderListView(generic.ListView, LoginRequiredMixin):
    model = Order
    context_object_name = 'orders'
    template_name = 'orders.html'
    # paginate_by = 10

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


class OrderCreateView(generic.CreateView, LoginRequiredMixin):
    model = Order
    # fields = '__all__'
    fields = ['service', 'quantity']
    success_url = "/orders/"
    template_name = 'order_creation_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

# order delete
# new service
# delete service
# update service