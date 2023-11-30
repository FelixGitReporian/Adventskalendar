document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById('snowball-form');
    form.onsubmit = function(event) {
        event.preventDefault();
        const target = document.getElementById('target').value;
        const messageBox = document.getElementById('message-box');
        const formData = new FormData(form);

        // Senden einer Anfrage an den Server
        fetch('/advent/snowball_fight/', {
            method: 'POST',
            body: formData,
            headers: {
                'X-CSRFToken': getCookie('csrftoken')
            }
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Netzwerkantwort war nicht ok');
            }
            return response.text();  // Erwartet HTML-Antwort
        })
        .then(html => {
            // Ersetzen Sie den Inhalt der Seite mit der neuen HTML-Antwort
            document.open();
            document.write(html);
            document.close();
        })
        .catch(error => {
            console.error('Error:', error);
        });
    };
});

// Hilfsfunktion, um den CSRF-Token zu erhalten
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
