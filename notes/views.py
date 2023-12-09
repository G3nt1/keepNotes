from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from notes.forms import CreateUserForm, LoginUserForm


# def home(request):
#     return request(render, 'home.html')

def register_user(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = form.cleaned_data['f_name' + 'l_name']
            user.save()
            return redirect('Login')
    else:
        form = CreateUserForm()
    return render(request, 'register.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=email, password=password)
            return redirect('home')
    else:
        form = LoginUserForm()

    return render(request, 'login.html', {'form':form})