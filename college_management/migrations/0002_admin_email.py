# Generated by Django 3.0.5 on 2023-11-06 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college_management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin',
            name='email',
            field=models.EmailField(default='email@gmail.com', max_length=100),
        ),
    ]
