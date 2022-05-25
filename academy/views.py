from django.shortcuts import render, redirect
from django.views.generic import ListView
from .forms import UserRegisterForm, UserLoginForm, WorkForm
from django.contrib.auth import login, logout
from django.contrib import messages
from .models import Work
from django.contrib.staticfiles.utils import get_files
from django.contrib.staticfiles.storage import StaticFilesStorage


# Create your views here.
def index(request):
    return render(request, 'academy/index.html')


def content(request):
    return render(request, 'academy/content.html')


def about_the_course(request):
    return render(request, 'academy/about_the_course.html')


def training(request):
    return render(request, 'academy/training.html')


def author(request):
    return render(request, 'academy/author.html')


def lecture(request):
    s = StaticFilesStorage()
    lectures = list(get_files(s, location='documents/lecture'))
    is_sidebar = True
    return render(request, 'academy/lecture.html', {
        'lectures': lectures,
        'is_sidebar': is_sidebar,
    })


def workshops(request):
    s = StaticFilesStorage()
    workshops_files = list(get_files(s, location='documents/workshops'))
    is_sidebar = True
    return render(request, 'academy/workshops.html', {
        'workshops': workshops_files,
        'is_sidebar': is_sidebar,
    })


def video_footage(request):
    videos = [
        'https://www.youtube.com/embed/OW9NaY6Dy7w',
        'https://www.youtube.com/embed/ZsN6B2M16S8',
        'https://www.youtube.com/embed/1a2aAeQ_h4Y',
        'https://www.youtube.com/embed/QPWgJWKbwp0',
        'https://www.youtube.com/embed/Kb1CN7cXaVQ',
        'https://www.youtube.com/embed/L5R4JTr58pw',
        'https://www.youtube.com/embed/kOQ1UbnF5CY',
        'https://www.youtube.com/embed/XddIRy_XRHY',
    ]
    is_sidebar = True
    return render(request, 'academy/video_footage.html', {
        'videos': videos,
        'is_sidebar': is_sidebar,
    })


def testing(request):
    s = StaticFilesStorage()
    tests = list(get_files(s, location='documents/testing'))
    is_sidebar = True
    return render(request, 'academy/testing.html', {
        'tests': tests,
        'is_sidebar': is_sidebar,
    })


def register(request):
    # Это POST запрос?
    if request.method == 'POST':
        # Передаём данные POST запроса в класс UserRegisterForm
        form = UserRegisterForm(request.POST)
        # Проверка является ли форма валидной (правильной)
        if form.is_valid():
            # Создание строки в БД
            user = form.save()
            # Залогинили пользователя
            login(request, user)
            # Отправляем сообщение об успешном регистрировании в аминку
            messages.success(request, 'Вы успешно зарегистрировались')
            # Перенаправляем пользователя на главную страницу
            return redirect(index)
        else:
            # Отправляем сообщение об ошибке регистрировании в аминку
            messages.error(request, 'Ошибка регистрации')
    else:
        # Если это не POST запрос, то вызываем класс UserRegisterForm
        # в переменной form будет лежать вся форма
        form = UserRegisterForm()
    # перенаправляем пользователя на странницу регистрации
    # и передаём на эту страницу request (запрос) и переменную form
    return render(request, 'academy/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('view_work')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserLoginForm()
    return render(request, 'academy/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')


# def view_work(request, username):
#     news_item = User.objects.get(username=username)
#     # news_item = get_object_or_404(User, username=username)
#     return render(request, 'academy/view_work.html', {"news_item": news_item})
class ViewWork(ListView):
    model = Work
    context_object_name = 'works'


def add_work(request):
    if request.method == 'POST':
        form = WorkForm(request.POST)
        if form.is_valid():
            # Создание строки в БД
            Work.objects.create(
                **form.cleaned_data,
                user=request.user
            )
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect(add_work)
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = WorkForm()
    return render(request, 'academy/add_work.html', {'form': form})

# class ViewWork(LoginRequiredMixin, CreateView):
#     form_class = workForm
#     template_name = 'academy/work.html'
#     # success_url = reverse_lazy('home')
#     # login_url = '/admin/'
#     raise_exception = True
