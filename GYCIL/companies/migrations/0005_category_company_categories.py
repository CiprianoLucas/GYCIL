# Generated by Django 5.0 on 2024-02-08 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0004_remove_company_company_name_remove_company_email_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('icon', models.ImageField(blank=True, null=True, upload_to='icons_categories')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.AddField(
            model_name='company',
            name='categories',
            field=models.ManyToManyField(blank=True, to='companies.category'),
        ),
    ]
