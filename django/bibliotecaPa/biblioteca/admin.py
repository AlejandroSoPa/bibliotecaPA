from django.contrib import admin
from .models import Usuari, Centre, Article, Llibre, CD, DVD, BR, Dispositiu, Reserva, Prestec, Solicitud

class CentreAdmin(admin.ModelAdmin):
    list_display = ["nom"]

class LlibreAdmin(admin.ModelAdmin):
    list_display = ["titol", "pagines", "ISBN"]

class CDAdmin(admin.ModelAdmin):
    list_display = ["nom"]

class DVDAdmin(admin.ModelAdmin):
    list_display = ["nom"]

class BRAdmin(admin.ModelAdmin):
    list_display = ["nom"]
    
class DispositiuAdmin(admin.ModelAdmin):
    list_display = ["nom"]


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


class CentreInline(admin.ModelAdmin):
    list_display = ["nom"]



# Register your models here.
admin.site.register(Usuari)
admin.site.register(Centre, CentreAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Llibre)
admin.site.register(CD)
admin.site.register(DVD)
admin.site.register(BR)
admin.site.register(Dispositiu)
admin.site.register(Reserva)
admin.site.register(Prestec)
admin.site.register(Solicitud)