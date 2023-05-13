from django.contrib import admin

from .models import Contributors

from .models import Projects
from .models import ProjectsAdmin

from .models import Issues
from .models import IssuesAdmin

from .models import Comments
from .models import CommentsAdmin

admin.site.register(Contributors)
admin.site.register(Issues, IssuesAdmin)
admin.site.register(Projects, ProjectsAdmin)
admin.site.register(Comments, CommentsAdmin)
