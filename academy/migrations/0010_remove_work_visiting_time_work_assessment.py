# Generated by Django 4.0.4 on 2022-05-24 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0009_remove_work_completed_works_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='work',
            name='visiting_time',
        ),
        migrations.AddField(
            model_name='work',
            name='assessment',
            field=models.CharField(choices=[('5', 'Отлично'), ('4', 'Хорошо'), ('3', 'Удовлетворительно'), ('2', 'Не сдано'), ('1', 'Нет')], default='1', max_length=1),
        ),
    ]
