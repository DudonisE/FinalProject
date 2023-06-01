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


@login_required
def profile(request):
    if request.user.is_authenticated():
        return render(request, 'users/profile.html')


@login_required
def profile(request):
    user = request.user
    if request.method == "POST":
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if p_form.is_valid() :
            p_form.save()
    else:
        p_form = ProfileUpdateForm(instance=request.user)
    if request.method == "POST":
        u_form = UpdateUserForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
    else:
        u_form = UpdateUserForm(instance=request.user)
    if request.method == "POST":
        m_form = BodyMeasurementsForm(request.POST)
        if m_form.is_valid():
            measurements = m_form.save(commit=False)
            if measurements.user is None:
                measurements.user = request.user
            measurements.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect(to='users-profile')
    else:
        m_form = BodyMeasurementsForm()

    # context = {
    #     'u_form': u_form,
    #     'p_form': p_form,
    #     'm_form': m_form,
    # }
    return render(request, 'users/profile.html', {
        'u_form': u_form,
        'p_form': p_form,
        'm_form': m_form,
    })


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