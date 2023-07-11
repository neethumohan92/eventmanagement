# Generated by Django 4.1.3 on 2022-12-05 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Decor_DB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=20, unique=True)),
                ('Number', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=50)),
                ('Businessname', models.CharField(max_length=20, unique=True)),
                ('Place', models.CharField(max_length=50)),
                ('Password', models.CharField(max_length=15)),
                ('Image', models.ImageField(upload_to='img')),
                ('Experience', models.IntegerField(default=2)),
            ],
        ),
    ]