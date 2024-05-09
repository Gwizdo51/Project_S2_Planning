function updateData() {
    fetch('/update_data?rand=' + Math.random())
        .then(response => response.json())
        .then(data => {
            // Mettre à jour les éléments de la page avec les nouvelles données
            document.getElementById('data-container').innerText = 'Nouvelle mise à jour : ' + data.timestamp;
        });
}