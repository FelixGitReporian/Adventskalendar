function showCharacterDetails(characterId) {
    var modal = document.getElementById('characterModal' + characterId);
    modal.style.display = 'flex';
}
function selectCharacter(characterId, isTaken) {
    if (!isTaken) {
        window.location.href = '/advent/choose-character/?selected_character=' + characterId;
    }
}
function closeModal(characterId) {
    var modal = document.getElementById('characterModal' + characterId);
    modal.style.display = 'none';
}

function confirmSelection(characterId) {
    // Schließen Sie das Charakter-Modal
    closeModal(characterId);

    // Setzen Sie die character_id im Registrierungsformular
    document.getElementById('selectedCharacterId').value = characterId;

    // Zeigen Sie das Registrierungsformular an
    document.getElementById('registrationModal').style.display = 'block';
}
window.onclick = function(event) {
    var modals = document.getElementsByClassName('modal');
    for (var i = 0; i < modals.length; i++) {
        var modal = modals[i];
        if (event.target == modal) {
            modal.style.display = 'none';
        }
    }
}
function toggleLogin(isLogin) {
    document.getElementById('is_login').value = isLogin ? 'true' : 'false';
}
