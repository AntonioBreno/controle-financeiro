from django.urls import path
from financas import views
urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),
]