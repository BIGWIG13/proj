# Generated by Django 5.0 on 2024-01-13 09:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_tbl_emp_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tbl_emp',
            name='gender',
        ),
    ]
