# Generated by Django 5.0 on 2023-12-31 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airport', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='department_name',
            field=models.TextField(choices=[('Pilot', 'Pilot'), ('FlightAttendant', 'Flight Attendant'), ('Mechanic', 'Mechanic'), ('GroundCrew', 'Ground Crew'), ('Concessions', 'Concessions'), ('Janitor', 'Janitor'), ('Security', 'Security'), ('Admin', 'Admin')], default='Admin'),
        ),
    ]