from rest_framework import serializers

from energy_metering.models import EnergyMetering


class EnergyMeteringSerializer(serializers.ModelSerializer):
    power_meter_key = serializers.CharField(source='power_meter.key')
    power_meter_name = serializers.CharField(source='power_meter.name')

    class Meta:
        model = EnergyMetering
        fields = [
            'id', 'measurement_time', 'energy_use',
            'power_meter_key', 'power_meter_name'
        ]


class EnergyMeteringCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnergyMetering
        fields = [
            'id', 'measurement_time', 'energy_use', 'power_meter'
        ]