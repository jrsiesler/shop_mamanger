from django.contrib import admin
from .models import Markets, MarketIntegrations, MarketAddress
# Register your models here.



class MarketAdressInLine(admin.StackedInline):
    model = MarketAddress
    extra = False

class MarketIntegrarionInLine(admin.StackedInline):
    model = MarketIntegrations
    extra = 3

class MarketsAdmin(admin.ModelAdmin):
        model = Markets
        fieldsets = [
        (None,   {'fields': ['name', 'common_name', 'document_number']}),
        ('tipo', {'fields': ['market_type'], 'classes': ['list']})
    ]
        inlines = [
        MarketAdressInLine,
        MarketIntegrarionInLine
        ]

admin.site.register(Markets, MarketsAdmin)