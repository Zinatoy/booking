# Generated by Django 4.0.4 on 2022-05-21 10:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0002_alter_settings_description_alter_settings_email_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='settings',
            options={'verbose_name': 'Настройка', 'verbose_name_plural': 'Настройки'},
        ),
    ]
