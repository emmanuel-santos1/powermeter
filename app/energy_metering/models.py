from datetime import datetime
from decimal import Decimal
from django.db import models
from django.core.validators import MinValueValidator


class EnergyMetering(models.Model):
    power_meter = models.ForeignKey(
        "power_meter.PowerMeter",
        on_delete=models.CASCADE,
        related_name="energy_meterings"
    )
    measurement_time = models.DateTimeField(default=datetime.now)
    energy_use = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])
