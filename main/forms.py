from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import Note


class NoteEditForm(forms.ModelForm):
    """
    Форма для редактирования заметки
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs[
            'style'] = 'width:400px; height:40px; border-radius: 10px; border: 1px solid #8C4162; background: #F5C5DF'
        self.fields['description'].widget.attrs[
            'style'] = 'width:300px; height:100px; border: 1px solid #8C4162; border-radius: 10px;  background: #F5C5DF'
        self.fields['importance'].widget.attrs[
            'style'] = 'border-radius: 10px; border: 1px solid #8C4162;  background: #F5C5DF'

    class Meta:
        model = Note
        exclude = ['autor']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form', }),
            'description': forms.Textarea(attrs={'class': 'form ', }),
        }


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