from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import generic

from service.models import Order, Service


class MyOrderListView(generic.ListView, LoginRequiredMixin):
    model = Order
    context_object_name = 'orders'
    template_name = 'orders.html'
    # paginate_by = 10

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


class OrderDetailView(LoginRequiredMixin, generic.DetailView):
    model = Order
    template_name = 'order.html'


class OrderCreateView(generic.CreateView, LoginRequiredMixin):
    model = Order
    # fields = '__all__'
    fields = ['service', 'quantity']
    success_url = '/orders/'
    template_name = 'order_creation_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class OrderUpdateView(generic.UpdateView, LoginRequiredMixin):
    model = Order
    fields = ['service', 'quantity']
    success_url = '/orders/'
    template_name = 'order_creation_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        order = self.get_object()
        return self.request.user == order.user


class OrderDeleteView(generic.DeleteView, LoginRequiredMixin, UserPassesTestMixin):
    model = Order
    success_url = '/orders/'
    template_name = 'order_delete.html'
    # template_name = 'delete_order.html'

    def test_func(self):
        order = self.get_object()
        return self.request.user == order.user


class ServiceListView(generic.ListView, UserPassesTestMixin, LoginRequiredMixin):
    model = Service
    context_object_name = 'services'
    template_name = 'services.html'
    # paginate_by = 10

    def get_queryset(self):
        return Service.objects.all()


class ServiceDetailView(generic.DetailView, LoginRequiredMixin):
    model = Service
    template_name = 'service.html'


class ServiceCreateView(generic.CreateView,LoginRequiredMixin):
    model = Service
    fields = ['title', 'price']
    success_url = '/services/'
    template_name = 'service_creation_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user.is_superuser
        return super().form_valid(form)


class ServiceUpdateView(generic.UpdateView, LoginRequiredMixin):
    model = Service
    fields = ['title', 'price']
    success_url = '/services/'
    template_name = 'service_creation_form.html'

    def form_valid(self, form):
        return super().form_valid(form)

    def test_func(self):
        order = self.get_object()
        return self.request.user.is_superuser


class ServiceDeleteView(generic.DeleteView, LoginRequiredMixin, UserPassesTestMixin):
    model = Service
    success_url = '/services/'
    template_name = 'service_delete.html'

    def test_func(self):
        order = self.get_object()
        return self.request.user == order.user


