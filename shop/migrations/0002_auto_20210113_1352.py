# Generated by Django 3.1.5 on 2021-01-13 11:52

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='old_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True, verbose_name='Старая цена'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=mptt.fields.TreeForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.category', verbose_name='Категория'),
        ),
    ]