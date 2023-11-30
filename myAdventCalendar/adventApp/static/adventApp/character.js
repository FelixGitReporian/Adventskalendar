



function showCharacterDetails(characterId) {
    var modal = document.getElementById('characterModal' + characterId);
    modal.style.display = 'flex';
}
function selectCharacter(characterId, is_taken) {
    if (!is_taken) {
        window.location.href = '/advent/choose-character/?selected_character=' + characterId;
    }
}
function closeModal(characterId) {
    var modal = document.getElementById('characterModal' + characterId);
    modal.style.display = 'none';
}
function confirmSelection(characterId) {
    window.location.href = '/advent/choose-character/?selected_character=' + characterId;
}

function resetCharacter(characterId, event) {
    event.stopPropagation();
    console.log("Reset-Funktion aufgerufen für ID:", characterId);
    var sliderValue = document.getElementById('reset-' + characterId).value;
    if (sliderValue == 1) {
        fetch('/advent/reset-character/' + characterId + '/', {
            method: 'POST',
            headers: {
                'X-CSRFToken': getCookie('csrftoken'), // CSRF-Token aus den Cookies holen
                'Content-Type': 'application/json'
            }
        }).then(response => {
            if (response.ok) {
                window.location.reload();
            } else {
                alert('Fehler beim Zurücksetzen des Charakters');
            }
        });
    } else {
        alert('Bitte schieben Sie den Regler ganz nach rechts, um zurückzusetzen.');
    }
}

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


    

document.addEventListener('DOMContentLoaded', (event) => {
    document.querySelectorAll('.reset-button').forEach(button => {
        button.addEventListener('click', (e) => {
            const characterId = button.getAttribute('data-character-id');
            resetCharacter(characterId, e);
        });
    });
});




