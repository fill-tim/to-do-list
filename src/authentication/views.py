from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

from .forms import LoginUserForm, RegisterUserForm


# Create your views here.
class LoginUser(LoginView):
    """
    Авторизация пользователя
    """
    form_class = LoginUserForm
    template_name = 'authentication/login.html'

    def get_success_url(self):
        return reverse_lazy('notes')


class RegisterUser(generic.CreateView):
    """
    Регистрация пользователя
    """
    form_class = RegisterUserForm
    template_name = 'authentication/register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('notes')


def logout_user(request):
    """
    Выход из аккаунта пользователя
    """
    logout(request)
    return redirect('notes')