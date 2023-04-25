from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from user.models import BodyMeasurements


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class BodyMeasurementsForm(forms.ModelForm):
    class Meta:
        model = BodyMeasurements
        exclude = ('last_updated',)


# class PasswordResetForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['email']
#