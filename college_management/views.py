from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import *
from student.views import *
from student.models import *
from .models import *

def admin_register(request):
    if request.method == 'POST':
        form = AdminRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_login')
            
    else:
        form = AdminRegistrationForm()
    return render(request, 'admin_register.html', {'form': form})

    


def admin_login(request):
    if request.method == 'POST':
        username =request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('admin_dashboard')
        else:
            messages.error(request, 'Invalid username or password. Please try again.')

    return render(request, 'admin_login.html')


@login_required
def admin_dashboard(request):
    users = UserDetails.objects.all()
    

    if request.method == 'POST':
        if 'delete_student' in request.POST:
            user_id = request.POST.get('delete_student')
            try:
                user_to_delete = UserDetails.objects.get(pk=user_id)
                user_to_delete.delete()
                messages.success(request, 'Student deleted successfully.')
                return redirect('admin_dashboard')
            except UserDetails.DoesNotExist:
                messages.error(request, 'Student not found.')

        
    return render(request, 'admin_dashboard.html',{'users': users})
@login_required
def logout_page(request): 
    logout(request)
    return redirect('/login/')    
@login_required
def add_student(request):
    if request.method == 'POST':
        add_student_form = UserDetailsForm(request.POST)
        if add_student_form.is_valid():
            add_student_form.save()
            messages.success(request, 'Student added successfully.')
            return redirect('admin_dashboard')
        else:
            messages.error(request, 'Error adding student. Please check the form.')
            print(add_student_form.errors)

    else:
        add_student_form = UserDetailsForm()
        print(add_student_form.errors)
    users = UserDetails.objects.all()
    return render(request, 'admin_dashboard.html', {'users': users, 'add_student_form': add_student_form})   

@login_required
def add_placement_drive(request):
    if request.method == 'POST':
        form = PlacementDriveForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Placement drive added successfully.')
            return redirect('admin_dashboard')
    else:
        form = PlacementDriveForm()    
    return render(request,'add_placement_drive.html',{'form': form})


@login_required
def all_placement_drives(request):
    drives = PlacementDrive.get_all_drives()
    return render(request, 'all_placement_drives.html', {'drives': drives})
@login_required
def update_placement_drive(request, placement_drive_id):
    placement_drive = get_object_or_404(PlacementDrive, id=placement_drive_id)
    if request.method == 'POST':
        form = PlacementDriveForm(request.POST, instance=placement_drive)
        if form.is_valid():
            form.save()
            messages.info(request, 'Placement Drive updated successfully!')
            return redirect('all_placement_drives')
    else:
        form = PlacementDriveForm(instance=placement_drive)

    return render(request, 'update_placement_drive.html',{'form': form, 'placement_drive': placement_drive})

def delete_placement_drive(request, placement_drive_id):
    placement_drive = get_object_or_404(PlacementDrive, id=placement_drive_id)
    placement_drive.studentapplication_set.all().delete()
    placement_drive.delete()
    messages.success(request,"placement drive deleted succesfully")
    return redirect('admin_dashboard')  
        

def view_applied_students(request):
    drives = PlacementDrive.get_all_drives()
    drives_with_students = []
    for drive in drives:
        students_applied = drive.get_applications()
        drives_with_students.append({'drive': drive, 'students_applied': students_applied})
    return render(request,'view_applied_students.html',{'drives_with_students':drives_with_students})