from django.apps import AppConfig


class IntegrationifoodConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'integrationIfood'
    def ready(self):
        from integrationIfood import integrartion
        integrartion.start_ifood_integration()
        integrartion.job_pooling()
        
