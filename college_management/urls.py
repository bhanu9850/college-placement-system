from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_register, name='admin_register'),
    path('login/', views.admin_login, name='admin_login'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('add_student/', views.add_student, name='add_student'),
    path('logout/', views.logout_page, name='logout_page'),
    path('add_placement_drive/', views.add_placement_drive, name='add_placement_drive'),
    path('all_placement_drives/', views.all_placement_drives, name='all_placement_drives'),
    path('update_placement_drive/<int:placement_drive_id>/', views.update_placement_drive, name='update_placement_drive'),
    path('view_applied_students/', views.view_applied_students, name='view_applied_students'),
    path('delete_placement_drive/<int:placement_drive_id>/', views.delete_placement_drive, name='delete_placement_drive'),
]
