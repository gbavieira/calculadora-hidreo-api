from django.contrib import admin
from calculadoras.models import LeadBasica, LeadAvancada

class LeadBasicas(admin.ModelAdmin):
    list_display = ('id','nome','potencia','mchs')
    list_display_links = ('id','nome')
    search_fields = ('nome',)
    list_per_page = 20

admin.site.register(LeadBasica, LeadBasicas)

class LeadAvancadas(admin.ModelAdmin):
    list_display = ('id','nome','potencia','mchs')
    list_display_links = ('id','nome')
    search_fields = ('nome',)
    list_per_page = 20

admin.site.register(LeadAvancada, LeadAvancadas)