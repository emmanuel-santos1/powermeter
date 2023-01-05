import re
from django.core import validators
from django.db import models
from django.utils.translation import gettext_lazy as _


class PowerMeter(models.Model):
    key = models.CharField(
        max_length=200,
        unique=True,
        validators=[
            validators.RegexValidator(
                re.compile('^[a-zA-Z0-9]+$'),
                _('Enter a valid key.'),
                'invalid')
        ])
    name = models.CharField(max_length=1000)
