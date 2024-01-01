# Generated by Django 5.0 on 2024-01-01 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airport', '0005_remove_crew_crew_staff_crew_crew_staff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='crew',
            name='crew_staff',
        ),
        migrations.AddField(
            model_name='crew',
            name='crew_staff',
            field=models.ManyToManyField(limit_choices_to={'emp_role__dept_name': 'FlightAttendant'}, to='airport.employee'),
        ),
    ]
