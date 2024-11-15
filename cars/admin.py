from django.contrib import admin
from cars.models import Car, Brand


# Register your models here.
# Depois de fazer o makemigrations e o migrate, é preciso configurar o display da classe
# e o campo de busca. Feito isso, serão lidos os arquivos e depois usa register para mostrar no adm

class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value')
    search_fields = ('model',)

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)    

admin.site.register(Brand, BrandAdmin)    
admin.site.register(Car, CarAdmin)  

