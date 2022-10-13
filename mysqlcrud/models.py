from django.db import models
class Student(models.Model):
    name=models.CharField(max_length=20,default='')
    roll_number=models.IntegerField()
    address= models.CharField(max_length=20,default='')
    gender=models.CharField(max_length=20,default='')
    language=models.CharField(max_length=20)
# Create your models here.
