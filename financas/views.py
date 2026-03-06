from datetime import date

from django.db.models import Sum
from django.contrib.auth.views import LoginView
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

from financas.forms import CategoriaForm, FormaPagamentoForm, TransacaoForm
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
def categoria_list_create(request):
    
    categorias = Categoria.objects.filter(user=request.user).order_by('-id')
    
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            categoria = form.save(commit=False)
            categoria.user = request.user 
            categoria.save()
            return redirect('categoria_list_create')
    else:
        form = CategoriaForm()

    context = {
        'form': form,
        'categorias': categorias
    }

    return render(request, 'categoria/categoria_page.html', context)

@login_required
def categoria_update(request, pk):
    categoria = get_object_or_404(
        Categoria,
        pk=pk,
        user=request.user  
    )

    form = CategoriaForm(request.POST or None, instance=categoria)

    if form.is_valid():
        form.save()
        return redirect('categoria_list_create')

    return render(request, 'categoria/categoria_form.html', {'form': form})

@login_required
def categoria_delete(request, pk):
    categoria = get_object_or_404(
        Categoria,
        pk=pk,
        user=request.user  
    )

    if request.method == 'POST':
        categoria.delete()
        return redirect('categoria_list_create')

    return render(request, 'categoria_confirm_delete.html', {'categoria': categoria})
        
# CRUD de Forma de Pagamento

@login_required
def formaPagamento_list_create(request):
    
    formaPagamentos = FormaPagamento.objects.filter(
        user=request.user
    ).order_by('-id')
    
    if request.method == "POST":
        form = FormaPagamentoForm(request.POST)
        if form.is_valid():
            forma_pagamento = form.save(commit=False)
            forma_pagamento.user = request.user  
            forma_pagamento.save()
            return redirect('formaPagamento_list_create')
    else:
        form = FormaPagamentoForm()

    context = {
        'form': form,
        'formaPagamentos': formaPagamentos
    }

    return render(request, 'formaPagamento/formaPagamento_page.html', context) 

@login_required
def formaPagamento_detail(request, pk):
    formaPagamento = get_object_or_404(
        FormaPagamento,
        pk=pk,
        user=request.user  
    )
    
    return render(
        request,
        'formaPagamento/formaPagamento_detail.html',
        {'formaPagamento': formaPagamento}
    )

@login_required
def formaPagamento_update(request, pk):
    
    formaPagamento = get_object_or_404(
        FormaPagamento,
        pk=pk,
        user=request.user  
    )

    form = FormaPagamentoForm(request.POST or None, instance=formaPagamento)
    
    if form.is_valid():
        form.save()
        return redirect('formaPagamento_list_create')

    return render(
        request,
        'formaPagamento/formaPagamento_form.html',
        {'form': form}
    )

@login_required
def formaPagamento_delete(request, pk):
    
    formaPagamento = get_object_or_404(
        FormaPagamento,
        pk=pk,
        user=request.user  # 🔥 proteção importante
    )

    if request.method == 'POST':
        formaPagamento.delete()
        return redirect('formaPagamento_list_create')

    return render(
        request,
        'formaPagamento_confirm_delete.html',
        {'formaPagamento': formaPagamento}
    )
    
# CRUD de Transação 
@login_required
def transacao_list_create(request):
    
    transacao = Transacao.objects.filter(
        user=request.user
    ).order_by('-id')
    
    if request.method == "POST":
        form = TransacaoForm(request.POST)

        # FILTRA AS CATEGORIAS DO USUÁRIO
        form.fields['categoria'].queryset = Categoria.objects.filter(user=request.user)

        if form.is_valid():
            transacao = form.save(commit=False)
            transacao.user = request.user  
            transacao.save()
            return redirect('transacao_list_create')
    else:
        form = TransacaoForm()

        # FILTRA AS CATEGORIAS DO USUÁRIO
        form.fields['categoria'].queryset = Categoria.objects.filter(user=request.user)

    context = {
        'form': form,
        'transacao': transacao
    }

    return render(request, 'transacao/transacao_page.html', context)

@login_required
def transacao_detail(request, pk):
    transacao = get_object_or_404(
        Transacao,
        pk=pk,
        user=request.user  
    )

    return render(
        request,
        'transacao/transacao_detail.html',
        {'transacao': transacao}
    )

@login_required
def transacao_update(request, pk):
    transacao = get_object_or_404(
        Transacao,
        pk=pk,
        user=request.user
    )

    form = TransacaoForm(request.POST or None, instance=transacao)

    if form.is_valid():
        form.save()
        return redirect('transacao_list_create')

    return render(request, 'transacao/transacao_form.html', {'form': form})

@login_required
def transacao_delete(request, pk):
    transacao = get_object_or_404(
        Transacao,
        pk=pk,
        user=request.user
    )

    if request.method == 'POST':
        transacao.delete()
        return redirect('transacao_list_create')

    return render(request, 'transacao_confirm_delete.html', {'transacao': transacao})


# CRUD de Categoria 
@login_required
def categoria_list_create(request):
    
    categoria = Categoria.objects.filter(
        user=request.user
    ).order_by('-id')
    
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            categoria = form.save(commit=False)
            categoria.user = request.user  
            categoria.save()
            return redirect('categoria_list_create')
    else:
        form = CategoriaForm()

    context = {
        'form': form,
        'categoria': categoria
    }

    return render(request, 'categoria/categoria_page.html', context)

@login_required
def categoria_detail(request, pk):
    categoria = get_object_or_404(
        Categoria,
        pk=pk,
        user=request.user  
    )

    return render(
        request,
        'categoria/categoria_detail.html',
        {'categoria': categoria}
    )

@login_required
def categoria_update(request, pk):
    categoria = get_object_or_404(
        Categoria,
        pk=pk,
        user=request.user
    )

    form = CategoriaForm(request.POST or None, instance=categoria)

    if form.is_valid():
        form.save()
        return redirect('categoria_list_create')

    return render(request, 'categoria/categoria_form.html', {'form': form})

@login_required
def categoria_delete(request, pk):
    categoria = get_object_or_404(
        Categoria,
        pk=pk,
        user=request.user
    )

    if request.method == 'POST':
        categoria.delete()
        return redirect('categoria_list_create')

    return render(request, 'categoria/categoria_confirm_delete.html', {'categoria': categoria})

@login_required
def categoria_valor(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk, user=request.user)

    data = {
        'valor_padrao': categoria.valor_padrao
    }

    return JsonResponse(data)