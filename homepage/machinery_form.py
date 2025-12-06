from django import forms
from .models import *

class MachineryForm(forms.ModelForm):
    class Meta:
        model=Machinery
        fields= '__all__'

class Machinery_activitesForm(forms.ModelForm):
    class Meta:
        model=Machinery_activities
        fields=[
            'Activity_date',
            'Activity_type',
            'Activity_cost',
            'Description'
        ]

class Machinery_maintenanceForm(forms.ModelForm):
    class Meta:
        model=Machinery_maintenance
        fields=[
            'Date',
            'Machinery_part',
            'Technician_details',
            'Cost',
            'Description'
        ]