# Generated by Django 4.0 on 2021-12-30 17:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ugc', '0002_alter_profile_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'Профиль', 'verbose_name_plural': 'Профили'},
        ),
    ]
