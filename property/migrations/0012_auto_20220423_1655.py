# Generated by Django 2.2.24 on 2022-04-23 13:55

from django.db import migrations


def link_flats_and_owners(apps, scheme_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    flats = Flat.objects.all()
    for flat in flats.iterator():
        owner = Owner.objects.get_or_create(
            full_name=flat.owner,
            phonenumber=flat.owners_phonenumber,
            pure_phone=flat.owner_pure_phone
        )


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0011_auto_20220423_1547'),
    ]

    operations = [
        migrations.RunPython(link_flats_and_owners)
    ]

