from django.db import models
# для перевода
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.urls import reverse


# Таблица
class Work(models.Model):
    # Её столбцы

    # ФИО
    full_name = models.CharField(max_length=150, verbose_name='ФИО')

    # Дни недели
    # Формируем выпадающий список
    class DaysOfTheWeek(models.TextChoices):
        monday = 'Пн', _('Понедельник')
        tuesday = 'Вт', _('Вторник')
        wednesday = 'Ср', _('Среда')
        thursday = 'Чт', _('Четверг')
        friday = 'Пт', _('Пятница')
        saturday = 'Сб', _('Суббота')
        sunday = 'Вс', _('Воскресенье')

    days_of_the_week = models.CharField(
        max_length=2, choices=DaysOfTheWeek.choices, default=DaysOfTheWeek.monday, )

    # Выполненные работы
    completed_works = models.TextField(verbose_name='Выполненные работы')

    class Assessment(models.TextChoices):
        excellent = '5', _('Отлично')
        good = '4', _('Хорошо')
        satisfactorily = '3', _('Удовлетворительно')
        not_rented = '2', _('Не сдано')
        nope = '1', _('Нет')

    assessment = models.CharField(
        max_length=1, choices=Assessment.choices, default=Assessment.nope, )

    # Внешний ключ. Связь один ко многим. Один пользователь может иметь несколько задач.
    # models.CASCADE:
    # автоматически удаляет строку из зависимой таблицы,
    # если удаляется связанная строка из главной таблицы
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')

    def __str__(self):
        return str(self.id)

    # для перехода на аккаунт студента
    def get_absolute_url(self):
        return reverse('view_work', kwargs={"user": self.user})

    # настройка для отображения в админке
    class Meta:
        # в единственном числе
        verbose_name = 'Работу'
        # во множественном числе
        verbose_name_plural = 'Работы'
        # как будет сортироваться данные
        ordering = ['full_name']
