# Generated by Django 3.2.5 on 2023-05-13 22:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('p5', '0021_auto_20230513_2137'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contributors',
            old_name='role',
            new_name='permissions',
        ),
    ]