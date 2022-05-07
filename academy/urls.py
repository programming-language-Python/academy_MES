from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.user_login, name='login'),
    path('about_the_course/', views.about_the_course, name='about_the_course'),
    path('training/', views.training, name='training'),
    path('author/', views.author, name='author'),
]
