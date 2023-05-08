from django.db import models

# Create your models here.

class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Users"

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Projects(models.Model):
    project_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    author_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='projects_author_user_id', default=1)

    class Meta:
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.title


class Contributors(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE, default=1)
    project_id = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name='contributors_project_id', default=1)   
    role = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Contributors"

    def __str__(self):
        return "Contributors"


class Issues(models.Model):
    title = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    tag = models.CharField(max_length=255)
    priority = models.CharField(max_length=255)
    project_id = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name='issues_project_id', default=1)
    author_user_id = models.ForeignKey(Projects, on_delete=models.CASCADE, default=1)
    status = models.CharField(max_length=255)
    author_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='issues_authored_issues', default=1)
    assignee_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='issues_assigned_issues', default=1)
    created_time = models.DateTimeField(auto_now_add=True) 

    class Meta:
        verbose_name_plural = "Issues"

    def __str__(self):
        return self.title


class Comments(models.Model):

    comment_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=255)
    author_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, default=1)
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Comments"

    def __str__(self):
        return self.description
