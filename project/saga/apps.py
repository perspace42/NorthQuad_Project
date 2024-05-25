'''
Author: Scott Field
Date: 5/24/2024
Version: 1.0
Purpose:
Configures the default database field, and name of the application (saga)
'''

from django.apps import AppConfig

class SagaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'saga'
