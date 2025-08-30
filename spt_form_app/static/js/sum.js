document.addEventListener('DOMContentLoaded', function () {

    /* ========================================================
       1. PENJUMLAHAN SATU KOLOM DI TABEL
    ======================================================== */
    function bindTableSum(tableId, inputName, totalFieldId) {
        const table = document.getElementById(tableId);
        const totalField = document.getElementById(totalFieldId);
        if (!table || !totalField) return;

        function calculateTotal() {
            let total = 0;
            table.querySelectorAll(`input[name="${inputName}"]`).forEach(input => {
                total += parseFloat(input.value.replace(/,/g, '')) || 0; // hapus koma
            });
            totalField.value = total;
        }

        table.addEventListener('input', function (e) {
            if (e.target?.name === inputName) {
                calculateTotal();
            }
        });

        calculateTotal(); // Hitung awal
    }

    // Pemanggilan fungsi untuk tabel tertentu
    bindTableSum('asset-table-1', 'acq_cost[]', 'id_total_asset');         // Tabel Harta
    bindTableSum('asset-table-2', 'amount[]', 'id_total_debt');            // Tabel Utang
    bindTableSum('asset-table-6', 'pph_amount[]', 'id_total_pph_amount');  // PPh Amount
    bindTableSum('asset-table-7', 'net_income[]', 'id_total_net_income_c');// Net Income


    /* ========================================================
       2. PENJUMLAHAN BANYAK KOLOM DI TABEL
    ======================================================== */
    function bindTableMultiSum(tableId, columns) {
        const table = document.getElementById(tableId);
        if (!table) return;

        function calculateTotals() {
            columns.forEach(col => {
                let total = 0;
                table.querySelectorAll(`input[name="${col.inputName}"]`).forEach(input => {
                    total += parseFloat(input.value.replace(/,/g, '')) || 0;
                });
                const totalField = document.getElementById(col.totalFieldId);
                if (totalField) totalField.value = total;
            });
        }

        table.addEventListener('input', function (e) {
            columns.forEach(col => {
                if (e.target?.name === col.inputName) {
                    calculateTotals();
                }
            });
        });

        calculateTotals(); // Hitung awal
    }

    // Pemanggilan fungsi multi kolom
    bindTableMultiSum('asset-table-4', [
        { inputName: 'retail_gross_income[]', totalFieldId: 'id_total_retail_gross_income' },
        { inputName: 'income_tax_25_paid[]', totalFieldId: 'id_total_income_tax_25_paid' }
    ]);

    bindTableMultiSum('asset-table-5', [
        { inputName: 'gross_turnover[]', totalFieldId: 'id_total_gross_turnover' },
        { inputName: 'final_pph_paid[]', totalFieldId: 'id_total_pph_final_paid' }
    ]);

});
