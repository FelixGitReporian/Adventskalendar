


// JavaScript-Code zum Senden der POST-Anfrage
fetch('/advent/end-session/', {
    method: 'POST',
    headers: {
        'X-CSRFToken': getCookie('csrftoken'), // CSRF-Token aus den Cookies holen
        'Content-Type': 'application/json'
    },
    // ... andere Optionen ...
});

// Funktion, um den CSRF-Token aus den Cookies zu lesen
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
