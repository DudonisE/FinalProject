from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from rest_framework import generics
from django.contrib.auth.models import User
from .forms import RegisterForm, ProfileUpdateForm, UpdateUserForm, BodyMeasurementsForm
from django.contrib.auth.decorators import login_required

from .models import BodyMeasurements
from .serializers import UserSerializer


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect("/")
    else:
        form = RegisterForm()
    return render(request, "users/register.html", {"form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("/")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="users/login.html", context={"login_form": form})


def logout_request(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect("/")


'''
@login_required
def update_profile(request):
    if request.method == "POST":
        u_form = UpdateUserForm(request.POST or None, instance=request.user)
        p_form = ProfileUpdateForm(request.POST or None, request.FILES, instance=request.user.profile)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return render(request, 'users/profile.html')
        elif p_form.is_valid():
            p_form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return render(request, 'users/profile.html')
    else:
        u_form = UpdateUserForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    return render(request, 'users/profile.html', {
        'u_form': u_form,
        'p_form': p_form,
    })


@login_required
def add_body_measurements(request):
    if request.method == "POST":
        m_form = BodyMeasurementsForm(request.POST, instance=request.user.profile)
        if m_form.is_valid():
            m_form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return render(request, 'users/profile.html')
    else:
        m_form = BodyMeasurementsForm(instance=request.user)
    return render(request, 'users/profile.html', {'m_form': m_form})
'''


@login_required
def profile(request):

    user = request.user.id
    bm = BodyMeasurements.objects.get(user_id=user)

    if request.method == "POST":
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        u_form = UpdateUserForm(request.POST, instance=request.user)
        m_form = BodyMeasurementsForm(request.POST, request.FILES, instance=bm)

        if p_form.is_valid():
            p_form.save()
        if u_form.is_valid():
            u_form.save()
        if m_form.is_valid():
            m_form.save()

        messages.success(request, 'Your profile was successfully updated!')
    else:
        try:
            p_form = ProfileUpdateForm(instance=request.user)
            u_form = UpdateUserForm(instance=request.user)
            measures = BodyMeasurements.objects.get(user_id=user)
            m_form = BodyMeasurementsForm(instance=measures)
        except BodyMeasurements.DoesNotExist:
            m_form = BodyMeasurementsForm()
            p_form = ProfileUpdateForm(instance=request.user)
            u_form = UpdateUserForm(instance=request.user)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'm_form': m_form,
    }

    return render(request, 'users/profile.html', context=context)


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'users/change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('users-profile')


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
