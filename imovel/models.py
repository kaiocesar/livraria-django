from datetime import datetime
from django.db import models


class Finalidade(models.Model):
    nome = models.CharField(max_length=45)
    status = models.CharField(max_length=2)

    def __unicode__(self):
        return self.nome


class Tipoimovel(models.Model):
    nome = models.CharField(max_length=45)
    status = models.CharField(max_length=2)

    def __unicode__(self):
        return self.nome

class Imoveis(models.Model):
    cod_ref = models.CharField(max_length=5)
    preco = models.DecimalField(decimal_places=10, max_digits=20)
    descricao = models.TextField(max_length=1400)
    created_at = models.DateTimeField('date created')
    cidade = models.CharField(max_length=45)
    bairro = models.CharField(max_length=45)
    endereco = models.CharField(max_length=96)
    finalidade = models.ForeignKey(Finalidade)
    tipoimovel = models.ForeignKey(Tipoimovel)

    def __unicode__(self):
        return self.descricao