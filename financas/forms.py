from django import forms


from financas.models.categoria import Categoria
from financas.models.formaPagamento import FormaPagamento
from financas.models.transacao import Transacao


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome', 'valor_padrao']
        
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'valor_padrao': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        
        
class TransacaoForm(forms.ModelForm):
    class Meta:
        model = Transacao
        fields = ['categoria', 'tipo', 'valor', 'descricao', 'data']
        
        widgets = {
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'valor': forms.NumberInput(attrs={'class': 'form-control'}),
            'descricao': forms.TextInput(attrs={'class': 'form-control'}),
            'data': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
        
class formaPagamentoForm(forms.ModelForm):
    class Meta:
        model = FormaPagamento
        fields = ['nome']
        
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
        }