# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 14:17:08 2023

@author: felix
"""

from django.urls import path
from . import views

urlpatterns = [
    path('choose-character/', views.choose_character, name='choose_character'),
    # Fügen Sie hier weitere URL-Muster für Ihre App hinzu
    #path('kalendar/', views.kalendar, name='kalendar'),
    path('advent_calendar/', views.advent_calendar, name='advent_calendar'),
    path('advent_day/<int:day>/', views.advent_day, name='advent_day'),
    path('chat/', views.chat_view, name='chat'),
    path('chat/send/', views.send_message, name='send_message'),
    path('chat/messages/', views.get_chat_messages, name='get_chat_messages'),
    path('end-session/', views.end_session, name='end_session'),
    path('reset-character/<int:character_id>/', views.reset_character, name='reset_character'),
    path('decision/<int:decision_id>/', views.decision_view, name='decision_view'),
    path('vote/<int:decision_id>/', views.vote, name='vote'),
    path('reset-game/', views.reset_game, name='reset_game'),
    path('join_game/', views.join_game, name='join_game'),
    path('snowball_fight/', views.snowball_fight, name='snowball_fight'),
    path('tree/', views.tree_view, name='tree_view'),
    path('update_character/', views.update_character, name='update_character'),
    path('labyrinth/<int:labyrinth_id>/', views.labyrinth_view, name='labyrinth_view'),
    path('vote_lab/<int:labyrinth_id>/', views.vote_lab, name='vote_lab'),
    path('reset_game_lab/', views.reset_game_lab, name='reset_game_lab'),
    path('join_game_lab/', views.join_game_lab, name='join_game_lab'),
    path('kuehlschrank/<int:tag>/', views.kuehlschrank, name='kuehlschrank'),
    path("update_position/", views.update_position, name="update_position"),
    path('erstelle_notizzettel/<int:tag>/', views.erstelle_notizzettel, name='erstelle_notizzettel'),
    path('lade_bild_hoch/<int:tag>/', views.lade_bild_hoch, name='lade_bild_hoch'),
    path('advent_kerze/', views.advent_kerze, name='advent_kerze'),
    path('start_labyrinth_choice/', views.start_labyrinth_choice, name='start_labyrinth_choice'),
]
