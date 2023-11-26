from django import forms
from .models import *

class UserDetailsForm(forms.ModelForm):
    BRANCH_CHOICES = (
        ('---select--', '---select--'),
        ('CSE', 'CSE'),
        ('ECE', 'ECE'),
        ('EEE', 'EEE'),
        ('Mechanical Engineering', 'Mechanical Engineering'),
        ('Civil Engineering', 'Civil Engineering'),
        ('NONE', 'NONE'),

    )


    COURSE_CHOICES = (
        ('---select--', '---select--'),
        ('B.TECH/BE', 'B.TECH/BE'),
        ('IT', 'IT'),
        ('AI/ML', 'AI/ML'),
        ('AI/DS', 'AI/DS'),
        ('MCA', 'MCA'),
        ('MBA', 'MBA'),
        ('Agriculture', 'Agriculture'),
    )

    GENDER_CHOICES=(
        ('--select--','--select--'),
        ('Male','Male'),
        ('Female','Female'),
        ('choose not to disclose','choose not to disclose'),
        
    )

    branch = forms.ChoiceField(choices=BRANCH_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    course = forms.ChoiceField(choices=COURSE_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    
    
    class Meta:
        model = UserDetails
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.TextInput(attrs={'class': 'form-control'}),
            
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone_number': forms.NumberInput(attrs={'class': 'form-control'}),
            
            'address': forms.Textarea(attrs={'class': 'form-control'}),
            
            'GPA': forms.NumberInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),  # Widget for the image field
            'rollno': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
        } 

class EditUserDetailsForm(forms.ModelForm):
    class Meta:
        model = UserDetails
        fields = ['first_name', 'last_name', 'gender', 'email', 'phone_number', 'address', 'course', 'branch', 'GPA', 'image', 'rollno', 'date_of_birth']

class StudentApplicationForm(forms.ModelForm):
    class Meta:
        model = StudentApplication
        fields = ('resume','experience','recommendation_letter') 

        
