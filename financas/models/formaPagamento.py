from django.conf import settings
from django.db import models   

class FormaPagamento(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome