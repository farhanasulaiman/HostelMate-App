from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
# login model
class Login(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_parent = models.BooleanField(default=False)


# student sign up model
class Student(models.Model):
    user = models.ForeignKey('Login', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(max_length=10)
    address = models.TextField(max_length=100)
    department = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    email = models.EmailField()
    regno = models.CharField(max_length=50)
    photo = models.FileField(upload_to='documents/')

    # parent can choose the reg no from the dropdown
    def __str__(self):
        return f'{self.regno} {self.name}'


# parent sign up model
class Parent(models.Model):
    user = models.ForeignKey('Login', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    relation = models.CharField(max_length=10)
    address = models.TextField(max_length=100)
    regno = models.ForeignKey('Student', on_delete=models.DO_NOTHING)  # connect parent to student using regno
    phone = models.CharField(max_length=12)
    email = models.EmailField()
