from django import forms
from .models import *

class AdminRegistrationForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = ('username', 'password', 'email')  


class PlacementDriveForm(forms.ModelForm):
    class Meta:
        model = PlacementDrive
        fields = ('company','title','description','date')
    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        input_formats=['%Y-%m-%d', '%m/%d/%Y', '%m/%d/%y', '%b %d %Y', '%B %d, %Y'],
    )    


class Update_Placement_Drive(forms.ModelForm):
    class Meta:
        model = PlacementDrive
        fields = ('company','title','description','date')