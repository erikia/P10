from django.contrib import admin

from softapi.models import Project, Contributor, Issue, Comment
from user.models import User

admin.site.register(User)
admin.site.register(Project)
admin.site.register(Contributor)
admin.site.register(Issue)
admin.site.register(Comment)
