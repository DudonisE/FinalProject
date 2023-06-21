from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from service.models import Order, OrderReview


# class ServiceForm(forms.ModelForm):
#     class Meta:
#         model = Order
#         # fields = '__all__'
#         exclude = ('user',)
