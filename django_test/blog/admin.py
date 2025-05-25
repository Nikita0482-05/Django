from django.contrib import admin
from django.contrib.auth.models import Permission

from .models import Blog, Comment

admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(Permission)
