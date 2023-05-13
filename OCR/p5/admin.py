from django.contrib import admin

from .models import Contributors
from .models import Projects
from .models import Issues
from .models import Comments
from .models import ProjectsAdmin

admin.site.register(Contributors)
admin.site.register(Issues)
admin.site.register(Comments)
admin.site.register(Projects, ProjectsAdmin)