#from django.db import models
#from randomuser import RandomUser
#import pandas as pd

# Create your models here.
from django.contrib.auth.models import User
from django.db import models
import random

class Character(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='characters/')  # Stellen Sie sicher, dass Pillow installiert ist
    background_text = models.TextField()
    is_taken = models.BooleanField(default=False)
    snowballs = models.IntegerField(default=5)
    #hits_received = models.IntegerField(default=0)  # Zählt, wie oft der Charakter getroffen wurde


    def __str__(self):
        return self.name
    
    def throw_snowball(self, target):
        if self.snowballs > 0:
            self.snowballs -= 1
            self.save()
            hit = target.get_hit()
            if hit:
                # Erstellen eines SnowballHit Datensatzes
                SnowballHit.objects.create(attacker=self, target=target)
            return hit
        return False

    def get_hit(self):
        # 80% Chance, getroffen zu werden
        return random.randint(1, 100) <= 80

class SnowballHit(models.Model):
    attacker = models.ForeignKey(Character, related_name='attacks_made', on_delete=models.CASCADE)
    target = models.ForeignKey(Character, related_name='hits_received', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    


class Ornament(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    position_x = models.IntegerField(default=0)
    position_y = models.IntegerField(default=0)
    # Weitere Attribute ...

class Gift(models.Model):
    sender = models.ForeignKey(Character, related_name='sent_gifts', on_delete=models.CASCADE)
    receiver = models.ForeignKey(Character, related_name='received_gifts', on_delete=models.CASCADE)
    position_x = models.IntegerField(default=0)
    position_y = models.IntegerField(default=0)
    note = models.TextField()
    # Weitere Attribute ...


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #pseudonym = models.CharField(max_length=100)
    character = models.ForeignKey(Character, on_delete=models.SET_NULL, null=True)
    # Weitere Felder nach Bedarf

class AdventNumber(models.Model):
    day = models.IntegerField(unique=True)
    position_x = models.IntegerField()
    position_y = models.IntegerField()
    rotation = models.IntegerField(default=0)  # Speichert die Rotation in Grad
    color = models.CharField(max_length=7, default="#FFFFFF")  # Speichert die Farbe

    def __str__(self):
        return f"Tag {self.day} - Position ({self.position_x}, {self.position_y})"
    

class ChatMessage(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.character.name}: {self.message[:50]}"
    

class Decision(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    background_image = models.ImageField(upload_to='decisions/')
    next_decision_a = models.ForeignKey('self', related_name='+', null=True, blank=True, on_delete=models.SET_NULL)
    next_decision_b = models.ForeignKey('self', related_name='+', null=True, blank=True, on_delete=models.SET_NULL)
    start_time = models.DateTimeField(auto_now_add=True)
    # weitere Felder...


class Vote(models.Model):
    decision = models.ForeignKey(Decision, on_delete=models.CASCADE)
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    choice = models.CharField(max_length=100)  # Zum Beispiel "Wald" oder "Tundra"
    
class Labyrinth(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    background_image = models.ImageField(upload_to='labyrinths/')
    next_labyrinth_a = models.ForeignKey('self', related_name='+', null=True, blank=True, on_delete=models.SET_NULL)
    next_labyrinth_b = models.ForeignKey('self', related_name='+', null=True, blank=True, on_delete=models.SET_NULL)
    possessed_character = models.ForeignKey(Character, on_delete=models.SET_NULL, null=True, blank=True, related_name='possessed_in_labyrinth')
    start_time = models.DateTimeField(auto_now_add=True)
    
    def is_character_possessed(self, character):
        return self.possessed_character == character
    
class Vote_lab(models.Model):
    labyrinth = models.ForeignKey(Labyrinth, on_delete=models.CASCADE)
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    choice = models.CharField(max_length=100)
    

class Notizzettel(models.Model):
    titel = models.CharField(max_length=100)
    inhalt = models.TextField()
    erstellungsdatum = models.DateTimeField(auto_now_add=True)
    x_position = models.IntegerField(default=0)
    y_position = models.IntegerField(default=0)
    tag = models.IntegerField(default=0)
    character = models.ForeignKey(Character, on_delete=models.SET_NULL, null=True, blank=True, related_name='notizzettel_character')  # Geänderter related_name    


class Bild(models.Model):
    titel = models.CharField(max_length=100)
    bild = models.ImageField(upload_to='bilder/')
    hochladedatum = models.DateTimeField(auto_now_add=True)
    x_position = models.IntegerField(default=0)
    y_position = models.IntegerField(default=0)
    tag = models.IntegerField(default=0)
    character = models.ForeignKey(Character, on_delete=models.SET_NULL, null=True, blank=True, related_name='bild_character')  # Geänderter related_name


class Tagesnachricht(models.Model):
    tag = models.IntegerField(unique=True)
    nachricht = models.TextField()
    


    
    

