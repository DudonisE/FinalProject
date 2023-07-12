from django import forms
from .models import Purchase, CartItem, Size, ProductReview, RATING_CHOICES


class PurchaseForm(forms.ModelForm):
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
        fields = ['name', 'email', 'postal_code', 'address']

        widgets = {
            'address': forms.Textarea(attrs={'row': 5, 'col': 8}),
        }


class SizeForm(forms.ModelForm):
    class Meta:
        model = Size
        fields = '__all__'


class ProductReviewForm(forms.ModelForm):

    rating = forms.ChoiceField(choices=RATING_CHOICES, widget=forms.RadioSelect())

    class Meta:
        model = ProductReview
        labels = {'content': 'Review', 'rating': 'Rate Product'}
        exclude = ('user', 'date_created', 'product', )
