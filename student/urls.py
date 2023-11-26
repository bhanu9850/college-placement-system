from student import views
from django.urls import path
 

urlpatterns = [
    path('', views.home,name="home"),
    path('register/', views.register_student,name="register_student"),
    path('login/', views.login_page,name="login"),
    path('logout/', views.logout_page,name="logout"),
    path('enter_details/', views.enter_details, name='enter_details'),
    path('student_dashboard/',views.student_dashboard,name='student_dashboard'),
    path('edit_details/',views.edit_details,name='edit_details'),
    path('apply_to_drive/<int:placement_drive_id>/', views.apply_to_drive, name='apply_to_drive'),
    ]