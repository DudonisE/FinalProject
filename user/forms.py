from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from user.models import BodyMeasurements, Profile, ContactUs


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class BodyMeasurementsForm(forms.ModelForm):
    class Meta:
        model = BodyMeasurements
        labels = {
            'bust': 'Bust (A)',
            'waist': 'Waist (B)',
            'hips': 'Hips (C)',
            'neck': 'Neck (D)',
            'chest': 'Chest (E)',
            'shoulder': 'Shoulder (F)',
            'sleeve': 'Sleeve (G)',
            'shoulder_to_waist': 'Shoulder to waist (H)',
            'shoulder_to_floor': 'Shoulder to floor (I)',
        }
        exclude = ('user', 'measure_model',)


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar']


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', ]


#TODO
# class PasswordResetForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['email']


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ('full_name', 'email', 'message')



