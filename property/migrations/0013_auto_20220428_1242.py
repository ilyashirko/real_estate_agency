# Generated by Django 2.2.24 on 2022-04-28 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0012_auto_20220423_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='floor',
            field=models.CharField(db_index=True, help_text='Первый этаж, последний этаж, пятый этаж', max_length=3, verbose_name='Этаж'),
        ),
        migrations.AlterField(
            model_name='flat',
            name='new_building',
            field=models.BooleanField(db_index=True, default=None, null=True, verbose_name='Новый дом?'),
        ),
        migrations.AlterField(
            model_name='flat',
            name='owner',
            field=models.CharField(db_index=True, max_length=200, verbose_name='ФИО владельца'),
        ),
        migrations.AlterField(
            model_name='flat',
            name='town_district',
            field=models.CharField(blank=True, db_index=True, help_text='Чертаново Южное', max_length=50, verbose_name='Район города, где находится квартира'),
        ),
        migrations.AlterField(
            model_name='owner',
            name='full_name',
            field=models.CharField(db_index=True, max_length=200, verbose_name='ФИО владельца'),
        ),
    ]
