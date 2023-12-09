from django.contrib.auth import views as auth_views
from django.urls import path

from notes import views

urlpatterns = [
    # path('', views.home, name='home')
    path('register/', views.register_user, name='register')
]