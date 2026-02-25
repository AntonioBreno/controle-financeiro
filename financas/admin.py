from django.contrib import admin

from .models import Categoria, FormaPagamento, Transacao
# Register your models here.

    
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'valor_padrao')
    search_fields = ('nome',)
    
    
class FormaPagamentoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    
class TransacaoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'categoria', 'tipo', 'valor', 'descricao', 'data', 'criado_em')
    list_filter = ('tipo', 'data')
    search_fields = ('descricao',)


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(FormaPagamento, FormaPagamentoAdmin)
admin.site.register(Transacao, TransacaoAdmin)