from django.urls import path
from financas import views

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),
    
    
    # Categoria URLs
    path('categorias/', views.categoria_list_create, name='categoria_list_create'),
    path('update/<int:pk>/', views.categoria_update, name='categoria_update'),
    path('delete/<int:pk>/', views.categoria_delete, name='categoria_delete'),
    
    path('formasPagamento/', views.formaPagamento_list_create, name='formaPagamento_list_create'),
    path('update/<int:pk>/', views.formaPagamento_update, name='formaPagamento_update'),
    path('delete/<int:pk>/', views.formaPagamento_delete, name='formaPagamento_delete'),
]