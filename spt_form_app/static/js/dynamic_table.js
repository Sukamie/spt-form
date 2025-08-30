document.addEventListener('DOMContentLoaded', function () {
    document.addEventListener('click', function (e) {
        // Tambah baris
        if (e.target.classList.contains('add-asset-row')) {
            let table = e.target.closest('.form-card').querySelector('table');
            let lastRow = table.querySelector('tbody tr:last-child');
            let newRow = lastRow.cloneNode(true);

            // Kosongkan semua input/select/textarea
            newRow.querySelectorAll('input, select, textarea').forEach(function (input) {
                input.value = '';
            });

            // Tambah tombol hapus
            let aksiCell = newRow.querySelector('td:last-child');
            aksiCell.innerHTML = '<button type="button" class="btn btn-danger btn-sm remove-row">Hapus</button>';

            table.querySelector('tbody').appendChild(newRow);
        }

        // Hapus baris
        if (e.target.classList.contains('remove-row')) {
            let row = e.target.closest('tr');
            let tbody = row.closest('tbody');
            if (tbody.querySelectorAll('tr').length > 1) {
                row.remove();
            } else {
                row.querySelectorAll('input, select, textarea').forEach(function (input) {
                    input.value = '';
                });
            }
        }
    });
});