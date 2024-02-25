# Generated by Django 5.0 on 2024-02-20 14:42

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_alter_service_category_delete_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, null=True, upload_to='services_files/')),
            ],
        ),
        migrations.AlterModelOptions(
            name='service',
            options={'verbose_name': 'Serviço', 'verbose_name_plural': 'Serviços'},
        ),
        migrations.RemoveField(
            model_name='service',
            name='photos',
        ),
        migrations.AddField(
            model_name='service',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='service',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.AddField(
            model_name='service',
            name='imagens',
            field=models.ManyToManyField(to='services.files'),
        ),
    ]
