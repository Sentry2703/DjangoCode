# Generated by Django 5.0 on 2024-01-04 04:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airport', '0009_alter_plane_plane_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='flight_crew',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='airport.crew'),
        ),
    ]