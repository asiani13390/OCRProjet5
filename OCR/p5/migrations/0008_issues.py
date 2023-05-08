# Generated by Django 4.2.1 on 2023-05-08 17:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("p5", "0007_contributors"),
    ]

    operations = [
        migrations.CreateModel(
            name="Issues",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("desc", models.CharField(max_length=255)),
                ("tag", models.CharField(max_length=255)),
                ("priority", models.CharField(max_length=255)),
                ("status", models.CharField(max_length=255)),
                ("created_time", models.DateTimeField(auto_now_add=True)),
                (
                    "assignee_user_id",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="issues_assigned_issues",
                        to="p5.users",
                    ),
                ),
                (
                    "author_user_id",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="issues_authored_issues",
                        to="p5.users",
                    ),
                ),
                (
                    "project_id",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="issues_project_id",
                        to="p5.projects",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Issues",
            },
        ),
    ]