# Generated by Django 3.2.5 on 2023-05-19 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('p5', '0030_rename_author_user_id_comment_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='issue_id',
            new_name='issue',
        ),
    ]
