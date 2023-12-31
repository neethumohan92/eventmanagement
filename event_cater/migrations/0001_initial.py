# Generated by Django 4.1.3 on 2022-12-14 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cater_DB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=20)),
                ('Number', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=50)),
                ('Businessname', models.CharField(max_length=20)),
                ('Place', models.CharField(max_length=50)),
                ('Password', models.CharField(max_length=15)),
                ('Image', models.ImageField(upload_to='cater')),
                ('Experience', models.IntegerField(default=2)),
            ],
        ),
        migrations.CreateModel(
            name='F_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('slug', models.SlugField(max_length=250, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='F_Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Desc', models.CharField(max_length=500)),
                ('Price', models.CharField(max_length=50)),
                ('Image', models.ImageField(upload_to='cater')),
                ('CaterID', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='event_cater.cater_db')),
                ('FCategory', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='event_cater.f_category')),
            ],
        ),
    ]
