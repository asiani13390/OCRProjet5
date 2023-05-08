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

class Comments(models.Model):

    comment_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=255)
    author_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, default=1)
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Comments"

    def __str__(self):
        return self.description
