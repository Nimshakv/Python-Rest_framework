from django.db import models


class DeptNew(models.Model):
    # department_id = models.IntegerField()
    name = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=200)

    def __str__(self):
        return '__all__'


class EmpNew(models.Model):
    # emp_id = models.CharField(max_length=5, primary_key=True)
    name = models.CharField(max_length=200, unique=True)
    department_id = models.ForeignKey(DeptNew, on_delete=models.CASCADE)
    dob = models.DateField()

    def __str__(self):
        return '__all__'
