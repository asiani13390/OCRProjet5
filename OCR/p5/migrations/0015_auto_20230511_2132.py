# Generated by Django 3.2.5 on 2023-05-11 21:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('p5', '0014_rename_author_user_id_projects_author_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='author_user',
        ),
        migrations.AddField(
            model_name='projects',
            name='author_user_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='projects_author_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comments',
            name='author_user_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='contributors',
            name='project_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contributors', to='p5.projects'),
        ),
        migrations.AlterField(
            model_name='contributors',
            name='role',
            field=models.CharField(choices=[('admin', 'Administrator'), ('member', 'Member'), ('guest', 'Guest')], max_length=255),
        ),
        migrations.AlterField(
            model_name='contributors',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='issues',
            name='assignee_user_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='issues_assigned_issues', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='issues',
            name='author_user_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='issues_authored_issues', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Users',
        ),
    ]