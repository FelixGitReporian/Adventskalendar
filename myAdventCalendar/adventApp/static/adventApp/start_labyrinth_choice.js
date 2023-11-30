function getCsrfToken() {
    const csrfTokenCookie = document.cookie.split('; ').find(row => row.startsWith('csrftoken='));
    return csrfTokenCookie ? csrfTokenCookie.split('=')[1] : '';
}

window.addEventListener('DOMContentLoaded', (event) => {
    const joinLabyrinthButton = document.getElementById('join-labyrinth-game');
    const startNewLabyrinthButton = document.getElementById('start-new-labyrinth');

    if (joinLabyrinthButton) {
        joinLabyrinthButton.addEventListener('click', function() {
            fetch('/advent/join_game_lab/', {
                method: 'POST',
                headers: {
                    'X-CSRFToken': getCsrfToken(),
                    'Content-Type': 'application/json'
                }
            }).then(response => response.json()).then(data => {
                if (data.status === 'success') {
                    window.location.href = '/advent/labyrinth_view/' + data.currentLabyrinthId;
                } else {
                    console.error('Fehler beim Zurücksetzen des Labyrinths:', data.message);
                }
            }).catch(error => {
                console.error('Fehler bei der Verarbeitung der Antwort:', error);
            });

        });
    }

    if (startNewLabyrinthButton) {
        startNewLabyrinthButton.addEventListener('click', function() {
            fetch('/advent/reset_game_lab/', {
                method: 'POST',
                headers: {
                    'X-CSRFToken': getCsrfToken(),
                    'Content-Type': 'application/json'
                }
            }).then(response => response.json()).then(data => {
                if (data.status === 'success') {
                    window.location.href = '/advent/labyrinth/12';
                } else {
                    console.error('Fehler beim Zurücksetzen des Labyrinths:', data.message);
                }
            }).catch(error => {
                console.error('Fehler bei der Verarbeitung der Antwort:', error);
            });
        });
    }
});
