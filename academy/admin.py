from django.contrib import admin
from .models import Work


# настройка отображения таблицы в админке
class WorkAdmin(admin.ModelAdmin):
    # какие столбцы отображать
    list_display = ('id', 'full_name', 'days_of_the_week', 'completed_works', 'assessment', 'user')
    # какие столбцы будут работать как ссылка для перехода изменения строки
    list_display_links = ('id', 'full_name')
    list_editable = ('assessment',)
    # по каким столбцам можно осуществлять поиск
    search_fields = ('id', 'full_name', 'days_of_the_week', 'completed_works', 'assessment', 'user')
    # столбцы по которым можно сортировать
    list_filter = ('id', 'full_name', 'days_of_the_week', 'completed_works', 'assessment', 'user')
    # добавить ли кнопку сохранить на вверх
    save_on_top = True


# регистрирование настроек для админки
admin.site.register(Work, WorkAdmin)

admin.site.site_title = 'Управление работами'
admin.site.site_header = 'Управление работами'
