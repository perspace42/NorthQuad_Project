'''
Author: Scott Field
Date: 5/24/2024
Version: 1.0
Purpose:
Configure the administrator access to the database data, and the UI for acessing that database data
'''

from django.contrib import admin
from .models import Unit,Faction

# Register your models here.
admin.site.register(Faction)
admin.site.register(Unit)