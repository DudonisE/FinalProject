from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
import user.views as views


urlpatterns = [
    path("register/", views.register, name="register"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name="logout"),
    path("profile", views.profile, name="users-profile"),
    path('password-change/', views.ChangePasswordView.as_view(), name='password_change'),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('contactus/', views.contact_us, name='contact_us')
]

urlpatterns = format_suffix_patterns(urlpatterns)
