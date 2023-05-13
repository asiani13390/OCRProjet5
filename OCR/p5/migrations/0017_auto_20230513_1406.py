# Generated by Django 3.2.5 on 2023-05-13 14:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('p5', '0016_alter_contributors_project_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='contributors',
            field=models.ManyToManyField(related_name='Projects_contributors', through='p5.Contributors', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='contributors',
            name='project_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contributors_projects_id', to='p5.projects'),
        ),
        migrations.AlterUniqueTogether(
            name='contributors',
            unique_together={('user_id', 'project_id')},
        ),
    ]