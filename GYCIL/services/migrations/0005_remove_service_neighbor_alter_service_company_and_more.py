# Generated by Django 5.0 on 2024-02-20 17:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0007_company_thumbnail'),
        ('services', '0004_files_alter_service_options_remove_service_photos_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='neighbor',
        ),
        migrations.AlterField(
            model_name='service',
            name='company',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='companies.company'),
        ),
        migrations.AlterField(
            model_name='service',
            name='date',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='service',
            name='description',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='service',
            name='hours_service',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='service',
            name='imagens',
            field=models.ManyToManyField(blank=True, to='services.files'),
        ),
        migrations.AlterField(
            model_name='service',
            name='number',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='service',
            name='price',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='service',
            name='rating',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='service',
            name='status',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
