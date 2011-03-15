from django.contrib import admin
from models import *


class RentalAdmin(admin.ModelAdmin):
    list_display = ['item','user','contact','planned_date_out','planned_date_in','date_out','date_in','notes']





admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Rental, RentalAdmin)


