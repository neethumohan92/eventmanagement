# Generated by Django 4.1.4 on 2023-01-03 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_cater', '0004_f_product_userid'),
    ]

    operations = [
        migrations.CreateModel(
            name='C_book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('number', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('prodid', models.CharField(default='0', max_length=20)),
                ('Spotid', models.CharField(default='0', max_length=20)),
                ('userid', models.CharField(default='0', max_length=20)),
                ('price', models.CharField(default='0', max_length=20)),
                ('book', models.BooleanField(default='False')),
                ('status', models.CharField(default='Pending', max_length=20)),
                ('accept', models.BooleanField(default='False')),
                ('reject', models.BooleanField(default='False')),
            ],
        ),
    ]
