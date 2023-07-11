# Generated by Django 4.1.4 on 2023-02-23 11:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('even_decor', '0016_book_paystatus'),
    ]

    operations = [
        migrations.CreateModel(
            name='D_image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.ImageField(upload_to='decor')),
                ('ProductID', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='even_decor.product')),
            ],
        ),
    ]