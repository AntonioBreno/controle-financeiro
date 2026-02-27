from datetime import date

from django.db.models import Sum
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

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

        