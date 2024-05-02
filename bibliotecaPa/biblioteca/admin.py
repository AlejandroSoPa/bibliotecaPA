from django.contrib import admin
from .models import Usuari, Centre, Article, Llibre, CD, DVD, BR, Dispositiu, Reserva, Prestec, Solicitud, Log
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class UsuariAdmin(admin.ModelAdmin):
    list_display = ["username", "data_naixement", 'centre' , "cicle", "imatge", "admin"]

class LogAdmin(admin.ModelAdmin):
    list_display = ["esdeveniment", "nivell", "data", "usuari", "ruta"]

class CentreAdmin(admin.ModelAdmin):
    list_display = ["nom"]

class LlibreAdmin(admin.ModelAdmin):
    list_display = ["titol", "pagines", "ISBN", "disponibilidad"]

class CDAdmin(admin.ModelAdmin):
    list_display = ["discografia", "durada"]

class DVDAdmin(admin.ModelAdmin):
    list_display = ["director", "durada"]

class BRAdmin(admin.ModelAdmin):
    list_display = ["estudi"]
    
class DispositiuAdmin(admin.ModelAdmin):
    list_display = ["model","marca"]

class ReservaAdmin(admin.ModelAdmin):
    list_display = ["usuari", "article", "data_reserva"]

class PrestecAdmin(admin.ModelAdmin):
    list_display = ["usuari", "article", "data_préstec", "data_retorn"]

class SolicitudAdmin(admin.ModelAdmin):
    list_display = ["usuari", "article", "data_sol·licitud", "centre_solicitant"]

class LlibreInline(admin.TabularInline):  
    model = Llibre
    extra = 0
    exclude = ["signatura"]

class CDInline(admin.TabularInline):  
    model = CD
    extra = 0

class DVDInline(admin.TabularInline):  
    model = CD
    extra = 0

class BRInline(admin.TabularInline):  
    model = CD
    extra = 0

class DispositiuInline(admin.TabularInline):  
    model = CD
    extra = 0

class ArticleAdmin(admin.ModelAdmin):
    inlines = [LlibreInline, CDInline]
    list_display = ["titol", "autor", "data_publicacio"]


# Register your models here.
admin.site.register(Usuari, UsuariAdmin)
admin.site.register(Centre, CentreAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Llibre, LlibreAdmin)
admin.site.register(CD, CDAdmin)
admin.site.register(DVD, DVDAdmin)
admin.site.register(BR, BRAdmin)
admin.site.register(Dispositiu, DispositiuAdmin)
admin.site.register(Reserva, ReservaAdmin)
admin.site.register(Prestec, PrestecAdmin)
admin.site.register(Solicitud, SolicitudAdmin) 
admin.site.register(Log, LogAdmin)