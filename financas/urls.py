from django.urls import path
from financas import views

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),
    
    
    # Categoria URLs
    path('categorias/', views.categoria_list, name='categoria_list'),
    path('categorias/criar/', views.categoria_create, name='categoria_create'),
    path('categorias/<int:pk>/editar/', views.categoria_update, name='categoria_update'),
    path('categorias/<int:pk>/deletar/', views.categoria_delete, name='categoria_delete'),
]