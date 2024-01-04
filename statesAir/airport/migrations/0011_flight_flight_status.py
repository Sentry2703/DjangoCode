# Generated by Django 5.0 on 2024-01-04 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airport', '0010_flight_flight_crew'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='flight_status',
            field=models.TextField(choices=[('On Time', 'On Time'), ('Delayed', 'Delayed'), ('Cancelled', 'Cancelled')], default='On Time'),
        ),
    ]