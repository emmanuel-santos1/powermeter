# Generated by Django 4.1.5 on 2023-01-05 20:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('power_meter', '0001_initial'),
        ('energy_metering', '0002_alter_energymetering_energy_use'),
    ]

    operations = [
        migrations.AlterField(
            model_name='energymetering',
            name='power_meter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='energy_meterings', to='power_meter.powermeter'),
        ),
    ]
