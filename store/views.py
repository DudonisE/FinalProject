from django.views import generic

from store import cart
from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import generics
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.db.models import Q

from store.cart import get_cart_from_session
from store.forms import PurchaseForm, CartItemForm
from store.models import Product, Category, Size, Cart, CartItem, Purchase
from store.permissions import IsOwnerOrReadOnly
from store.serializers import ProductSerializer
from django.core.paginator import Paginator


def index(request):

    context = {
        'women_category': Category.objects.filter(gender='Woman'),
        'men_category': Category.objects.filter(gender='Men'),
    }
    # all_products = Product.objects.all()
    # return render(request, "index.html", {'all_products': all_products})
    return render(request, "index.html", context)


def products_by_gender(request, gender):
    products = Product.objects.filter(category_name__gender=gender)
    paginator = Paginator(products, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'store/products_by_gender.html', {'products': page_obj, 'gender': gender})


def products_by_category(request, gender, category_name):
    products = Product.objects.filter(category_name__gender=gender, category_name__category_name=category_name)
    paginator = Paginator(products, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'store/products_by_categorys.html', {'products': page_obj, 'gender': gender, 'category_name': category_name})


def one_product(request, gender, pk):
    product = Product.objects.get(category_name__gender=gender, id=pk)
    sizes = product.size.all()
    return render(request, 'store/product.html', {'product': product, 'sizes': sizes})


def search_feature(request):
    if request.method == 'GET':
        search_query = request.GET.get('q')
        products = Product.objects.filter(Q(name__icontains=search_query))
        return render(request, 'store/search.html', {'products': products})
    return render(request, 'store/search.html', {})


def view_cart(request):
    cart = get_cart_from_session(request)
    cart_items = cart.cartitem_set.all()
    return render(request, 'cart.html', {'cart': cart, 'cart_items': cart_items})

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    user = request.user

    # Check if the user is authenticated or a guest
    if user.is_authenticated:
        # If the user is authenticated, check if they have a cart
        cart, created = Cart.objects.get_or_create(user=user)
    else:
        # If the user is a guest, check if they have a session
        session_id = request.session.session_key
        cart, created = Cart.objects.get_or_create(session_id=session_id)

    # Check if the product is already in the cart
    cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)

    # If the product is already in the cart, increase the quantity
    if not item_created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart')  # Redirect to the cart page after adding the product
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def remove_from_cart(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.delete()
    return redirect('view_cart')


def update_cart_item(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    if request.method == 'POST':
        form = CartItemForm(request.POST, instance=cart_item)
        if form.is_valid():
            form.save()
            return redirect('view_cart')
    else:
        form = CartItemForm(instance=cart_item)
    return render(request, 'update_cart_item.html', {'form': form, 'cart_item': cart_item})


def place_order(request):
    cart = get_cart_from_session(request)

    if request.method == 'POST':
        order_form = PurchaseForm(request.POST)

        if order_form.is_valid():
            order = order_form.save(commit=False)
            order.cart = cart
            order.save()

            # Clear the cart or perform any additional actions

            return redirect('order_success')
    else:
        order_form = PurchaseForm()

    context = {'order_form': order_form, 'cart': cart}
    return render(request, 'place_order.html', context)


def order_success(request):
    return render(request, 'order_success.html')


def about_us(request):
    return render(request, "about_us.html")


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