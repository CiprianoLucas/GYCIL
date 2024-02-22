# Generated by Django 5.0 on 2024-02-20 17:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0007_company_thumbnail'),
        ('services', '0005_remove_service_neighbor_alter_service_company_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='companies.company'),
        ),
    ]