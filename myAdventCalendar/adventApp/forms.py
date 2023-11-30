# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 19:33:20 2023

@author: felix
"""

from django import forms
from .models import Notizzettel, Bild

#class RegistrationForm(forms.Form):
#    character_id = forms.IntegerField(widget=forms.HiddenInput())
#    password = forms.CharField(widget=forms.PasswordInput())
    
class RegistrationLoginForm(forms.Form):
    character_id = forms.IntegerField(widget=forms.HiddenInput())
    password = forms.CharField(widget=forms.PasswordInput())
    is_login = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput())
    
    
class NotizzettelForm(forms.ModelForm):
    class Meta:
        model = Notizzettel
        fields = ['titel', 'inhalt', 'character', 'x_position', 'y_position']

class BildForm(forms.ModelForm):
    class Meta:
        model = Bild
        fields = ['titel', 'bild', 'character', 'x_position', 'y_position']
