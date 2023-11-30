from django.contrib import admin
from .models import Character, UserProfile
from django.contrib.auth.models import User
from .models import AdventNumber
from .models import ChatMessage
from .models import Decision
from .models import Vote
from .models import SnowballHit
from .models import Labyrinth
from .models import Notizzettel
from .models import Bild
from .models import Tagesnachricht

admin.site.register(ChatMessage)
admin.site.register(Character)
admin.site.register(UserProfile)  # Fügen Sie dies hinzu, um UserProfiles im Admin-Bereich zu sehen
# Optional: Sie können auch das User-Modell registrieren, falls noch nicht geschehen
admin.site.register(AdventNumber)
admin.site.register(Decision)
admin.site.register(Vote)
admin.site.register(SnowballHit)
admin.site.register(Labyrinth)
admin.site.register(Notizzettel)
admin.site.register(Bild)
admin.site.register(Tagesnachricht)
