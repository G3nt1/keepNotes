from django.contrib.auth import authenticate, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

from notes.forms import CreateUserForm, LoginUserForm, CreateNotes
from notes.models import BigNotes


def home(request):
    notes = BigNotes.objects.all().order_by('-created_at')

    return render(request, 'home.html', {'notes': notes})


 # if request.method == "POST":
 #        form = CreateNotes(request.POST)
 #        if form.is_valid():
 #            form.save()
 #            return redirect('home')
 #    else:
 #        form = CreateNotes()


def register_user(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = form.cleaned_data['email']
            user.save()
            return redirect('login')
    else:
        form = CreateUserForm()
    return render(request, 'users/register.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            return redirect('home')
    else:
        form = LoginUserForm()

    return render(request, 'users/login.html', {'form': form})


def edit_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        form = CreateUserForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = form.cleaned_data['email']
            user.save()

            return redirect('home')
    else:
        form = CreateUserForm(instance=user)
    return render(request, 'users/edit_user.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('login')
