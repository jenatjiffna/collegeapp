
from django.db import models


# Create your models here.
class Center(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Subcenter(models.Model):
    center = models.ForeignKey(Center, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Course1(models.Model):
    name=models.CharField(max_length=250)
    def __str__(self):
        return self.name

class Total_fees(models.Model):
    name=models.CharField(max_length=250)
    course1= models.ForeignKey(Course1, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Student1(models.Model):
    name = models.CharField(max_length=100)
    birthdate = models.DateField(null=True, blank=True)
    gender=models.CharField(max_length=250)
    blood_group=models.CharField(max_length=250)
    mail_id=models.EmailField(blank=False)
    address=models.TextField(blank=False)
    course1=models.ForeignKey(Course1, on_delete=models.SET_NULL, null=True)
    total_fees=models.ForeignKey(Total_fees, on_delete=models.SET_NULL, null=True)
    center = models.ForeignKey(Center, on_delete=models.SET_NULL, null=True)
    subcenter = models.ForeignKey(Subcenter, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name