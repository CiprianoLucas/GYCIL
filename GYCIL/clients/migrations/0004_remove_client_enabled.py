# Generated by Django 5.0 on 2024-02-13 19:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0003_client_name_client_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='enabled',
        ),
    ]