from django import forms
from .models import Work
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class UserLoginForm(AuthenticationForm):
    # Формируем поля
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'uk-input',
            'id': 'username',
            'placeholder': 'Имя пользователя',
            'minlength': 5
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'uk-input',
            'id': 'pass',
            'placeholder': 'Пароль',
            'minlength': 5
        }
    ))


class UserRegisterForm(UserCreationForm):
    # Формируем поля
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'uk-input',
            'id': 'username',
            'placeholder': 'Имя пользователя',
            'minlength': 5
        }
    ))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'class': 'uk-input',
            'id': 'email',
            'placeholder': 'E-mail'
        }
    ))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'uk-input',
            'id': 'pass',
            'placeholder': 'Пароль',
            'minlength': 5
        }
    ))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'uk-input',
            'id': 'passConfirm',
            'placeholder': 'Потвердите пароль',
            'minlength': 5
        }
    ))

    class Meta:
        # С какой таблицей работаем
        model = User
        # Какие поля нам нужны
        fields = ('username', 'email', 'password1', 'password2')


class WorkForm(forms.ModelForm):
    class Meta:
        # С какой таблицей работаем
        model = Work
        # Какие поля нам нужны
        fields = ['full_name', 'completed_works']
        # Формируем поля
        widgets = {
            'full_name': forms.TextInput(
                attrs={
                    'class': 'uk-input',
                    'id': 'full_name',
                    'placeholder': 'ФИО'
                }
            ),
            'completed_works': forms.Textarea(
                attrs={
                    'class': 'uk-textarea',
                    'id': 'completed_works',
                    'placeholder': 'Выполненные работы'
                }
            ),
        }
