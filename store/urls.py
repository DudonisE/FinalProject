from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from store import views

urlpatterns = [
    path('snippets/<int:pk>/', views.ProductDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)