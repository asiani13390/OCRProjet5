from django.contrib.auth import get_user_model
from django.db import models
from django.contrib import admin

#
# Obtention du modele 'User' utilisé par Django
#
User = get_user_model()

#
# Creation du modele 'Projects'
#
class Projects(models.Model):
    project_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    contributors_id = models.ManyToManyField(User, through="Contributors", related_name='Projects_contributors')
    author_user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects_author_user', default=1)
    

    class Meta:
        # Le nom de la table dans l'interface d'administration Django sera 'Projects'
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.title


#
# Creation du modele pour la table de jointure entre User et Projects 'Contributors'
#
class Contributors(models.Model):

    # Valeur du champs - Champs visible
    ROLES = (
        ('admin', 'Administrator'),
        ('member', 'Member'),
        ('guest', 'Guest'),
    )

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    project_id = models.ForeignKey('Projects', on_delete=models.CASCADE, related_name='contributors_projects_id')
    role = models.CharField(max_length=255, choices=ROLES)

    class Meta:
        # Le nom de la table dans l'interface d'administration Django sera 'Contributors'
        verbose_name_plural = "Contributors"
        # Eviter les doublons
        unique_together = ('user_id', 'project_id')
    
#
# Creation du modele 'Issues'
# 
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

#
# Creation du modele 'Comments'
# 
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


###############################################################################
# [DEBUT] Ces classes permettent à l'interface d'administration Django 
# d'afficher le champs many to many 'contributors_id' de la classe 'Projects'
#
# Documentation Django
# https://docs.djangoproject.com/en/dev/ref/contrib/admin/#working-with-many-to-many-intermediary-models
#
class ContributorsInline(admin.TabularInline):
    model = Contributors
    extra = 1

class UserAdmin(admin.ModelAdmin):
    inlines = [ContributorsInline]


class ProjectsAdmin(admin.ModelAdmin):
    inlines = [ContributorsInline]

#[FIN] ##############################################################################
