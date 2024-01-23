# Adventskalendar
Adventskalendar mit narrativen und spielerischen Askpekten - für die ganze Familie.
Link zur Website folgt im neuen Jahr - nachdem das Projekt einmal durchgelaufen ist.

## Projektbeschreibung

Das "Advent Decision Game" ist ein interaktives Web-basiertes Spiel, das in Django entwickelt wurde. Es ermöglicht Benutzern, Charaktere zu wählen und an Entscheidungen teilzunehmen, die den weiteren Verlauf des Spiels beeinflussen. Jede Entscheidung wird in Echtzeit bewertet, und die Mehrheitsentscheidung bestimmt den nächsten Schritt im Spiel. Das Spiel bietet eine einzigartige Mischung aus Abenteuer und Strategie und ist ideal für die Adventszeit geeignet.
Hauptmerkmale

### Charakterauswahl: Benutzer können aus verschiedenen Charakteren auswählen, um am Spiel teilzunehmen.

![alt text](https://github.com/FelixGitReporian/Adventskalendar/blob/main/choose_char_html.png)
![alt text](https://github.com/FelixGitReporian/Adventskalendar/blob/main/choose_char_html2.png)

### Echtzeit-Entscheidungen: Entscheidungen werden in Echtzeit getroffen, wenn mehrere speilen wir abgestimmt und beeinflussen den Spielverlauf.
![alt text](https://github.com/FelixGitReporian/Adventskalendar/blob/main/game1.png)
![alt text](https://github.com/FelixGitReporian/Adventskalendar/blob/main/schneeballschlacht_html.png)

### Interaktive Chat-Funktion: Ermöglicht den Spielern, während des Spiels miteinander zu kommunizieren.
https://github.com/FelixGitReporian/Adventskalendar/blob/main/kalendar_html.png
![alt text](https://github.com/FelixGitReporian/Adventskalendar/blob/main/kalendar_html.png)

### Responsive Design: Die Anwendung ist sowohl auf Desktop- als auch auf mobilen Geräten nutzbar.
### noch in Bearbeitung: Kühlschrank mit täglichen Sammlungen der Teilnehmer für Fragen wie "wofür bist du dankbar?", welche als Notiz oder Bild an eine Stelle der Kühlschranktür gedraftet werden können. Ein zu beschmückender Weihnachtsbaum mit zu plazierenden Geschenken für die anderen folgt auch noch.
![alt text](https://github.com/FelixGitReporian/Adventskalendar/blob/main/kuelschrank_html.png)

## Technologien

    Backend: Django (Python-basiertes Web-Framework)
    Frontend: HTML, CSS, JavaScript
    Datenbank: SQLite (Standard-Datenbank von Django)
    
ich benutze zum selber hosten unraid --> mysql --> Apache Webserver --> Gunicorn
https://docs.djangoproject.com/en/4.2/howto/deployment/

## Installation und Einrichtung

Repository klonen:

    git clone https://github.com/FelixGitReporian/Adventskalendar.git


## Abhängigkeiten installieren:

bash:

    pip install -r requirements.txt

## Django-Anwendung ausführen:

bash:

    python manage.py runserver

    Im Browser öffnen:
    Besuchen Sie http://localhost:8000 in Ihrem Webbrowser, um auf das Spiel zuzugreifen.

### Mitwirken

Ihr Beitrag zu diesem Projekt ist willkommen. Bitte erstellen Sie ein Issue oder senden Sie einen Pull-Request, wenn Sie eine Verbesserung vorschlagen möchten.
