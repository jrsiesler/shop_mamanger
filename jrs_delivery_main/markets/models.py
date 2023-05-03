from django.db import models

# Create your models here.
class MarketType(models.TextChoices):
    STORE = 'STR'
    MARKET = 'MKT'
    SUPERMARKET = 'SKT'

    def __str__ (self):
        return self.name
    
class MarketChannel(models.TextChoices):
    WHATSAPP = 1
    INSTAGRAN = 2
    FACEBOOK = 3
    GOOGLE = 4
    IFOOD = 5

    def __str__(self):
        return self.name

class MarketStatus(models.TextChoices):
    AVAILABLE = 'A'
    UNAVAILABLE = 'U'
    PENDING = 'P'
    EXCLUDED = 'E'


class Markets(models.Model):
    name = models.CharField('razao social:', max_length=200)
    common_name = models.CharField('nome fantasia:', max_length=60)
    document_number = models.BigIntegerField('cnpj:', max_length=14)
    creation_date = models.DateTimeField('data criacao', null=True)
    market_type = models.CharField(MarketType, max_length=20, null=True)
    integration_ifood = models.BooleanField('integra com ifood')
    id_ifood = models.UUIDField('id da loja ifood')

class MarketAddress(models.Model):
    market = models.ForeignKey(Markets, on_delete=models.CASCADE, null=True)
    adrress = models.CharField('endreço:', max_length=100)
    address_number = models.IntegerField ('numero:', max_length=10)
    address_details = models.CharField('complemento:', max_length=50)
    address_neighborhood = models.CharField('bairro:', max_length=50)
    address_city = models.CharField('municipio', max_length=60)
    address_state = models.CharField('estado:', max_length=2)
    address_country = models.CharField('pais:', max_length=50)
    address_postal_code = models.IntegerField('codigo postal:', max_length=8)
    creation_date = models.DateTimeField('data de cadastro:')



class MarketIntegrations(models.Model):
    market = models.ForeignKey(Markets, on_delete=models.CASCADE)
    market_channel = MarketChannel
    integration_host = models.CharField(max_length=255, null=True)
    access_key = models.CharField(max_length=50, null=True)
    secret_access_key = models.CharField(max_length=50, null=True)

    
