from datetime import date

from django.db.models import Sum
from django.contrib.auth.views import LoginView
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

from financas.forms import CategoriaForm, FormaPagamentoForm
from financas.models.categoria import Categoria
from financas.models.formaPagamento import FormaPagamento
from financas.models.transacao import Transacao

# Create your views here.
class CustomLoginView(LoginView):
    template_name = './login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('dashboard') 
    
    
@login_required
def dashboard_view(request):
        
    hoje = date.today()
        
    transacoes = Transacao.objects.filter(
        user=request.user,
        data__month=hoje.month,
        data__year=hoje.year
    )
        
    total_receita = transacoes.filter(tipo='receita').aggregate(Sum('valor'))['valor__sum'] or 0
    total_despesa = transacoes.filter(tipo='despesa').aggregate(Sum('valor'))['valor__sum'] or 0
    saldo = total_receita - total_despesa
        
    context = {
        'total_receita': total_receita,
        'total_despesa': total_despesa,
        'saldo': saldo
    }
    return render(request, 'dashboard.html', context)

# CRUD de Categoria

@login_required
def categoria_create(request):
    form = CategoriaForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('categoria_list')
    return render(request, 'categoria/categoria_form.html', {'form': form})

def categoria_list(request):
    categorias = Categoria.objects.all()
    return render(request, 'categoria/categoria_list.html', {'categorias': categorias})

def categoria_update(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    form = CategoriaForm(request.POST or None, instance=categoria)
    
    if form.is_valid():
        form.save()
        return redirect('categoria_list')
    return render(request, 'categoria/categoria_form.html', {'form': form})

def categoria_delete(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        categoria.delete()
        return redirect('categoria_list')
    return render(request, 'categoria_confirm_delete.html', {'categoria': categoria})
        
        
# CRUD de Forma de Pagamento

def formaPagamento_create(request):
    
    form = FormaPagamentoForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('formaPagamento_list')
    return render(request, 'formaPagamento/formaPagamento_form.html', {'form': form})

def formaPagamento_list(request):
    formaPagamentos = FormaPagamento.objects.all()
    return render(request, 'formaPagamento/formaPagamento_list.html', {'formaPagamentos': formaPagamentos}) 

def formaPagamento_update(request, pk):
    formaPagamento = get_object_or_404(FormaPagamento, pk=pk)
    form = FormaPagamentoForm(request.POST or None, instance=formaPagamento)
    
    if form.is_valid():
        form.save()
        return redirect('formaPagamento_list')
    return render(request, 'formaPagamento/formaPagamento_form.html', {'form': form})

def formaPagamento_delete(request, pk):
    formaPagamento = get_object_or_404(FormaPagamento, pk=pk)
    if request.method == 'POST':
        formaPagamento.delete()
        return redirect('formaPagamento_list')
    return render(request, 'formaPagamento_confirm_delete.html', {'formaPagamento': formaPagamento})