# Generated by Django 3.2.5 on 2023-05-19 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('p5', '0052_auto_20230519_1221'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='issue_project', to='p5.project'),
        ),
    ]
