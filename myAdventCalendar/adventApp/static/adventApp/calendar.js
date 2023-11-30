document.addEventListener('wheel', function(e) {
    var container = document.getElementById('adventContainer');
    var scale = Math.max(1, container.getBoundingClientRect().width / window.innerWidth);
    if (e.deltaY < 0) {
        scale *= 1.1; // Vergrößern
    } else {
        scale /= 1.1; // Verkleinern
    }
    container.style.transform = 'scale(' + scale + ')';
});
