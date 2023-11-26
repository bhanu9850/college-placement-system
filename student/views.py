from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import *
from django.shortcuts import render, redirect,HttpResponse,get_object_or_404
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .forms import *
from college_management.models import *
  
def home(request):
    return render(request,'home.html')

def register_student(request):
    if request.method == 'POST':
            first_name =request.POST.get('first_name')
            last_name =request.POST.get('last_name')
            username =request.POST.get('username')
            password = request.POST.get('password')

            user = User.objects.filter(username=username)
            if user.exists():
                messages.info(request,'username already taken')
                return redirect('/register_student/')
            
            student = User.objects.create(
                username = username,
                first_name = first_name,
                last_name = last_name)
            student.set_password(password)
            student.save()
            messages.info(request,'account created successfully')
            
    return render(request,'register_student.html')    

def login_page(request):
    if request.method == 'POST':
            username =request.POST.get('username')
            password = request.POST.get('password')
            if not User.objects.filter(username = username).exists():
                messages.error(request,'Invalid Username')  
            user = authenticate(username =username,password=password)
            if user is None:
                messages.error(request,'Incorrect Password')
                return redirect('login')
            else:
                login(request,user) 
                return render(request,'home.html')

    return render(request,'login.html')
@login_required
def logout_page(request): 
    logout(request)
    return redirect('login')
@login_required
def enter_details(request):
    if request.method == 'POST':
        form = UserDetailsForm(request.POST)
        if form.is_valid():
            user_details = form.save(commit=False)
            user_details.user = request.user
            user_details.save()
            return redirect('student_dashboard')

    else:
        form = UserDetailsForm()

    return render(request, 'enter_details.html', {'form': form})
@login_required
def student_dashboard(request):
    username = request.user.username
    user_details = UserDetails.objects.filter(user__username=username)
    drives = PlacementDrive.objects.all()
    return render(request, 'dashboard.html', {'user_details': user_details,'drives': drives})       
@login_required
def edit_details(request):
    user = UserDetails.objects.get(user=request.user)
    if request.method == 'POST':
        form = EditUserDetailsForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('student_dashboard')
    else:
        form = EditUserDetailsForm(instance=user)

    return render(request, 'edit_details.html', {'form': form})

@login_required
def apply_to_drive(request, placement_drive_id):
    drive = get_object_or_404(PlacementDrive, id=placement_drive_id)
    student = request.user

    
    if StudentApplication.objects.filter(student=student, placement_drive=drive).exists():
        messages.info(request,"you've already applied to this role")
        return redirect('student_dashboard')
        
    else:
        if request.method == 'POST':
            form = StudentApplicationForm(request.POST, request.FILES)
            if form.is_valid():
                application = form.save(commit=False)
                application.student = student
                application.placement_drive = drive
                application.save()
                return redirect('student_dashboard')
        else:
            form = StudentApplicationForm()

    return render(request, 'apply_to_drive.html', {'form': form, 'drive': drive})