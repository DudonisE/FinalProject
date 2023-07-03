from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from service.models import Order, OrderReview


class OrderReviewForm(forms.ModelForm):
    class Meta:
        model = OrderReview
        fields = ('content', 'order', 'user',)
        widgets = {'order': forms.HiddenInput(), 'user': forms.HiddenInput()}
