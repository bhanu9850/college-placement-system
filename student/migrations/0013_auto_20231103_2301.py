# Generated by Django 3.0.5 on 2023-11-03 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0012_remove_student_dob'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdetails',
            name='DOB',
        ),
        migrations.RemoveField(
            model_name='userdetails',
            name='Roll_no',
        ),
        migrations.RemoveField(
            model_name='userdetails',
            name='image',
        ),
    ]
