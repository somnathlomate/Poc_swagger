from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.


def validate_names(value):
    if type(value)==str and len(value)>=5:
        return value
    else:
        raise ValidationError("Invalid Name..!")


def validate_emails(value):
    if type(value)==str and len(value)>=11 and "@gmail.com":      #s@ab.in
        return value
    else:
        raise ValidationError("Invalid Name..!")


'''


phone_regex = RegexValidator(regex=r'^[6-9][0-9]{9}$', message="Please Enter Valid Mobile No.")
phone = models.CharField(validators=[phone_regex], max_length=10, unique=True)

'''


class Employee(models.Model):
    name = models.CharField(max_length=30,validators=[validate_names])
    age = models.IntegerField()
    email = models.CharField(max_length=30, unique=True,validators=[validate_emails])
    role = models.CharField(max_length=30, default='Guest')
    phone_num = models.BigIntegerField(unique=True)
    joiningDate = models.DateField()
    address = models.CharField(max_length=255, default='Y')

    class Meta:
        db_table = 'EMPLOYEE_MASTER'
        ordering = ['role']  # select * from employee_master order by role desc
