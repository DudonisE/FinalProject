from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import BadHeaderError, send_mail
from django.db.models import Q
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm
from .forms import RegisterForm



def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect("/home")
    else:
        form = RegisterForm()
    return render(response, "users/register.html", {"form": form})

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
    messages.info(request, "You have successfully logged out.")
    return redirect("/")


def password_reset(request):
    form = PasswordResetForm(request.POST)
    return render(request=request, template_name="users/password_reset.html", context={"form": form})
    # if request.method == "POST":
    #     domain = request.headers['Host']
    #     password_reset_form = PasswordResetForm(request.POST)
    #     if password_reset_form.is_valid():
    #         data = password_reset_form.cleaned_data['email']
    #         associated_users = User.objects.filter(Q(email=data))
    #         # You can use more than one way like this for resetting the password.
    #         # ...filter(Q(email=data) | Q(username=data))
    #         # but with this you may need to change the password_reset form as well.
    #         if associated_users.exists():
    #             for user in associated_users:
    #                 subject = "Password Reset Requested"
    #                 email_template_name = "admin/accounts/password/password_reset_email.txt"
    #                 c = {
    #                     "email": user.email,
    #                     'domain': domain,
    #                     'site_name': 'Interface',
    #                     "uid": urlsafe_base64_encode(force_bytes(user.pk)),
    #                     "user": user,
    #                     'token': default_token_generator.make_token(user),
    #                     'protocol': 'http',
    #                 }
    #                 email = render_to_string(email_template_name, c)
    #                 try:
    #                     send_mail(subject, email, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)
    #                 except BadHeaderError:
    #                     return HttpResponse('Invalid header found.')
    #                 return redirect("/core/password_reset/done/")
    # password_reset_form = PasswordResetForm()
    # return render(request=request, template_name="users/password_reset.html",
    #               context={"password_reset_form": password_reset_form})
