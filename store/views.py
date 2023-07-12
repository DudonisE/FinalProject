from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import generics
from rest_framework import permissions
from django.db.models import Q, Avg

from store.cart import get_cart_from_session
from store.forms import CheckoutForm, PurchaseForm, ProductReviewForm
from store.models import Product, Category, Size, Cart, CartItem, Purchase, ProductReview
from store.permissions import IsOwnerOrReadOnly
from store.serializers import ProductSerializer
from django.core.paginator import Paginator

"""
Views for products display and adding to cart.
"""


def index(request):
    context = {
        'women_category': Category.objects.filter(gender='Woman'),
        'men_category': Category.objects.filter(gender='Men'),
    }
    return render(request, "index.html", context)


def products_by_gender(request, gender):
    products = Product.objects.filter(category_name__gender=gender)
    """
    Get the pages for products with Paginator
    """
    paginator = Paginator(products, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'store/products_by_gender.html', {'products': page_obj, 'gender': gender})


def products_by_category(request, gender, category_name):
    products = Product.objects.filter(category_name__gender=gender, category_name__category_name=category_name)
    """
    Get the pages for products with Paginator
    """
    paginator = Paginator(products, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'store/products_by_categorys.html', {'products': page_obj, 'gender': gender, 'category_name': category_name})


def one_product(request, gender, pk):
    product = get_object_or_404(Product, category_name__gender=gender, id=pk)
    sizes = product.size.all()
    average_rating = ProductReview.objects.filter(product=product).aggregate(Avg('rating'))['rating__avg']
    form = ProductReviewForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()
            return redirect('product-view', gender=gender, pk=pk)
    reviews = ProductReview.objects.filter(product=product)
    context = {
        'product': product,
        'sizes': sizes,
        'form': form,
        'average_rating': average_rating,
        'reviews': reviews,
    }
    return render(request, 'store/product.html', context)


def delete_review(request, review_id):
    review = get_object_or_404(ProductReview, id=review_id)
    if request.user == review.user:  # Only allow the review owner to delete the review
        product_id = review.product.id
        gender = review.product.category_name.all().first().gender
        review.delete()
        return redirect('product-view', gender=gender, pk=product_id)


def search_feature(request):
    if request.method == 'GET':
        search_query = request.GET.get('q')
        products = Product.objects.filter(Q(name__icontains=search_query))
        return render(request, 'store/search.html', {'products': products})
    return render(request, 'store/search.html', {})


def view_cart(request):
    cart = Cart.objects.get(user=request.user)
    cart_items = cart.cart_items.all()
    total_cost = sum(item.total_cost() for item in cart_items)
    return render(request, 'store/cart.html', {'cart_items': cart_items, 'total_cost': total_cost})

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def add_to_cart(request, product_id):
    if request.method == 'POST':
        product = Product.objects.get(pk=product_id)
        size_ids = request.POST.getlist('size_id')
        sizes = Size.objects.filter(pk__in=size_ids)
        cart, created = Cart.objects.get_or_create(user=request.user)
        quantity = int(request.POST.get('quantity', 1))
        for size in sizes:
            cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product, size=size)
            if created:
                cart_item.quantity = quantity
            else:
                cart_item.quantity += quantity
            cart_item.save()
        return redirect('view_cart')
    return redirect('view_cart')
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def remove_from_cart(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.delete()
    return redirect('view_cart')


def update_cart_item(request, item_id):
    if request.method == 'POST':
        cart_item = CartItem.objects.get(id=item_id)
        quantity = int(request.POST.get('quantity', 0))
        if quantity > 0:
            cart_item.quantity = quantity
            cart_item.save()
        else:
            cart_item.delete()
    return redirect('view_cart')


@login_required
def checkout(request):
    cart = Cart.objects.get(user=request.user)
    cart_items = cart.cart_items.all()
    total_cost = sum(item.total_cost() for item in cart_items)

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        postal_code = request.POST['postal_code']
        address = request.POST['address']

        purchase = Purchase.objects.create(user=request.user, cart=cart, name=name, email=email,
                                           postal_code=postal_code, address=address, total_price=total_cost)
        cart_items.delete()
        cart.delete()
        return redirect('purchase', purchase_id=purchase.id)
    form = CheckoutForm()

    return render(request, 'store/checkout.html', {'cart_items': cart_items, 'total_cost': total_cost, 'form': form})


def purchase(request, purchase_id):
    purchase = Purchase.objects.get(id=purchase_id)
    return render(request, 'store/purchase.html', {'purchase': purchase})


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


"""
REST framework code to see product list or only one product by entering ID.
"""


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
