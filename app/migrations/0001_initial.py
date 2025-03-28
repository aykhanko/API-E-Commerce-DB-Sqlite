# Generated by Django 5.1.7 on 2025-03-19 15:42

import app.models.products
import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('PC', 'PC'), ('Laptop', 'Laptop'), ('CPU', 'CPU'), ('GPU', 'GPU'), ('RAM', 'RAM'), ('Storage', 'Storage')], max_length=10)),
                ('brand', models.CharField(max_length=150)),
                ('price', models.IntegerField()),
                ('description', models.CharField(max_length=150)),
                ('photo', models.ImageField(upload_to=app.models.products.product_image_path)),
                ('cpu', models.CharField(blank=True, max_length=150, null=True)),
                ('gpu', models.CharField(blank=True, max_length=150, null=True)),
                ('storage', models.CharField(blank=True, max_length=150, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, max_length=30, null=True, validators=[django.core.validators.RegexValidator(message='Nömrəni düzgün daxil edin: XXX-XXX-XXXX)', regex='^\\+?[0-9\\s\\(\\)\\-]+$')])),
                ('mail', models.EmailField(blank=True, max_length=254, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Profiles',
            },
        ),
        migrations.CreateModel(
            name='UserProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
