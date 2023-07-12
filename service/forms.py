from django import forms
from service.models import OrderReview


class OrderReviewForm(forms.ModelForm):
    class Meta:
        model = OrderReview
        fields = ('content', 'order', 'user',)
        widgets = {'order': forms.HiddenInput(), 'user': forms.HiddenInput()}
