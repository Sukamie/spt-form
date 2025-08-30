document.addEventListener('DOMContentLoaded', function() {
    const otherIncomeSelect = document.querySelector('[name="other_income_option"]');
    const pp46Table = document.getElementById('asset-table-5');
    const pp46AddRowButton = pp46Table
        ? pp46Table.closest('.form-card').querySelector('.add-asset-row')
        : null;

    function togglePP46Table() {
        if (!otherIncomeSelect) return;
        const isLocked = otherIncomeSelect.value === '2'; // PP23/PP55

        if (pp46Table) {
            const tableFields = pp46Table.querySelectorAll('input, select, textarea');
            tableFields.forEach(el => el.disabled = isLocked);
        }

        if (pp46AddRowButton) {
            pp46AddRowButton.disabled = isLocked;
        }
    }

    if (otherIncomeSelect) {
        otherIncomeSelect.addEventListener('change', togglePP46Table);
        togglePP46Table();
    }
});