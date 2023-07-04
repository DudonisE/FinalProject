from django import forms
from .models import Purchase, CartItem


class OrderForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ['guest_name', 'guest_email']


class CartItemForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = ['product', 'quantity']


class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Purchase
        exclude = ('paid',)

        widgets = {
            'address': forms.Textarea(attrs={'row': 5, 'col': 8}),
        }
