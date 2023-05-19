from django.contrib.auth import get_user_model
from django.db import models


#
# Obtention du modele 'User' utilisé par Django
#
User = get_user_model()


#
# Creation du modele 'Project'
#
class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    contributors = models.ManyToManyField(User, through="Contributor", related_name='Project_contributors')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='project_author', default=1)

    class Meta:
        # Le nom de la table dans l'interface d'administration Django sera 'Project'
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.title


#
# Creation du modele pour la table de jointure entre User et Project 'Contributor'
#
class Contributor(models.Model):

    # Valeur du champs - Champs visible
    PERMISSIONS = (
        ('admin', 'Administrator'),
        ('member', 'Member'),
        ('guest', 'Guest'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='contributors_project')

    permissions = models.CharField(max_length=255, choices=PERMISSIONS)
    role = models.CharField(max_length=255, null=True, blank=True, default='')

    class Meta:
        # Le nom de la table dans l'interface d'administration Django sera 'Contributors'
        verbose_name_plural = "Contributors"
        # Eviter les doublons : Un user
        #unique_together = ('user_id', 'project_id')


#
# Creation du modele 'Issue'
# 
class Issue(models.Model):
    title = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    tag = models.CharField(max_length=255)
    priority = models.CharField(max_length=255)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='issue_project', default=1)
    status = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='issue_author', default=1)
    assignee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='issue_assignee', default=1)
    created_time = models.DateTimeField(auto_now_add=True) 

    class Meta:
        verbose_name_plural = "Issues"

    def __str__(self):
        return self.title


#
# Creation du modele 'Comment'
# 
class Comment(models.Model):
    description = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE, default=1)
    created_time = models.DateTimeField(auto_now = True)

    class Meta:
        verbose_name_plural = "Comments"

    def __str__(self):
        return self.description
