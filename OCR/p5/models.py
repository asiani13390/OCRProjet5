from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

User = get_user_model()

class Projects(models.Model):
    project_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    author_user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects_author_user', default=1)
  
    class Meta:
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.title


class Contributors(models.Model):

    # Valeur du champs - Champs visible
    ROLES = (
        ('admin', 'Administrator'),
        ('member', 'Member'),
        ('guest', 'Guest'),
    )

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    project_id = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name='contributors')
    role = models.CharField(max_length=255, choices=ROLES)

    class Meta:
        verbose_name_plural = "Contributors"


class Issues(models.Model):
    title = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    tag = models.CharField(max_length=255)
    priority = models.CharField(max_length=255)
    project_id = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name='issues_project_id', default=1)
    status = models.CharField(max_length=255)
    author_user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='issues_authored_issues', default=1)
    assignee_user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='issues_assigned_issues', default=1)
    created_time = models.DateTimeField(auto_now_add=True) 

    class Meta:
        verbose_name_plural = "Issues"

    def __str__(self):
        return self.title


class Comments(models.Model):
    comment_id = models.IntegerField(null = True)
    description = models.CharField(max_length=255)
    author_user_id = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    issue_id = models.ForeignKey(Issues, on_delete=models.CASCADE, default=1)
    created_time = models.DateTimeField(auto_now = True)

    class Meta:
        verbose_name_plural = "Comments"

    def __str__(self):
        return self.description
