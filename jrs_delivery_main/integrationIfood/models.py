from django.db import models
from markets.models import Markets

# Create your models here.
class IntegrationEnvirionment(models.Model):
    ENVIRONMENT_CHOICES = (
        ('DEV','DEVELOPMENT'),
        ('HML','HOMOLOGATION'),
        ('PRD','PRODUCTION')
    )


class IntegrationConfig(models.Model):
    ENVIRONMENT_CHOICES = (
        ('DEV','DEVELOPMENT'),
        ('HML','HOMOLOGATION'),
        ('PRD','PRODUCTION')
    )
    client_id = models.UUIDField()
    client_secret = models.CharField(max_length=120)
    integration_base_url = models.URLField(max_length=120, default=None)
    integration_environment = models.CharField(choices=IntegrationEnvirionment.ENVIRONMENT_CHOICES, max_length=3)



class IntegrarionEvent(models.Model):
    market = models.ForeignKey(Markets, on_delete=models.DO_NOTHING)
