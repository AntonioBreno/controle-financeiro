from django.db import models   

class FormaPagamento(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome