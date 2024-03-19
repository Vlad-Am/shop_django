import secrets
import time

from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, \
    PasswordResetCompleteView
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from auth_app.forms import UserRegistrationForm, UserProfileForm, UserForgotPasswordForm, UserSetNewPasswordForm
from auth_app.models import User
from config import settings


class RegisterView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'auth_app/register.html'
    success_url = reverse_lazy('auth_app:login')

    def form_valid(self, form):
        token = secrets.token_hex(16)
        user = form.save()
        user.token = token
        user.is_active = False
        user.save()
        host = self.request.get_host()
        link = f'http://{host}/auth/activate/{token}'
        message = f'''Для активации вашего аккаунта перейдите по ссылке:
                {link}'''
        time.sleep(10)
        send_mail("Верификация почты", message, settings.EMAIL_HOST_USER, [user.email, ])
        return super().form_valid(form)


def confirm_email(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return render(request, 'auth_app/login.html', status=200)


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('auth:profile')

    def get_object(self, queryset=None):
        return self.request.user


class UserResetPasswordView(PasswordResetView):
    """
    Стартовая страница сброса пароля почте
    """
    success_url = reverse_lazy('auth_app:password_reset_done')
    template_name = "registration/password_reset_.html"


class UserPasswordResetConfirmView(PasswordResetConfirmView):
    """
    Представление установки нового пароля(страница на которую переходит пользователь для сброса пароля)
    """
    success_url = reverse_lazy("auth_app:login")
    template_name = "registration/entering_new_password.html"


class UserPasswordResetDoneView(PasswordResetDoneView):
    """
    Представление успешной отправки сообщения на почту
    """
    template_name = 'registration/successful_password_change.html'

