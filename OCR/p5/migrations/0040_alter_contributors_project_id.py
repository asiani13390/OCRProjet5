# Generated by Django 3.2.5 on 2023-05-19 10:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('p5', '0039_auto_20230519_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contributors',
            name='project_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contributors_project', to='p5.projects'),
        ),
    ]
