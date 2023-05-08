from django.db import models

# Create your models here.
class MarketType(models.Model):
    MARKET_TYPE_CHOICES = (
        ('STR','STORE'),
        ('MKT','MARKET'),
        ('SKT','SUPERMARKET')
    )    

    def __str__ (self):
        return self.name
    
class MarketChannel(models.Model):
    MARKET_CHANNEL_CHOICES = (
        ('WTZ','WHATSAPP'),
        ('ITG','INSTAGRAN'),
        ('FBK','FACEBOOK'),
        ('GOG','GOOGLE'),
        ('IFD', 'IFOOD')
    )    

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
    # market_type = models.CharField(choices=MarketType.MARKET_TYPE_CHOICES, max_length=3, null=True)

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
    market_channel = models.CharField('canal de vendas: ', choices=MarketChannel.MARKET_CHANNEL_CHOICES, max_length=3, default='MKT')
    integration_host = models.CharField(max_length=255, null=True)
    integration_id = models.BooleanField('integra com ifood', null=True)
    id_ifood = models.UUIDField('id da loja ifood', null=True)
    access_key = models.CharField('access-key ou client-id: ', max_length=50, null=True)
    secret_access_key = models.CharField('secret-key ou client-secret: ', max_length=50, null=True)
    active = models.BooleanField

    
