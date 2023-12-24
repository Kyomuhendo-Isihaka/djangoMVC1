from django.db import models

# Create your models here.
class Student(models.Model):
    stdName = models.CharField(max_length=255)
    stdAge = models.CharField(max_length=100)
    stdCourse = models.CharField(max_length=100)

class Account(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField()
    password= models.CharField(max_length=255)
    birthdate = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name
    

   

