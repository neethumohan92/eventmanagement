# Generated by Django 4.1.3 on 2022-12-22 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_spot', '0003_s_product_userid'),
    ]

    operations = [
        migrations.AddField(
            model_name='s_product',
            name='Accept',
            field=models.BooleanField(default='False'),
        ),
        migrations.AddField(
            model_name='s_product',
            name='Reject',
            field=models.BooleanField(default='False'),
        ),
    ]
