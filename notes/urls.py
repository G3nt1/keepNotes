from django.urls import path
from django.views.generic import detail

from notes import views

urlpatterns = [
    path('', views.home, name='home'),
    path('notes/<int:note_id>/', views.detail_notes, name='detail_note'),
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('edit-user/<int:user_id>', views.edit_user, name='edit_user'),
    path('logout/', views.logout_user, name='logout'),

    path('create-notes', views.create_notes, name='create_notes'),
    path('edit-note/<int:notes_id>', views.edit_notes, name='edit_notes'),
    path('delete_notes/<int:notes_id>', views.delete_notes, name='delete_notes'),

]
