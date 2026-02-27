from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

class Transacao(models.Model):
    TIPO_CHOICES = (
        ('receita', 'Receita'),
        ('despesa', 'Despesa'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)
    
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.CharField(max_length=255)
    data = models.DateField()
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tipo.capitalize()} - {self.valor} - {self.descricao}"