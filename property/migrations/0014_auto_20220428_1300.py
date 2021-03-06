# Generated by Django 2.2.24 on 2022-04-28 10:00

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0013_auto_20220428_1242'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flat',
            name='owners_phonenumber',
        ),
        migrations.RemoveField(
            model_name='owner',
            name='phonenumber',
        ),
        migrations.AlterField(
            model_name='flat',
            name='owner_pure_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(default=None, max_length=128, null=True, region=None, verbose_name='Номер владельца'),
        ),
        migrations.AlterField(
            model_name='owner',
            name='pure_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(default=None, max_length=128, null=True, region=None, verbose_name='Номер владельца'),
        ),
    ]
