# Generated by Django 4.1.4 on 2023-01-12 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_cater', '0010_f_product_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='c_book',
            name='review',
            field=models.CharField(default='Good', max_length=20),
        ),
    ]
