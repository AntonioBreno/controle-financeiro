from django.contrib import admin
from .models import Gasto, Categoria, Receita, FormaPagamento
# Register your models here.

class GastoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'valor', 'data', 'categoria', 'forma_pagamento')
    list_filter = ('data', 'categoria', 'forma_pagamento')
    search_fields = ('nome',)
    
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'valor_padrao')
    search_fields = ('nome',)
    
class ReceitaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'valor', 'data', 'categoria')
    list_filter = ('data', 'categoria')
    search_fields = ('nome',)
    
class FormaPagamentoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

admin.site.register(Gasto, GastoAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Receita, ReceitaAdmin)
admin.site.register(FormaPagamento, FormaPagamentoAdmin)