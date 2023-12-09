from django.urls import path

from notes import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_user, name='register'),
    path('login/', views.login, name='login'),
    path('edit-user/<int:user_id>', views.edit_user, name='edit_user'),
    path('logout/', views.logout_user, name='logout'),
]