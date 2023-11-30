document.addEventListener('DOMContentLoaded', function() {
    let draggables = document.querySelectorAll('.draggable');
    let kuehlschrank = document.getElementById('kuehlschrank');
    let tag = kuehlschrank.getAttribute('data-tag'); // Abrufen des Tag-Wertes

    draggables.forEach(function(draggable) {
        draggable.addEventListener('dragstart', function(event) {
            console.log("Dragstart für Element mit ID:", this.getAttribute('data-id'));
            event.dataTransfer.setData("text/plain", this.getAttribute('data-id'));
        });
    });

    kuehlschrank.addEventListener('dragover', function(event) {
        event.preventDefault();
    });

    kuehlschrank.addEventListener('drop', function(event) {
        event.preventDefault();
        const data = event.dataTransfer.getData("text");
        const draggableElement = document.querySelector(`.draggable[data-id="${data}"]`);

        if (!draggableElement) {
            console.error("Draggable Element nicht gefunden:", data);
            return;
        }

        const kuehlschrankRect = kuehlschrank.getBoundingClientRect();
        let newX = event.clientX - kuehlschrankRect.left - draggableElement.offsetWidth / 2;
        let newY = event.clientY - kuehlschrankRect.top - draggableElement.offsetHeight / 2;

        console.log("Neue Position:", newX, newY);

        draggableElement.style.left = `${newX}px`;
        draggableElement.style.top = `${newY}px`;

        updatePosition(draggableElement, newX, newY, tag); // Übergeben des Tags als zusätzliches Argument
    });
});

function updatePosition(element, x, y) {
    let id = element.getAttribute('data-id');
    let type = element.getAttribute('data-type');

    console.log("Sending update for", type, id, "with position", x, y); // Zum Debuggen

    fetch('/advent/update_position/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ type: type, id: id, x: x, y: y })
    }).then(response => {
        if (!response.ok) {
            console.error("Fehler bei der Update-Anfrage:", response.statusText);
        }
        return response.json();
    }).then(data => {
        console.log("Serverantwort:", data);
    }).catch(error => {
        console.error("Fehler beim Senden der Anfrage:", error);
    });
}


function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
