# Generated by Django 3.2.5 on 2023-05-13 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p5', '0024_alter_contributors_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contributors',
            name='role',
            field=models.CharField(default='', max_length=255),
        ),
    ]
