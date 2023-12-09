from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from notes.models import BigNotes


class CreateNotes(forms.ModelForm):
    class Meta:
        model = BigNotes
        fields = ('title', 'content')

    def save_notes(self):
        # This method saves the form data to the database using the associated model
        if self.is_valid():
            return BigNotes.objects.create(
                title=self.cleaned_data['title'],
                content=self.cleaned_data['content']
            )
        return None


class CreateUserForm(UserCreationForm):
    first_name = forms.CharField(max_length=200, required=True)
    last_name = forms.CharField(max_length=200, required=True)
    email = forms.EmailField(max_length=255, required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')


class LoginUserForm(forms.Form):
    email = forms.EmailField(max_length=255, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    def save(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        return email, password
