# Generated by Django 3.0.5 on 2023-11-03 06:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_remove_userdetails_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetails',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='student.Student'),
        ),
    ]