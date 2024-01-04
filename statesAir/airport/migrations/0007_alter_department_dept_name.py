# Generated by Django 5.0 on 2024-01-02 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airport', '0006_remove_crew_crew_staff_crew_crew_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='dept_name',
            field=models.TextField(choices=[('Pilot', 'Pilot'), ('Flight Attendant', 'Flight Attendant'), ('Mechanic', 'Mechanic'), ('Ground Crew', 'Ground Crew'), ('Concessions', 'Concessions'), ('Janitor', 'Janitor'), ('Security', 'Security'), ('Admin', 'Admin')], default='Admin', unique=True),
        ),
    ]
