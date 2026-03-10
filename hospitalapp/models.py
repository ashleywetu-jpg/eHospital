from django.db import models
__all__ = ['Mypatients', 'Mydoctors', 'Myappointments']

# Create your models here.

class Mypatients(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    dob = models.DateField()
    datetime = models.DateTimeField()
    medical_history = models.TextField()
    age = models.IntegerField()

    def __str__(self):
        return self.name

class Mydoctors(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    dob = models.DateField()
    datetime = models.DateTimeField()
    specialization = models.CharField(max_length=100)
    experience = models.IntegerField()

    def __str__(self):
        return self.name       

    
class Myappointments(models.Model):     
    name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField()
    datetime = models.DateTimeField()
    department = models.CharField(max_length=20)
    doctor = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return self.name

    