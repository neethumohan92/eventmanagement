# Generated by Django 4.1.4 on 2023-02-24 04:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('even_decor', '0017_d_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='d_image',
            old_name='ProductID',
            new_name='DID',
        ),
    ]