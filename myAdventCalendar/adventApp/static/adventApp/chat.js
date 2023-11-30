


var baseURL = 'http://127.0.0.1:8000/'


document.addEventListener('DOMContentLoaded', (event) => {
    var chatContainer = document.getElementById("chat-container");
    var isChatOpen = localStorage.getItem('chatOpen') === 'true';

    // Zustand des Chats beim Laden der Seite setzen
    chatContainer.style.display = isChatOpen ? 'block' : 'none';
});


function sendMessage() {
    var message = document.getElementById('chat-message').value;
    console.log(characterId)
    fetch('/advent/chat/send/', {
        method: 'POST',
        body: JSON.stringify({
            'message': message,
            'character_id': characterId
        }),
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        }
    }).then(response => {
        if (response.ok) {
            document.getElementById('chat-message').value = ''; // Textfeld zurücksetzen
            loadMessages(); // Nachrichten neu laden
        }
    });
}

document.getElementById('chat-message').addEventListener('keypress', function(event) {
    if (event.key === 'Enter') {
        event.preventDefault();
        sendMessage();
    }
});

function loadMessages() {
    fetch('/advent/chat/messages/')
        .then(response => response.json())
        .then(data => {
            var chatMessagesDiv = document.getElementById('chat-messages');
        
            chatMessagesDiv.scrollTop = chatMessagesDiv.scrollHeight;
            chatMessagesDiv.innerHTML = '';  // Löschen der aktuellen Nachrichten
            data.messages.forEach(message => {
                var messageDiv = document.createElement('div');
                messageDiv.className = 'chat-message';
                messageDiv.innerHTML = `<strong>${message.character__name}</strong>: ${message.message} <div class="chat-time">${new Date(message.timestamp).toLocaleTimeString()}</div>`;
                chatMessagesDiv.appendChild(messageDiv);
            });
        });
}


// Hilfsfunktion, um den CSRF-Token aus den Cookies zu lesen
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

function toggleChat() {
    var chatContainer = document.getElementById("chat-container");
    var isChatOpen = chatContainer.style.display !== 'none';

    // Umschalten der Anzeige des Chats
    chatContainer.style.display = isChatOpen ? 'none' : 'block';

    // Speichern des Zustands im localStorage
    localStorage.setItem('chatOpen', !isChatOpen);
}





// Laden der Nachrichten beim Start der Seite
loadMessages();

// Nachrichten alle 0.5 Sekunden aktualisieren
setInterval(loadMessages, 500);