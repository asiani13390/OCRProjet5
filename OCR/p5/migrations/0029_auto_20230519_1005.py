# Generated by Django 3.2.5 on 2023-05-19 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p5', '0028_rename_comments_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='comment_id',
        ),
        migrations.AddField(
            model_name='comment',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
