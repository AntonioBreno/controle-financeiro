from django.db import models
from django.conf import settings

class Categoria(models.Model):
    
    TIPO_CHOICES = [
        ('receita', 'Receita'),
        ('despesa', 'Despesa'),
    ]
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=10,choices=TIPO_CHOICES,default='despesa')
    valor_padrao = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.nome