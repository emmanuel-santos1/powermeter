from rest_framework import serializers

from power_meter.models import PowerMeter


class PowerMeterSerializer(serializers.ModelSerializer):

    class Meta:
        model = PowerMeter
        fields = [
            'id', 'key', 'name'
        ]