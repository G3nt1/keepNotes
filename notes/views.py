import markdown
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from notes.forms import CreateUserForm, LoginUserForm, CreateNotes
from notes.models import BigNotes
from django.contrib.auth.decorators import login_required


# Notes

@login_required
def home(request):
    notes = BigNotes.objects.filter(user=request.user)

    return render(request, 'home.html', {'notes': notes})


@login_required
def create_notes(request):
    form = CreateNotes()
    if request.user.is_authenticated:
        if request.method == "POST":
            form = CreateNotes(request.POST)
            if form.is_valid():
                note = form.save(commit=False)
                note.user = request.user
                note.save()
                return redirect('detail_note', note.id)

    return render(request, 'create_notes.html', {'form': form})


def detail_notes(request, note_id):
    note = get_object_or_404(BigNotes, id=note_id)
    notes = BigNotes.objects.filter(user=request.user)
    html = markdown.markdown(note.content, extensions=['markdown.extensions.fenced_code',
                                                       'markdown.extensions.admonition',
                                                       'markdown.extensions.tables',
                                                       'fenced_code',

                                                       ])

    return render(request, 'home.html', {'selected_note': note,
                                         'notes': notes,
                                         'html_text': html})


@login_required
def edit_notes(request, notes_id):
    notes = get_object_or_404(BigNotes, id=notes_id)
    if request.method == 'POST':
        form = CreateNotes(request.POST, instance=notes)
        if form.is_valid():
            form.save()
            return redirect('detail_note', notes.id)
    else:
        form = CreateNotes(instance=notes)
    return render(request, 'edit_notes.html', {'form': form})


@login_required
def delete_notes(request, notes_id):
    notes = get_object_or_404(BigNotes, id=notes_id)
    if request.method == 'POST':
        notes.delete()
        return redirect('home')
    return render(request, 'delete_notes.html', {'notes': notes})


# Users
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


def login_user(request):
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
            if user:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, "Invalid email or password")
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
