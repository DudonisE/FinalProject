from django.urls import path
import user.views as views



urlpatterns = [
    path("register/", views.register, name="register"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name="logout"),
    path("profile", views.profile, name="users-profile"),
    path('password-change/', views.ChangePasswordView.as_view(), name='password_change'),
]
