document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('televerser-btn').addEventListener('click', function(e) {
        e.preventDefault();
        document.getElementById('file-input').click();
    });

    document.getElementById('file-input').addEventListener('change', function() {
        if (this.files.length > 0) {
            document.getElementById('upload-form').submit();
        }
    });

    document.getElementById('fichier-select').addEventListener('change', function() {
        const scanId = this.value;
        if (!scanId) return;
        window.location.href = `/${scanId}`;
    });

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