from django import forms


from financas.models.categoria import Categoria
from financas.models.formaPagamento import FormaPagamento
from financas.models.transacao import Transacao


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome', 'tipo', 'valor_padrao']
        
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'valor_padrao': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # remove user dos kwargs
        super().__init__(*args, **kwargs)

        if user:
            self.fields['categoria'].queryset = Categoria.objects.filter(user=user)
        
        
class TransacaoForm(forms.ModelForm):
    class Meta:
        model = Transacao
        fields = ['tipo','categoria', 'valor', 'descricao', 'data']
        
        widgets = {
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'valor': forms.NumberInput(attrs={'class': 'form-control'}),
            'descricao': forms.TextInput(attrs={'class': 'form-control'}),
            'data': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
        
class FormaPagamentoForm(forms.ModelForm):
    class Meta:
        model = FormaPagamento
        fields = ['nome']
        
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
        }