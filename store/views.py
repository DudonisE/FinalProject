from django.views import generic

from store import cart
from django.shortcuts import render, get_object_or_404, redirect
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
    return render(request, 'index.html')


def products_by_gender(request, gender):
    products = Product.objects.filter(category_name__gender=gender)
    return render(request, 'store/products_by_gender.html', {'products': products, 'gender': gender})


def products_by_category(request, gender, category_name):
    products = Product.objects.filter(category_name__gender=gender, category_name__category_name=category_name)
    return render(request, 'store/products_by_categorys.html', {'products': products, 'gender': gender, 'category_name': category_name})


def one_product(request, gender, pk):
    product = Product.objects.get(category_name__gender=gender, id=pk)
    return render(request, 'store/product.html', {'product': product})


def search_feature(request):
    if request.method == 'GET':
        search_query = request.GET.get('q')
        products = Product.objects.filter(Q(name__icontains=search_query))
        return render(request, 'store/search.html', {'products': products})
    return render(request, 'store/search.html', {})


# class Products(generic.ListView):
#     model = Product
#     context_object_name = 'all_products'
#     template_name = 'index.html'
#
#     def products_by_gender(self, *args, **kwargs):
#         category = Category.objects.get(gender=self.kwargs['gender'])
#         product = Product.objects.filter(category=category)
#         context = {
#             'product_list': product,
#             'category_title': category,
#         }
#         return render(self.request, "category.html", context)


# def products_by_gender(request, gender):
#     products = Product.objects.filter(category_name__gender=gender)
#     return render(request, "store/products_by_gender.html", {'products': products, 'gender': gender})

    # categorys = Product.objects.filter(category_name=category_name)
    # product = get_object_or_404(Product, id=id)
# def men_products(request):
#     context = {
#         'men_items': Product.objects.filter(category_name__gender='Man'),
#         'men_category': Category.objects.filter(gender='Man'),
#     }
#     return render(request, "store/men_products.html", context)


# def category_list(request, category_name):
#     category = Category.objects.filter(gender='Woman')
#     woman_category = get_object_or_404(category, category_name=category_name)
#     context = {'products': Product.objects.filter(category_name=woman_category)}
#     return render(request, "store/products_by_gender.html", context)


# def one_product(request, gender, pk):
#     product = get_object_or_404(Product, category_name__gender=gender, id=pk)
    # if request.method == 'POST':
    #     form = CartForm(request, request.POST)
    #     if form.is_valid():
    #         request.form_data = form.cleaned_data
    #         cart.add_item_to_cart(request)
    #         return redirect('show_cart')
    #
    # form = CartForm(request, initial={'product_id': product.id})
    # return render(request, 'store/product.html', {'product': product})

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

# < form
# action = "{% url 'product-view' %}"
# method = "post" >
# { % csrf_token %}
# {{form}}
# < input
# type = "submit"
# value = "Add to cart"
#
#
# class ="btn btn-primary" >
#
# < / form >