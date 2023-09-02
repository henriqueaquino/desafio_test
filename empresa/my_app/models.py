from django.db import models

class Departamento(models.Model):
    criado = models.DateTimeField(auto_now_add=True)
    nome = models.CharField(max_length=100, blank=True, default='')

class Empregado(models.Model):
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    criado = models.DateTimeField(auto_now_add=True)
    nome = models.CharField(max_length=100, blank=True, default='')
    cpf = models.CharField(max_length=100, blank=True, default='')
    email = models.EmailField

    class Meta:
        ordering = ['criado']

