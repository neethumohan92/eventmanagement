# Generated by Django 4.1.4 on 2023-01-13 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_cater', '0011_c_book_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='c_book',
            name='review',
            field=models.CharField(default='Null', max_length=20),
        ),
    ]
