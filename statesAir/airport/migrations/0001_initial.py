# Generated by Django 5.0 on 2023-12-31 00:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('department_id', models.IntegerField(primary_key=True, serialize=False)),
                ('department_location', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Plane',
            fields=[
                ('plane_id', models.IntegerField(primary_key=True, serialize=False)),
                ('capacity', models.IntegerField()),
                ('plane_status', models.CharField(max_length=50)),
                ('plane_airline', models.CharField(max_length=50)),
                ('commission_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employee_id', models.IntegerField(primary_key=True, serialize=False)),
                ('employee_fname', models.CharField(max_length=20)),
                ('employee_lname', models.CharField(max_length=20)),
                ('employment_date', models.DateField()),
                ('salary', models.IntegerField()),
                ('employee_role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='airport.department')),
            ],
        ),
        migrations.CreateModel(
            name='Crew',
            fields=[
                ('crew_id', models.IntegerField(primary_key=True, serialize=False)),
                ('employees', models.ManyToManyField(to='airport.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('flight_id', models.IntegerField(primary_key=True, serialize=False)),
                ('flight_origin', models.CharField(max_length=50)),
                ('flight_destination', models.CharField(max_length=50)),
                ('flight_departure', models.DateTimeField()),
                ('flight_arrival', models.DateTimeField()),
                ('flight_plane', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='airport.plane')),
            ],
        ),
    ]
