from django.contrib import admin
from .models import IntegrationConfig
# Register your models here.



class IntegrationConfigAdmin(admin.ModelAdmin):
        model = IntegrationConfig
        fieldsets = [
        (None,   {'fields': ['client_id', 'client_secret', 'integration_base_url', 'integration_environment']})
    ]

admin.site.register(IntegrationConfig, IntegrationConfigAdmin)