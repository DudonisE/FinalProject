from django.urls import path
from user.views import MyProfile


urlpatterns = [
    path('profile/', MyProfile.as_view())
]