let lastActivityTime = new Date();

// Funktion, um die letzte Aktivitätszeit zu aktualisieren
function updateLastActivityTime() {
    lastActivityTime = new Date();
}

// Fügen Sie Event-Listener hinzu, um die Benutzeraktivität zu überwachen
window.addEventListener('mousemove', updateLastActivityTime);
window.addEventListener('keydown', updateLastActivityTime);
window.addEventListener('scroll', updateLastActivityTime);
// ... weitere Event-Listener für Benutzeraktionen ...

// Funktion, um die Session zu beenden, falls die Inaktivitätszeit zu lang ist
function checkInactivity() {
    let currentTime = new Date();
    let inactivityTime = (currentTime - lastActivityTime) / 1000; // in Sekunden

    // SESSION_COOKIE_AGE in Sekunden (z.B. 15 Minuten = 900 Sekunden)
    const SESSION_COOKIE_AGE = 9000;

    if (inactivityTime > SESSION_COOKIE_AGE) {
        // Senden Sie die POST-Anfrage, um die Session zu beenden
        fetch('/advent/end-session/', {
            method: 'POST',
            headers: {
                'X-CSRFToken': getCookie('csrftoken'),
                'Content-Type': 'application/json'
            }
        }).then(response => {
            if (response.ok) {
                // Optionale Logik nach dem Beenden der Session
                console.log('Session beendet');
            }
        });
    }
}

// Überprüfen Sie die Inaktivität alle 5 Sekunden
setInterval(checkInactivity, 5000);
