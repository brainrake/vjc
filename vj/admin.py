from django.contrib import admin
from vj.models import *

class TeamAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Team,TeamAdmin)
