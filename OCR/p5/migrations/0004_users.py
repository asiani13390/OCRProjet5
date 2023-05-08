# Generated by Django 4.2.1 on 2023-05-08 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("p5", "0003_remove_comments_id_alter_comments_comment_id"),
    ]

    operations = [
        migrations.CreateModel(
            name="Users",
            fields=[
                ("user_id", models.AutoField(primary_key=True, serialize=False)),
                ("first_name", models.CharField(max_length=255)),
                ("last_name", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=254)),
                ("password", models.CharField(max_length=255)),
            ],
            options={
                "verbose_name_plural": "Users",
            },
        ),
    ]