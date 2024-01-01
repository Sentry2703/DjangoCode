# Generated by Django 5.0 on 2023-12-31 01:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('airport', '0002_department_department_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='crew',
            old_name='employees',
            new_name='crew_staff',
        ),
        migrations.RenameField(
            model_name='department',
            old_name='department_id',
            new_name='dept_id',
        ),
        migrations.RenameField(
            model_name='department',
            old_name='department_location',
            new_name='dept_location',
        ),
        migrations.RenameField(
            model_name='department',
            old_name='department_name',
            new_name='dept_name',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='employment_date',
            new_name='emp_date',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='employee_fname',
            new_name='emp_fname',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='employee_id',
            new_name='emp_id',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='employee_lname',
            new_name='emp_lname',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='employee_role',
            new_name='emp_role',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='salary',
            new_name='emp_sal',
        ),
    ]