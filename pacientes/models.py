from django.db import models
from django.db.models import AutoField, CharField


class Pacientes(models.Model):
    paciente_id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    data_nasc = models.DateTimeField(blank=True, null=True)
    endereco = models.CharField(max_length=80, blank=True, null=True)
    endereco_num = models.CharField(max_length=10, blank=True, null=True)
    endereco_bairro = models.CharField(max_length=60, blank=True, null=True)
    cep = models.CharField(max_length=100, blank=True, null=True)
    cadastro_date = models.DateTimeField(auto_now_add=True)
    rg = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'pacientes'
