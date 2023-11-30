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
    console.log(`Navigating to: /advent/choose-character/?selected_character=${characterId}`);
    window.location.href = `/advent/choose-character/?selected_character=${characterId}`;
}
