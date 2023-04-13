from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class RegisterUserForm(UserCreationForm):
    """
    Форма для регистрации пользователя
    """
    username = forms.CharField(label='Логин',
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control border-dark', }))
    email = forms.CharField(label='Почта',
                            widget=forms.EmailInput(
                                attrs={'class': 'form-control border-dark', }))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs={'class': 'form-control border-dark', }))
    password2 = forms.CharField(label='Повторный пароль', widget=forms.PasswordInput(
        attrs={'class': 'form-control border-dark', }))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginUserForm(AuthenticationForm):
    """
    Форма для авторизации пользователя
    """
    username = forms.CharField(label='Логин',
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control border-dark', }))
    password = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput(
                                   attrs={'class': 'form-control border-dark', }))

    class Meta:
        model = User
        fields = ['username', 'password']