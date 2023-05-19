from django.contrib import admin
from .models import Contributors
from .models import Projects
from .models import Issues
from .models import Comment

###############################################################################
# [DEBUT] Ces classes permettent à l'interface d'administration Django 
# d'afficher le champs many to many 'contributors_id' de la classe 'Projects'
#
# Documentation Django
# https://docs.djangoproject.com/en/dev/ref/contrib/admin/#working-with-many-to-many-intermediary-models
#
# Et: Afficher en lecture seule le champs project_id :
# Documentation Django
# https://docs.djangoproject.com/en/dev/ref/contrib/admin/#django.contrib.admin.ModelAdmin.readonly_fields
#
class ContributorsInline(admin.TabularInline):
    model = Contributors
    extra = 1


class UserAdmin(admin.ModelAdmin):
    inlines = [ContributorsInline]


class ProjectsAdmin(admin.ModelAdmin):
    readonly_fields = ('project_id', )
    inlines = [ContributorsInline]


class CommentsAdmin(admin.ModelAdmin):
    readonly_fields = ('created_time', 'comment_id')


class IssuesAdmin(admin.ModelAdmin):
    readonly_fields = ('created_time', )

#[FIN] ##############################################################################

admin.site.register(Contributors)
admin.site.register(Issues, IssuesAdmin)
admin.site.register(Projects, ProjectsAdmin)
admin.site.register(Comment, CommentsAdmin)
