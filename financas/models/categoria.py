from django.db import models


class Categoria(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    
    nome = models.CharField(max_length=100)
    valor_padrao = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.nome