from django import forms
from django.forms import fields
from .models import AnnouncedPuResults,AnnouncedLgaResults,Agentname,AnnouncedStateResults,AnnouncedWardResults, New_Polling_unit

class AddPolls(forms.ModelForm):

    class Meta:
        model = AnnouncedPuResults
        fields = ['polling_unit_uniqueid']

class NewPollingUnit(forms.ModelForm):

    class Meta:
        model =  New_Polling_unit
        fields = '__all__'