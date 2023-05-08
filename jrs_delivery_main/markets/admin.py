from django.contrib import admin
from .models import Markets, MarketIntegrations, MarketAddress
# Register your models here.



class MarketAdressInLine(admin.StackedInline):
    model = MarketAddress
    extra = False

class MarketIntegrarionInLine(admin.StackedInline):
    model = MarketIntegrations
    extra = False

class MarketsAdmin(admin.ModelAdmin):
        model = Markets
        fieldsets = [
        (None,   {'fields': ['name', 'common_name', 'document_number']})
    ]

admin.site.register(Markets, MarketsAdmin)