from decimal import Decimal
from django.db.models import Sum, Avg
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from power_meter.models import PowerMeter
from power_meter.serializers import PowerMeterSerializer
from energy_metering.serializers import EnergyMeteringSerializer


class PowerMeterViewSet(viewsets.ModelViewSet):
    """Power meter information."""

    serializer_class = PowerMeterSerializer
    queryset = PowerMeter.objects.all().prefetch_related("energy_meterings")

    @action(methods=['get'], detail=True, url_path="maximum-measurement")
    def maximum_measurement(self, *args, **kwargs):
        self.object = self.get_object()
        max_measurement = self.object.energy_meterings.order_by('-energy_use').first()
        return Response(EnergyMeteringSerializer(max_measurement).data)


    @action(methods=['get'], detail=True, url_path="minimum-measurement")
    def minimum_measurement(self, *args, **kwargs):
        self.object = self.get_object()
        min_measurement = self.object.energy_meterings.order_by('energy_use').first()
        return Response(EnergyMeteringSerializer(min_measurement).data)

    @action(methods=['get'], detail=True, url_path="total-use")
    def total_use(self, *args, **kwargs):
        self.object = self.get_object()
        total_use = self.object.energy_meterings.aggregate(
            total_use=Sum('energy_use')
        ).get('total_use') or Decimal('0')
        return Response({"total_use": total_use})

    @action(methods=['get'], detail=True, url_path="average-use")
    def average_use(self, *args, **kwargs):
        self.object = self.get_object()
        avg_use = self.object.energy_meterings.aggregate(
            avg_use=Avg('energy_use')
        ).get('avg_use') or Decimal('0')
        return Response({"average_use": avg_use})
