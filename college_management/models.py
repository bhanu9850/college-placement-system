from django.db import models
from student.models import *


class Admin(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,default="email@gmail.com")



class PlacementDrive(models.Model):
    company = models.CharField(max_length=255,default="xyz")
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    
    
    @classmethod
    def get_all_drives(cls):
        return cls.objects.all()

    def get_applications(self):
        return self.studentapplication_set.all()




