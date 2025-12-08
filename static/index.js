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
});