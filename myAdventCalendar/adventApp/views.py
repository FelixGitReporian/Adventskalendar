from django.shortcuts import render, redirect, get_object_or_404
#from django.contrib.auth.models import User
#from django.contrib.auth.hashers import make_password
from .models import Character
from .models import AdventNumber
import random
from django.http import HttpResponse
from datetime import datetime
#from django.shortcuts import render
from .models import ChatMessage
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth import logout
from django.views.decorators.http import require_POST
from django.utils import timezone
from .models import Decision, Vote
#from django.http import HttpResponseForbidden
from django.db.models import Count
from .models import Ornament, Gift, SnowballHit
from .models import Labyrinth
import random
from .models import Notizzettel, Bild
from django.core.exceptions import ObjectDoesNotExist
from .forms import NotizzettelForm, BildForm
from django.db.models import F
from .models import Tagesnachricht, Vote_lab

def advent_day(request, day):
    # Logik, um den Inhalt für den spezifischen Tag zu laden
    # ...
    if day == 2:
        start_decision_id = 11  # Die ID der Startentscheidung für Tag 3
        return redirect('decision_view', decision_id=start_decision_id)
    if day == 3 or day == 10 or day == 17:
        return redirect("advent_kerze")
    if day == 8:
        return redirect('snowball_fight')
    if day == 9:
        return redirect("start_labyrinth_choice")
    if day == 11:
        return redirect("kuehlschrank", tag=day)
    if day == 23 or day == 24:
        return redirect('tree_view')
    return render(request, 'advent_day.html', {'day': day})

def advent_kerze(request):
    return render(request, 'adventApp/advent_kerze.html')


def kuehlschrank(request, tag):
    notizzettel_list = Notizzettel.objects.filter(tag=tag).annotate(character_name=F('character__name'))
    bild_list = Bild.objects.filter(tag=tag).annotate(character_name=F('character__name'))
    tagesnachricht = Tagesnachricht.objects.get(tag=tag)
    return render(request, 'adventApp/kuehlschrank.html', {
        'notizzettel_list': notizzettel_list,
        'bild_list': bild_list,
        'tagesnachricht': tagesnachricht.nachricht,
        'tag': tag  # Fügen Sie diese Zeile hinzu
    })


def erstelle_notizzettel(request, tag):
    if request.method == 'POST':
        form = NotizzettelForm(request.POST)
        if form.is_valid():
            notizzettel = form.save(commit=False)
            notizzettel.x_position = 0
            notizzettel.y_position = 0
            notizzettel.tag = tag
            notizzettel.save()
            return redirect('kuehlschrank', tag=tag)  # Tag in der Redirect-URL mitgeben
    else:
        form = NotizzettelForm()

    return render(request, 'adventApp/erstelle_notizzettel.html', {'form': form, 'tag': tag})


def lade_bild_hoch(request, tag):
    if request.method == 'POST':
        form = BildForm(request.POST, request.FILES)
        if form.is_valid():
            bild = form.save(commit=False)
            bild.x_position = 0  # Startposition, kann angepasst werden
            bild.y_position = 0  # Startposition, kann angepasst werden
            bild.tag = tag
            bild.save()
            return redirect('kuehlschrank', tag=tag)  # Passen Sie die Redirect-URL an
    else:
        form = BildForm()

    return render(request, 'adventApp/lade_bild_hoch.html', {'form': form, 'tag': tag})

@csrf_exempt
def update_position(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            obj_type = data['type']
            obj_id = data['id']
            new_x = int(data['x'])
            new_y = int(data['y'])
            print("wwwwwwwwwwwwwwwwwwwwwwww", new_x, new_y)
        except (ValueError, TypeError):
            return JsonResponse({'status':'false','message':'Ungültige Koordinaten'}, status=400)

        try:
            if obj_type == 'notizzettel':
                print("notiz")
                obj = Notizzettel.objects.get(id=obj_id)
            elif obj_type == 'bild':
                print("bild")
                obj = Bild.objects.get(id=obj_id)
            else:
                return JsonResponse({'status':'false','message':'Ungültiger Typ'}, status=400)

            obj.x_position = new_x
            obj.y_position = new_y
            obj.save()
            return JsonResponse({'status':'true','message':'Position aktualisiert'})
        except (KeyError, ValueError, TypeError):
            return JsonResponse({'status':'false','message':'Ungültige Daten'}, status=400)
        except ObjectDoesNotExist:
            return JsonResponse({'status':'false','message':'Objekt nicht gefunden'}, status=404)

    return JsonResponse({'status':'false','message':'Ungültige Anfrage'}, status=400)



def start_labyrinth_choice(request):
    return render(request, 'adventApp/start_labyrinth_choice.html')

@csrf_exempt
def update_character(request):
    if request.method == 'POST':
        data = request.POST
        if 'ornament_id' in data:
            ornament = Ornament.objects.get(id=data['ornament_id'])
            ornament.position_x = data['position_x']
            ornament.position_y = data['position_y']
            ornament.save()
        elif 'gift_id' in data:
            gift = Gift.objects.get(id=data['gift_id'])
            gift.position_x = data['position_x']
            gift.position_y = data['position_y']
            gift.note = data['note']
            gift.save()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'failed'})



def tree_view(request):
    ornaments = Ornament.objects.all()
    gifts = Gift.objects.all()
    context = {'ornaments': ornaments, 'gifts': gifts}
    return render(request, 'adventApp/tree.html', context)



def get_all_character_names():
    characters = Character.objects.all()
    return [character.name for character in characters]

def get_current_character_name(character_id):
    character = get_object_or_404(Character, id=character_id)
    return character.name

#@csrf_exempt
def snowball_fight(request):
    current_player_id = request.session.get('selected_character_id')
    player_character = get_object_or_404(Character, id=current_player_id)
    characters = Character.objects.exclude(id=current_player_id)
    
    hits_made = SnowballHit.objects.filter(attacker=player_character).count()
    hits_received = SnowballHit.objects.filter(target=player_character).count()

    if request.method == 'POST':
        target_id = request.POST.get('target')
        target_character = get_object_or_404(Character, id=target_id)

        hit = player_character.throw_snowball(target_character)
        message = f"Du hast {target_character.name} getroffen!" if hit else "Du hast verfehlt!"
        # Fügen Sie hier ggf. weitere Logik hinzu

    return render(request, 'adventApp/snowball_fight.html', {
        'characters': characters,
        'player_character': player_character,
        'hits_made': hits_made,
        'hits_received': hits_received,
        # 'message': message, falls Sie eine Nachricht übergeben möchten
    })


MISCHPUNKTE = [4, 8, 12]
def labyrinth_view(request, labyrinth_id):
    print("Accessing labyrinth view for labyrinth_id:", labyrinth_id)
    labyrinth = get_object_or_404(Labyrinth, id=labyrinth_id)

    # Prüfe, ob das aktuelle Labyrinth gemischt werden soll
    if labyrinth_id in MISCHPUNKTE:
        mische_labyrinth()

    user_vote = None
    message = evaluate_votes_lab(request, labyrinth, user_vote)
    
    if 'chat_checked' in request.session:
        del request.session['chat_checked']
        
    if 'labyrinth_id_before' in request.session:
        labyrinth_mess_id = request.session['labyrinth_id_before']
        chat_response = labyrinth_chat(request, labyrinth_id=labyrinth_mess_id)
        if chat_response:
            message = chat_response
            print("Chat response from previous labyrinth:", message)
    else:
        chat_response = labyrinth_chat(request, labyrinth_id)
        if chat_response:
            message = chat_response
            print("Chat response from current labyrinth:", message)
        else:
            message = None

    if request.session.get('labyrinth_completed'):
        del request.session['labyrinth_completed']  # Lösche die Session-Variable nach Gebrauch
        context = {'background_image_url': '/adventApp/kuehlschrankbild.png'}
        return render(request, 'adventApp/labyrinth_ende.html', context)
    
    

    if 'next_labyrinth_id' in request.session:
        next_labyrinth_id = request.session.pop('next_labyrinth_id')
        request.session['labyrinth_id_before'] = labyrinth_id
        if next_labyrinth_id == 'end':
            return redirect('/advent/advent_calendar/')
        else:
            return redirect('labyrinth_view', labyrinth_id=next_labyrinth_id)

    if 'game_choice_made' not in request.session:
        request.session['game_choice_made'] = False
        if not Vote_lab.objects.filter(labyrinth=labyrinth).exists():
            labyrinth.start_time = timezone.now()
            labyrinth.save()
    
        if 'selected_character_id' in request.session:
            user_vote = Vote.objects.filter(character_id=request.session['selected_character_id'], labyrinth=labyrinth).first()

    return render(request, 'adventApp/labyrinth.html', {
        'labyrinth': labyrinth,
        'user_vote': user_vote,
        'message': message
    })


def vote_lab(request, labyrinth_id):
    selected_character_id = request.session.get('selected_character_id')
    if not selected_character_id:
        return redirect('choose_character')

    if Vote_lab.objects.filter(labyrinth_id=labyrinth_id, character_id=selected_character_id).exists():
        return redirect('labyrinth_view', labyrinth_id=labyrinth_id)

    if request.method == 'POST':
        choice = request.POST.get('choice')
        labyrinth = get_object_or_404(Labyrinth, id=labyrinth_id)
        if not Vote_lab.objects.filter(labyrinth=labyrinth).exists():
            labyrinth.start_time = timezone.now()
            labyrinth.save()
        
        Vote_lab.objects.create(labyrinth_id=labyrinth_id, character_id=selected_character_id, choice=choice)
    return redirect('labyrinth_view', labyrinth_id=labyrinth_id)

def evaluate_votes_lab(request, labyrinth, user_vote):
    if (timezone.now() - labyrinth.start_time) > timezone.timedelta(seconds=10):
        votes = Vote_lab.objects.filter(labyrinth=labyrinth).values('choice').annotate(count=Count('choice')).order_by('-count')
        if votes:
            top_vote = votes[0]
            if len(votes) > 1 and votes[1]['count'] == top_vote['count']:
                return "Gleichstand, bitte stimmen Sie erneut ab."
            else:
                next_labyrinth = labyrinth.next_labyrinth_a if top_vote['choice'] == 'A' else labyrinth.next_labyrinth_b
                if next_labyrinth:
                    request.session['next_labyrinth_id'] = next_labyrinth.id
                    return None
                else:
                    request.session['next_labyrinth_id'] = 'end'
                    return None
        else:
            return 'Keine Stimmen abgegeben.'
    else:
        return 'Abstimmung läuft noch.'

def mische_labyrinth():
    all_labyrinths = list(Labyrinth.objects.all())
    for lab in all_labyrinths:
        next_choices = [l for l in all_labyrinths if l.id != lab.id]
        lab.next_decision_a = random.choice(next_choices)

        next_choices.remove(lab.next_decision_a)
        lab.next_decision_b = random.choice(next_choices) if next_choices else None

        lab.save()
        
def labyrinth_chat(request, labyrinth_id):
    labyrinth = get_object_or_404(Labyrinth, id=labyrinth_id)
    selected_character_id = request.session.get('selected_character_id')
    selected_character = get_object_or_404(Character, id=selected_character_id) if selected_character_id else None

    if 'chat_checked' not in request.session:
        if labyrinth.possessed_character == selected_character:
            

            valid_messages = ChatMessage.objects.filter(timestamp__gte=labyrinth.start_time)
            print("weiwiweiiiiiiiiiiiiiiiiiiiiiiiiiwwwwwwwwwwwwwwwwwww:    ", valid_messages, labyrinth.start_time)
    
            for message in valid_messages:
                lower_message = message.message.lower()
                if 'krampus' in lower_message and labyrinth.possessed_character == selected_character:
                    print("yeah baby_________________________________________________________________")
                    request.session['labyrinth_completed'] = True
                    break
                elif ('man sieht nur mit dem herzen gut' in lower_message or 'das wesentliche ist für die augen unsichtbar' in lower_message) and selected_character != labyrinth.possessed_character:
                    request.session['labyrinth_completed'] = True
                    break
    
            request.session['chat_checked'] = True
        return 'Du bist besessen - führe die Gruppe in die Irre.'
    
    return None



    
    


@csrf_exempt
def reset_game_lab(request):
    if request.method == 'POST':
        Vote_lab.objects.all().delete()
        for labyrinth in Labyrinth.objects.all():
            labyrinth.start_time = timezone.now()
            labyrinth.save()
        request.session['game_choice_made'] = True
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error'}, status=405)
    
@csrf_exempt
def join_game_lab(request):
    if request.method == 'POST':
        selected_character_id = request.POST.get('selected_character')
        if selected_character_id:
            request.session['selected_character_id'] = selected_character_id

        latest_labyrinth_with_votes = (
            Labyrinth.objects
            .annotate(vote_count=Count('vote'))
            .filter(vote_count__gt=0)
            .order_by('-start_time')
            .first()
        )

        if latest_labyrinth_with_votes:
            return JsonResponse({'status': 'success', 'currentLabyrinthId': latest_labyrinth_with_votes.id})
        else:
            return JsonResponse({'status': 'success', 'currentLabyrinthId': 1})
    else:
        return JsonResponse({'status': 'error'}, status=405)









def decision_view(request, decision_id):
    #if reset_game(request):
    #    pass
    print("Accessing decision view for decision_id:", decision_id)
    decision = get_object_or_404(Decision, id=decision_id)
    user_vote = None
    
    message = evaluate_votes(request, decision, user_vote)
    if 'next_decision_id' in request.session:
        next_decision_id = request.session.pop('next_decision_id')
        if next_decision_id == 'end':
            return redirect('/advent/advent_calendar/')
        else:
            return redirect('decision_view', decision_id=next_decision_id)

    
    
    
    if 'game_choice_made' not in request.session:
        request.session['game_choice_made'] = False
        # Zurücksetzen der Startzeit bei Beginn einer neuen Abstimmung
        if not Vote.objects.filter(decision=decision).exists():
            decision.start_time = timezone.now()
            print("new ________________________", decision.start_time)
            decision.save()
    
        if 'selected_character_id' in request.session:
            print("öööööööööööööööööööööööööö (decision:_view):  ", request.session)
            user_vote = Vote.objects.filter(character_id=request.session['selected_character_id'], decision=decision).first()
    
    # Zusätzliche Variable für das Template, um zu bestimmen, ob das Modal angezeigt werden soll
    #show_game_choice_modal = not request.session['game_choice_made']

    # Hier wird die evaluate_votes Logik direkt aufgerufen
    return render(request, 'adventApp/decision.html', {
        'decision': decision,
        'user_vote': user_vote,
        'message': message
    })


def vote(request, decision_id):
    selected_character_id = request.session.get('selected_character_id')
    print("zzzzzzzzzzzzzzzzzzzzzzzzzzzzz   (vote):  ", selected_character_id)
    # Überprüfen, ob ein Charakter ausgewählt wurde
    if not selected_character_id:
        # Umleiten zur Charakterauswahl oder eine Fehlermeldung anzeigen
        return redirect('choose_character')
    
    if Vote.objects.filter(decision_id=decision_id, character_id=selected_character_id).exists():
        # Benutzer hat bereits abgestimmt
        print("Benutzer hat bereits abgestimmt")
        return redirect('decision_view', decision_id=decision_id)

    if request.method == 'POST':
        choice = request.POST.get('choice')
        
        decision = get_object_or_404(Decision, id=decision_id)
        # Prüfen, ob es die erste Stimme für diese Entscheidung ist
        if not Vote.objects.filter(decision=decision).exists():
            decision.start_time = timezone.now()
            decision.save()
        
        Vote.objects.create(decision_id=decision_id, character_id=selected_character_id, choice=choice)
    # Nach der Abstimmung zurück zur Entscheidungsansicht
    return redirect('decision_view', decision_id=decision_id)


    

def evaluate_votes(request, decision, user_vote):
    print("Evaluating votes for decision:", decision.id)
    current_time = timezone.now()
    print(current_time - decision.start_time, "xxxxxxxxxxxxxxxxxxxxx")
    print(timezone.timedelta(seconds=10))
    if (current_time - decision.start_time) > timezone.timedelta(seconds=10):
        votes = Vote.objects.filter(decision=decision).values('choice').annotate(count=Count('choice')).order_by('-count')
        if votes:
            top_vote = votes[0]
            if len(votes) > 1 and votes[1]['count'] == top_vote['count']:
                return "Gleichstand, bitte stimmen Sie erneut ab."
            else:
                next_decision = decision.next_decision_a if top_vote['choice'] == 'A' else decision.next_decision_b
                if next_decision:
                    request.session['next_decision_id'] = next_decision.id
                    return None
                else:
                    request.session['next_decision_id'] = 'end'
                    return None
        else:
            return 'Keine Stimmen abgegeben.'
    else:
        return 'Abstimmung läuft noch.'





@csrf_exempt
def reset_game(request):
    if request.method == 'POST':
        # Löschen aller Vote-Objekte
        Vote.objects.all().delete()

        # Zurücksetzen der Startzeit der ersten Entscheidung
        #first_decision = Decision.objects.first()
        for decision in Decision.objects.all():
            decision.start_time = timezone.now()
            decision.save()

        # Setzen der Session-Variable
        request.session['game_choice_made'] = True

        # Rückgabe einer JSON-Antwort
        return JsonResponse({'status': 'success'})

    else:
        return JsonResponse({'status': 'error'}, status=405)
    
@csrf_exempt
def join_game(request):
    if request.method == 'POST':
        selected_character_id = request.POST.get('selected_character')

        # Loggen oder Ausdrucken der empfangenen Daten
        print("Empfangene selected_character_id:", selected_character_id)

        if selected_character_id:
            request.session['selected_character_id'] = selected_character_id
            print("Session-Update: selected_character_id gesetzt auf", selected_character_id)
        else:
            print("Keine selected_character_id im Request gefunden")

        # Suchen Sie die aktuellste Entscheidung, die noch nicht vollständig abgestimmt wurde
        latest_decision_with_votes = (
            Decision.objects
            .annotate(vote_count=Count('vote'))
            .filter(vote_count__gt=0)
            .order_by('-start_time')
            .first()
        )

        if latest_decision_with_votes:
            return JsonResponse({'status': 'success', 'currentDecisionId': latest_decision_with_votes.id})
        else:
            # Wenn keine Votes vorhanden sind, beginnen Sie von der ersten Entscheidung
            return JsonResponse({'status': 'success', 'currentDecisionId': 1})
    else:
        return JsonResponse({'status': 'error'}, status=405)
   
    


def choose_character(request):
    """if initialize_advent_numbers():
        # Die Initialisierung wurde gerade durchgeführt
        pass
    if update_advent_numbers_positions():
        pass"""
    
    characters = Character.objects.all()

    # Überprüfen, ob ein Charakter ausgewählt wurde
    selected_character_id = request.GET.get('selected_character')
    if selected_character_id:
        Character.objects.filter(id=selected_character_id).update(is_taken=True)
        
        #session abschnitt
        request.session['selected_character_id'] = selected_character_id
        # Erstellen eines datetime-Objekts
        current_time = datetime.now()
        # Umwandlung in einen String
        time_str = current_time.strftime('%Y-%m-%d %H:%M:%S')
        request.session['session_start_time'] = time_str
        
        # Weiterleitung zur Adventskalender-Seite
        return redirect('/advent/advent_calendar/')
    else:
        print("noch da")
    
    return render(request, 'adventApp/choose_character.html', {'characters': characters})



def advent_calendar(request):
    # Überprüfen, ob die Session noch gültig ist
    if 'selected_character_id' not in request.session:
        # Zurück zu choose_character
        return redirect('/advent/choose-character/')

    selected_character_id = request.session.get('selected_character_id')
    # Setzen Sie den ausgewählten Charakter als "nicht genommen"
    #Character.objects.filter(id=selected_character_id).update(is_taken=False)
    
    # Laden aller AdventNumber-Objekte
    advent_numbers = AdventNumber.objects.all()
    
    """#farbe und rotation
    colors = ['#ff0000', '#00ff00', '#0000ff', '#ffff00']  # Beispielfarben
    for number in advent_numbers:
        number.color = random.choice(colors)
    for number in advent_numbers:
        number.rotation = random.randint(0, 360)  # Zufällige Rotation zwischen 0 und 360 Grad"""
    # Übergeben der Daten an das Template
    return render(request, 'adventApp/advent_calendar.html', {'advent_numbers': advent_numbers})


def chat_view(request):
    # Hier müssen Sie den ausgewählten Charakter basierend auf der Session oder einer anderen Methode abrufen
    selected_character_id = request.session.get('selected_character_id')
    character = Character.objects.get(id=selected_character_id) # Hier den ausgewählten Charakter abrufen
    return render(request, 'chat.html', {'messages': ChatMessage.objects.all(), 
                                         'character': character})

@csrf_exempt
def end_session(request):
    print("end_session View wurde aufgerufen_____________________________")
    character_id = request.session.pop('selected_character_id', None)
    Character.objects.filter(id=character_id).update(is_taken=False)
    logout(request)
    return JsonResponse({'status': 'session_ended'})

@csrf_exempt
def send_message(request):
    data = json.loads(request.body)
    message_content = data.get('message', '')
    selected_character_id = request.session.get('selected_character_id')
    
    try:
        character = Character.objects.get(id=selected_character_id)
        if message_content:
            # Verwenden Sie hier 'message' anstelle von 'content'
            ChatMessage.objects.create(character=character, message=message_content)
            return JsonResponse({'status': 'ok'})
        else:
            return JsonResponse({'status': 'empty_message'}, status=400)
    except Character.DoesNotExist:
        return JsonResponse({'status': 'character_not_found'}, status=404)
    

def get_chat_messages(request):
    messages = ChatMessage.objects.all().order_by('timestamp')  # [:-10] Die letzten 10 Nachrichten
    messages_data = messages.values(
        'character__name',   # Zugriff auf den Namen des Charakters
        'message',
        'timestamp'
    )
    #print("schnablu: ", messages_data)
    return JsonResponse({'messages': list(messages_data)})







"""def initialize_advent_numbers():
    if AdventNumber.objects.count() == 0:
        for day in range(1, 25):
            position_x = random.randint(0, 100)  # Beispielwerte
            position_y = random.randint(0, 300)
            rotation = random.randint(0, 360)
            color = "#{:06x}".format(random.randint(0, 0xFFFFFF))  # Generiert einen zufälligen HEX-Farbcode
            AdventNumber.objects.create(day=day, position_x=position_x, 
                                        position_y=position_y, rotation=rotation, color=color)
        return True
    return False"""


def update_advent_numbers_positions():
    for number in AdventNumber.objects.all():
        number.position_x = random.randint(0, 100)  # Zufällige Position zwischen 0 und 100
        number.position_y = random.randint(0, 200)
        number.save()

    # Weiterleitung zurück zur Admin-Seite oder wo immer Sie möchten
    return redirect('/advent/advent_calendar/')

@require_POST
def reset_character(request, character_id):
    Character.objects.filter(id=character_id).update(is_taken=False)
    return JsonResponse({'status': 'ok'})



