# Generated by Django 3.2.5 on 2023-05-19 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('p5', '0034_alter_issues_assignee_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='issues',
            old_name='assignee_user_id',
            new_name='assignee',
        ),
        migrations.RenameField(
            model_name='issues',
            old_name='author_user_id',
            new_name='author',
        ),
    ]