# Generated by Django 5.1.3 on 2025-01-24 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0003_vacancyquestion_weekday_remove_vacancy_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vacancy',
            name='title',
        ),
    ]
