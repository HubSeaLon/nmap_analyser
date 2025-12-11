document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('televerser-btn').addEventListener('click', function() {
        document.getElementById('file-input').click();
    });

    // Evenement qui submit le formulaire quand un ou plusieurs fichier est déposé
    document.getElementById('file-input').addEventListener('change', function() {
        if (this.files.length > 0) {
            document.getElementById('upload-form').submit();
        }
    });

    document.getElementById('fichier-select').addEventListener('change', function() {
        const scanId = this.value;
        window.location.href = `/${scanId}`;
    });

    // Récupérer l'ID du scan depuis l'URL et ajouter des écouteurs d'événements aux IPs
    const urlId = new URLSearchParams(window.location.search);
    const scanId = urlId.get('scanId');
    
    if (scanId) {
        const ipRows = document.querySelectorAll('.result-ip-header');
        ipRows.forEach(row => {
            row.addEventListener('click', function () {
                const ipId = this.getAttribute('data-ip-id'); 
                window.location.href = `/${scanId}/${ipId}`;
            });
        });
    }
});