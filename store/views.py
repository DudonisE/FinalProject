from . import cart
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView
from rest_framework import generics
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.db.models import Q

from store.forms import CartForm
from store.models import Product, Category, Size
from store.permissions import IsOwnerOrReadOnly
from store.serializers import ProductSerializer


def index(request):
    all_products = Product.objects.all()
    return render(request, "index.html", {'all_products': all_products})


def search_feature(request):
    if request.method == 'GET':
        search_query = request.GET.get('q')
        products = Product.objects.filter(Q(name__icontains=search_query))
        return render(request, 'store/search.html', {'products': products})
    return render(request, 'store/search.html', {})


def women_products(request):
    context = {
        'women_items': Product.objects.filter(category_name__gender='Woman'),
        'women_category': Category.objects.filter(gender='Woman'),
    }
    return render(request, "store/women_products.html", context)


def men_products(request):
    context = {
        'men_items': Product.objects.filter(category_name__gender='Man'),
        'men_category': Category.objects.filter(gender='Man'),
    }
    return render(request, "store/men_products.html", context)

# def category_list():
#     return {
#         "category_urls": [
#             {"name": category.name, "url": category.get_absolute_url()}
#             for category in Category.objects.all()
#         ]
#     }


def one_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = CartForm(request, request.POST)
        if form.is_valid():
            request.form_data = form.cleaned_data
            cart.add_item_to_cart(request)
            return redirect('show_cart')

    form = CartForm(request, initial={'product_id': product.id})
    return render(request, 'store/product.html', {
        'product': product,
        'form': form,
    })

    # one_product = get_object_or_404(Product, pk=pk)
    # return render(request, "store/product.html", {'one_product': one_product})


def show_cart(request):

    if request.method == 'POST':
        if request.POST.get('submit') == 'Update':
            cart.update_item(request)
        if request.POST.get('submit') == 'Remove':
            cart.remove_item(request)

    cart_items = cart.get_all_cart_items(request)
    cart_subtotal = cart.subtotal(request)
    return render(request, 'store/cart.html', {
                                            'cart_items': cart_items,
                                            'cart_subtotal': cart_subtotal,
                                            })


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format)
    })
