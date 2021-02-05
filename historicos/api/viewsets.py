from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from historicos.api.serializers import HistoricosSerializer
from historicos.api.serializers import HistoricosDetalhesSerializer
from historicos.models import Historicos


class HistoricosViewSet(viewsets.ModelViewSet):
    queryset = Historicos.objects.all().order_by('historico_date')
    serializer_class = HistoricosSerializer

    @action(detail=True, methods=['get'])
    def detalhes(self, request, pk=None, *args, **kwargs):
        queryset = Historicos.objects.filter(pk=pk)
        self.serializer_class = HistoricosDetalhesSerializer
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
