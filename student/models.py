from django.db import models
from django.contrib.auth.models import User
import datetime 
from college_management.models import * 

class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
   
        
    
class UserDetails(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    first_name = models.CharField(max_length=255)    
    last_name = models.CharField(max_length=255)  
    gender = models.CharField(max_length=10,null=True)  
    
    email = models.EmailField(max_length=255)
    phone_number = models.CharField(max_length=10)
    address = models.TextField()
    
    course = models.CharField(max_length=255)
    branch= models.CharField(max_length=255)
    
    GPA = models.DecimalField(max_digits=3, decimal_places=2)
    image = models.ImageField(upload_to='student_images/',null=True, blank=True)  # For storing student images.
    rollno = models.CharField(max_length=20,null=True)  # Adjust the max_length as needed.
    date_of_birth = models.DateField(default=datetime.date.today)
    
    

    def __str__(self):
        return self.first_name
      

class StudentApplication(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    placement_drive = models.ForeignKey(PlacementDrive, on_delete=models.CASCADE)
    date_applied = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    resume = models.FileField(upload_to ='uploads/')
    experience = models.CharField(max_length=255, blank=True, null=True)
    recommendation_letter = models.FileField(upload_to='uploads/', blank=True, null=True)

    def __str__(self):
        return f"{self.student.username} - {self.placement_drive.title}"