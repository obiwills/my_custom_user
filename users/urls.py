# users/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('about/', views.AboutPageView.as_view(), name='about'),
]