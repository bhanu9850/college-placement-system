# Generated by Django 3.0.5 on 2023-11-21 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college_management', '0004_auto_20231121_1602'),
    ]

    operations = [
        migrations.AddField(
            model_name='placementdrive',
            name='company',
            field=models.CharField(default='xyz', max_length=255),
        ),
    ]
