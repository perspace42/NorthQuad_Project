'''
Author: Scott Field
Date: 5/24/2024
Version: 1.0
Purpose:
Configure the administrator access to the database data, and the UI for acessing that database data
'''

from django.contrib import admin
from .models import Unit,Faction

class UnitInline(admin.TabularInline):
    model = Unit
    extra = 0

class FactionAdmin(admin.ModelAdmin):
    inlines = [UnitInline]
    list_display = ('name','description','specialRules')

#Register Your Models Here
admin.site.register(Faction,FactionAdmin)


'''    
# Old way to register models
admin.site.register(Faction)
admin.site.register(Unit)
'''
