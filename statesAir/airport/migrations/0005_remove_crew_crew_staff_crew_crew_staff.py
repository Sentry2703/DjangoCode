# Generated by Django 5.0 on 2024-01-01 03:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airport', '0004_alter_department_dept_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='crew',
            name='crew_staff',
        ),
        migrations.AddField(
            model_name='crew',
            name='crew_staff',
            field=models.ForeignKey(default=2, limit_choices_to={'emp_role__dept_name': 'FlightAttendant'}, on_delete=django.db.models.deletion.PROTECT, to='airport.employee'),
            preserve_default=False,
        ),
    ]
