from django.db import models
import uuid

# Create your models here.
class Employee(models.Model):
    emp_id = models.IntegerField(primary_key=True)
    emp_name = models.CharField(max_length=200)
    emp_email = models.EmailField()
    emp_contact = models.CharField(max_length=10)
    emp_role = models.CharField(max_length=200)
    emp_salary = models.IntegerField()
    def __str__(self):
        return self.emp_name
