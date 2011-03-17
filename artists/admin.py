from django.contrib import admin
from models import *

class ArtistAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Artist, ArtistAdmin)
