from .models import Cart

"""
This function makes sure that a valid Cart object is retrieved
from the session. If an existing cart is found, it is returned. If not, 
a new cart is created and associated with the user's session.
"""


def get_cart_from_session(request):
    cart_id = request.session.get('cart_id')
    cart = None

    if cart_id:
        try:
            cart = Cart.objects.get(id=cart_id)
        except Cart.DoesNotExist:
            pass

    if not cart:
        cart = Cart.objects.create()
        request.session['cart_id'] = cart.id

    return cart
