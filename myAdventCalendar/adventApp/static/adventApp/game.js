function getCsrfToken() {
    return document.cookie.split('; ').find(row => row.startsWith('csrftoken')).split('=')[1];
}

window.addEventListener('DOMContentLoaded', (event) => {
    setTimeout(() => {
        const messageElement = document.querySelector('.message');
        if (messageElement) {
            messageElement.style.display = 'none';
        }
    }, 4000); // Versteckt die Nachricht nach 4 Sekunden
});

// Stellen Sie sicher, dass die Elemente vorhanden sind, bevor Sie Event-Listener hinzufügen
const joinGameButton = document.getElementById('join-game');
const startNewGameButton = document.getElementById('start-new-game');

if (joinGameButton) {
    joinGameButton.addEventListener('click', function() {
        document.getElementById('game-options-modal').style.display = 'none';
        fetch('/advent/join_game/', {
            method: 'POST',
            headers: {
                'X-CSRFToken': getCsrfToken(),
                'Content-Type': 'application/json'
            }
        }).then(response => response.json()).then(data => {
            if (data.status === 'success') {
                window.location.href = '/advent/decision/' + data.currentDecisionId;
            } else {
                console.error('Fehler beim Beitreten des Spiels');
            }
        });
    });
}

if (startNewGameButton) {
    startNewGameButton.addEventListener('click', function() {
        fetch('/advent/reset-game/', {
            method: 'POST',
            headers: {
                'X-CSRFToken': getCsrfToken(),
                'Content-Type': 'application/json'
            }
        }).then(response => response.json()).then(data => {
            if (data.status === 'success') {
                window.location.href = '/advent/decision/1';
            } else {
                console.error('Fehler beim Zurücksetzen des Spiels');
            }
        });
    });
}
