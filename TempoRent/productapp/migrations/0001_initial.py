# Generated by Django 2.2.8 on 2019-12-10 05:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=250)),
                ('product_rate', models.PositiveIntegerField()),
                ('product_date', models.DateField(auto_now_add=True)),
                ('product_catagory', models.CharField(max_length=100)),
                ('product_image', models.ImageField(upload_to='products/')),
                ('product_rules', models.TextField()),
                ('location', models.CharField(max_length=100)),
                ('late_charge', models.PositiveIntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Prebooking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('location', models.CharField(max_length=10)),
                ('product_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productapp.Product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PendingProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=250)),
                ('product_rate', models.PositiveIntegerField()),
                ('product_date', models.DateField(auto_now_add=True)),
                ('product_catagory', models.CharField(max_length=100)),
                ('product_image', models.ImageField(upload_to='products/')),
                ('product_rules', models.TextField()),
                ('location', models.CharField(max_length=100)),
                ('late_charge', models.PositiveIntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
