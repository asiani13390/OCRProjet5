# Generated by Django 3.2.5 on 2023-05-13 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p5', '0020_rename_contributors_projects_contributors_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='id',
        ),
        migrations.AlterField(
            model_name='comments',
            name='comment_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
