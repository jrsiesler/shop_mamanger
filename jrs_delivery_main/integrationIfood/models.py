from django.db import models
from markets.models import Markets
import logging

# Create your models here.
class IntegrationEnvirionment(models.Model):
    ENVIRONMENT_CHOICES = (
        ('DEV','DEVELOPMENT'),
        ('HML','HOMOLOGATION'),
        ('PRD','PRODUCTION')
    )


class IntegrationConfig(models.Model):
    logging.info('IntegrationConfig:')
    ENVIRONMENT_CHOICES = (
        ('DEV','DEVELOPMENT'),
        ('HML','HOMOLOGATION'),
        ('PRD','PRODUCTION')
    )
    client_id = models.UUIDField()
    client_secret = models.CharField(max_length=120)
    integration_base_url = models.URLField(max_length=120, default=None)
    integration_environment = models.CharField(choices=IntegrationEnvirionment.ENVIRONMENT_CHOICES, max_length=3)
    active = models.BooleanField(default=True)

    # função para retornar a configuração atual do sistema para integração com ifood
    # necessario implementar regras de negocio para validação da configuração retornada
    def get_current_config():
        logging.info('IntegrationConfig.get_current_config')
        config = IntegrationConfig.objects.filter(active=True)
        logging.info(config.count())
        logging.info(config[0])
        return config[0]
    
    def get_all_config():
        config = IntegrationConfig.objects.all()
        return config


class IntegrarionEvent(models.Model):
    market = models.ForeignKey(Markets, on_delete=models.DO_NOTHING)
