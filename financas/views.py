from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

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
    return render(request, 'dashboard.html')