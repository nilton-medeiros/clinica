from django.db import models
from django.db.models import DateTimeField

from agendamentos.models import Agendamentos


class Historicos(models.Model):
    historico_id = models.AutoField(primary_key=True)
    historico_date: DateTimeField = models.DateTimeField(auto_now_add=True)
    aparecimentos_sintomas = models.CharField(max_length=100, blank=True, null=True)
    duracao_sintomas = models.CharField(max_length=100, blank=True, null=True)
    local_dor = models.CharField(max_length=100, blank=True, null=True)
    tipo_dor = models.CharField(max_length=100, blank=True, null=True)
    conclusao = models.TextField(blank=True, null=True)
    agendamento_id = models.ForeignKey(Agendamentos, related_name='historicos', on_delete=models.CASCADE, blank=False, null=False)

    class Meta:
        managed = True
        db_table = 'historicos'
