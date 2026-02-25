from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from financas.views import CustomLoginView
from financas.views import dashboard_view

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('dashboard/', dashboard_view, name='dashboard'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'), # ROTA LOGIN
    path('logout/', auth_views.LogoutView.as_view(next_page='/login/'), name='logout'), # ROTA LOGOUT
]
