from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# models
from users.models import User

class UserCreateForm(UserCreationForm):
    password1 = forms.CharField(label='password',
        widget=forms.PasswordInput(attrs={'placeholder': 'password'}))
    password2 = forms.CharField(label='password confirmation',
        widget=forms.PasswordInput(attrs={'placeholder': 'confirm password'}))

    class Meta:
        model = User
        fields = ('username', 'email',)
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'placeholder': 'email'}),
        }


class UserUpdateForm(UserChangeForm):

    class Meta:
        model = User
        fields = (
            'password',
            'username',
            'first_name',
            'last_name',
            'email',
            'birthday',
            'photo',)

        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'email'}),
            'birthday': forms.DateInput(
                attrs={'placeholder': 'birthday', 'type': 'date'},
                format='%Y-%m-%d'),
            # 'photo': forms.FileInput(attrs={'accept': 'image/*'}),
        }
