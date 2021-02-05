from django.db import models
from historicos.models import Historicos


def imagens_historico(instance, filename):
    return '/'.join(['historico', str(instance.historico_id.historico_id), filename])


class ImagensHistorico(models.Model):
    imagem_historico_id = models.AutoField(primary_key=True)
    imagem = models.ImageField(blank=True, null=True, upload_to=imagens_historico)
    historico_id = models.ForeignKey(Historicos, related_name='imagens', on_delete=models.CASCADE, blank=False, null=False)
