# Generated by Django 3.1.5 on 2021-01-13 20:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attributes', '0002_auto_20210113_1346'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoryfeature',
            options={'verbose_name': 'Характеристика', 'verbose_name_plural': 'Характеристики'},
        ),
        migrations.AlterModelOptions(
            name='featurevalidator',
            options={'verbose_name': 'Валидатор', 'verbose_name_plural': 'Валидаторы'},
        ),
        migrations.AlterModelOptions(
            name='productfeatures',
            options={'verbose_name': 'Значение', 'verbose_name_plural': 'Значения'},
        ),
    ]
