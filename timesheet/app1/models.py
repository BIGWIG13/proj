from django.db import models




# Create your models here.


class tbl_emp(models.Model):
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    designation=models.CharField(max_length=30)
    salary=models.IntegerField()
    department=models.CharField(max_length=30)
    place=models.CharField(max_length=30)
    phone=models.IntegerField()
    email=models.CharField(max_length=30)
    class meta:
        db_table="tbl_emp"

class project(models.Model):
    project_name=models.CharField(max_length=50)
    topic=models.CharField(max_length=50)
    comments=models.CharField(max_length=100)
    class meta:
        db_table="project"

class Assigned_project(models.Model):
    project_id=models.CharField(max_length=100)
    employee_id=models.CharField(max_length=100)
    start_time=models.CharField(max_length=100)
    end_time=models.CharField(max_length=100)
    status=models.CharField(max_length=100)
    class meta:
        db_table="Assigned_project"

class report(models.Model):
    project_id=models.CharField(max_length=100)
    employee_id=models.CharField(max_length=100)
    report_time=models.CharField(max_length=100)
    status=models.CharField(max_length=100)
    class meta:
        db_table="report"

              

