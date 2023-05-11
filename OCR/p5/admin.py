from django.contrib import admin

# Register your models here.

from .models import Contributors
from .models import Projects
from .models import Issues
from .models import Comments

admin.site.register(Contributors)
admin.site.register(Projects)
admin.site.register(Issues)
admin.site.register(Comments)
