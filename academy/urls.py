from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', register, name='register'),
    path('work/', ViewWork.as_view(), name='view_work'),
    path('work/add-work/', add_work, name='add_work'),
    path('content/', content, name='content'),
    path('about_the_course/', about_the_course, name='about_the_course'),
    path('training/', training, name='training'),
    path('author/', author, name='author'),
    path('lecture/', lecture, name='lecture'),
    path('workshops/', workshops, name='workshops'),
    path('video_footage/', video_footage, name='video_footage'),
    path('testing/', testing, name='testing'),

    path(
        "robots.txt",
        TemplateView.as_view(template_name="academy/robots.txt", content_type="text/plain"),
    ),
]
