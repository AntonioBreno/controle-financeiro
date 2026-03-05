from django.urls import path
from financas import views

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),
    
    
    # Categoria URLs
    path('categorias/', views.categoria_list_create, name='categoria_list_create'),
    path('categorias/<int:pk>/', views.categoria_detail, name='categoria_detail'),
    path('update/<int:pk>/', views.categoria_update, name='categoria_update'),
    path('delete/<int:pk>/', views.categoria_delete, name='categoria_delete'),
    
    path('formasPagamento/', views.formaPagamento_list_create, name='formaPagamento_list_create'),
    path('formasPagamento/<int:pk>/', views.formaPagamento_detail, name='formaPagamento_detail'),
    path('update/<int:pk>/', views.formaPagamento_update, name='formaPagamento_update'),
    path('delete/<int:pk>/', views.formaPagamento_delete, name='formaPagamento_delete'),
    
    path('transacao/', views.transacao_list_create, name='transacao_list_create'),
    path('transacoes/<int:pk>/', views.transacao_detail, name='transacao_detail'),
    path('update/<int:pk>/', views.transacao_update, name='transacao_update'),
    path('delete/<int:pk>/', views.transacao_delete, name='transacao_delete'),

]