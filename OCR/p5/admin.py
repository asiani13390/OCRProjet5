from django.contrib import admin
from .models import Contributor
from .models import Project
from .models import Issue
from .models import Comment

###############################################################################
# [DEBUT] Ces classes permettent à l'interface d'administration Django 
# d'afficher le champs many to many 'contributors_id' de la classe 'Project'
#
# Documentation Django
# https://docs.djangoproject.com/en/dev/ref/contrib/admin/#working-with-many-to-many-intermediary-models
#
# Et: Afficher en lecture seule le champs project_id :
# Documentation Django
# https://docs.djangoproject.com/en/dev/ref/contrib/admin/#django.contrib.admin.ModelAdmin.readonly_fields
#
class ContributorsInline(admin.TabularInline):
    model = Contributor
    extra = 1


class UserAdmin(admin.ModelAdmin):
    inlines = [ContributorsInline]


class IssueAdmin(admin.ModelAdmin):
    readonly_fields = ('created_time', )


class ProjectAdmin(admin.ModelAdmin):
    inlines = [ContributorsInline]

#[FIN] ##############################################################################

admin.site.register(Contributor)
admin.site.register(Issue, IssueAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Comment)
