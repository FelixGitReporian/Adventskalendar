let lastActivityTime = new Date().getTime();

function refreshActivityTime() {
    lastActivityTime = new Date().getTime();
}

function checkActivity() {
    let currentTime = new Date().getTime();
    let inactiveTime = currentTime - lastActivityTime;
    
    // Zeit in Millisekunden (z.B. 5 Minuten Inaktivität: 300000)
    if (inactiveTime > 150) {
        // Senden Sie eine Anfrage an den Server, um die Session zu beenden
        fetch('/advent/end-session/', { method: 'POST' });
    }
}

// Aktivitäts-Events
document.addEventListener('mousemove', refreshActivityTime);
document.addEventListener('keypress', refreshActivityTime);

// Regelmäßige Überprüfung
setInterval(checkActivity, 6000); // Überprüfen Sie jede Minute
