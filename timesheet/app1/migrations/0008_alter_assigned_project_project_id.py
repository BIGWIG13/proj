# Generated by Django 4.0.4 on 2023-12-28 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_alter_assigned_project_employee_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assigned_project',
            name='project_id',
            field=models.CharField(max_length=100),
        ),
    ]
