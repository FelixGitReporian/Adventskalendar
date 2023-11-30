# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 21:00:17 2023

@author: felix
"""

from django.utils import timezone
from django.conf import settings
from datetime import datetime
from django.shortcuts import redirect
from .models import Character  # Importieren Sie Ihr Character-Modell

class ResetCharacterMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        self.update_last_activity(request)
        response = self.get_response(request)
        return response

    def update_last_activity(self, request):
        
        if request.path not in ['/advent/chat/messages/', '/andere/pfade/zum/ignorieren']:
            request.session['last_activity'] = timezone.now().isoformat()

        if 'selected_character_id' in request.session and 'last_activity' in request.session:
            last_activity = timezone.datetime.fromisoformat(request.session['last_activity'])
            print(settings.SESSION_COOKIE_AGE - (timezone.now() - last_activity).total_seconds()+settings.SESSION_COOKIE_AGE*0.25)
            if ((timezone.now() - last_activity).total_seconds()+settings.SESSION_COOKIE_AGE*0.25) > settings.SESSION_COOKIE_AGE:
                print("gleich isses soweit___________________________________________")
                character_id = request.session.pop('selected_character_id', None)
                Character.objects.filter(id=character_id).update(is_taken=False)
                # Keine Notwendigkeit für eine Umleitung hier, da die Middleware auf jeden Request angewendet wird




