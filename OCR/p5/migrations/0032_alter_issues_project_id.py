# Generated by Django 3.2.5 on 2023-05-19 10:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('p5', '0031_rename_issue_id_comment_issue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issues',
            name='project_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='issue_project', to='p5.projects'),
        ),
    ]
