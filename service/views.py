from django.shortcuts import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import generic
from django.views.generic.edit import FormMixin
from service.models import Order, Service
from .forms import OrderReviewForm

"""
Views for service orders.
"""


class MyOrderListView(generic.ListView, LoginRequiredMixin):
    model = Order
    context_object_name = 'orders'
    template_name = 'orders.html'
    # paginate_by = 10

    def get_queryset(self):
        """sita pridejau tada rodo superuser visus orderius, bet neleidzia jam ju per puslapi update arba istrinti."""
        if self.request.user.is_superuser:
            return Order.objects.all()
        else:
            return Order.objects.filter(user=self.request.user)


class OrderDetailView(FormMixin, generic.DetailView):
    model = Order
    template_name = 'order.html'
    form_class = OrderReviewForm

    def get_success_url(self):
        return reverse('book-detail', kwargs={'pk': self.object.id})


    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


    def form_valid(self, form):
        form.instance.order = self.object
        form.instance.user = self.request.user
        form.save()
        return super(OrderDetailView, self).form_valid(form)


class OrderCreateView(generic.CreateView, LoginRequiredMixin):
    model = Order
    fields = ['service', 'quantity']
    success_url = '/orders/'
    template_name = 'order_creation_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        """sita pridejau kad leistu kartu su kainomis issiimti services."""
        context = super().get_context_data(**kwargs)
        context['services'] = Service.objects.all()
        return context


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
