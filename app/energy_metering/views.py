from rest_framework import viewsets

from energy_metering.models import EnergyMetering
from energy_metering.serializers import EnergyMeteringSerializer, EnergyMeteringCreateSerializer


class EnergyMeteringViewSet(viewsets.ModelViewSet):
    """Energy metering information."""

    serializer_class = EnergyMeteringSerializer
    queryset = EnergyMetering.objects.all().select_related('power_meter')

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return EnergyMeteringSerializer
        return EnergyMeteringCreateSerializer
