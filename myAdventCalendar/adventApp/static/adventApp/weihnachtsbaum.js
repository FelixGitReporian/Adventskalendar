// weihnachtsbaum.js
document.addEventListener('DOMContentLoaded', function() {
    const draggables = document.querySelectorAll('.draggable');
    const treeArea = document.getElementById('tree-area');

    draggables.forEach(draggable => {
        draggable.addEventListener('dragstart', () => {
            draggable.classList.add('dragging');
        });

        draggable.addEventListener('dragend', () => {
            draggable.classList.remove('dragging');
            updateCharacterPosition(draggable);
        });
    });

    function updateCharacterPosition(draggable) {
        const id = draggable.getAttribute('data-id');
        const type = draggable.getAttribute('data-type');
        const x = draggable.style.left;
        const y = draggable.style.top;
        const note = type === 'gift' ? draggable.getAttribute('data-note') : '';

        fetch('advent/update_character/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: `type=${type}&id=${id}&position_x=${x}&position_y=${y}&note=${note}`
        })
        .then(response => response.json())
        .then(data => {
            console.log(data.status);
        });
    }
});
