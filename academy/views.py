from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserLoginForm
from django.contrib.auth import login, logout
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, 'academy/index.html')


def about_the_course(request):
    return render(request, 'academy/about_the_course.html')


def training(request):
    return render(request, 'academy/training.html')


def author(request):
    return render(request, 'academy/author.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('home')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'academy/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('app:home')
    else:
        form = UserLoginForm()
    return render(request, 'academy/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')
