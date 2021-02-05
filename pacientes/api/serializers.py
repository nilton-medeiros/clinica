from rest_framework import serializers

from pacientes.models import Pacientes
from agendamentos.api.serializers import AgendamentosDetalhesSerializer


class PacientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pacientes
        fields = "__all__"


class PacientesDetalhesSerializer(serializers.ModelSerializer):
    agendamentos = AgendamentosDetalhesSerializer(many=True, read_only=True)

    class Meta:
        model = Pacientes
        fields = [
            'paciente_id',
            'nome',
            'data_nasc',
            'endereco',
            'endereco_num',
            'endereco_bairro',
            'cep',
            'cadastro_date',
            'rg',
            'agendamentos'
        ]
