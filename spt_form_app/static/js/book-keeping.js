document.addEventListener('DOMContentLoaded', function() {
    const bookKeepingSelect = document.getElementById('id_book_keeping_option');
    const accountantFields = [
        'id_public_accountant',
        'id_public_accountant_npwp',
        'id_public_accountant_office',
        'id_public_accountant_office_npwp',
        'id_tax_consultant',
        'id_tax_consultant_npwp',
        'id_tax_consultant_office',
        'id_tax_consultant_office_npwp'
    ].map(id => document.getElementById(id));

    function toggleAccountantFields() {
        const isTidakDiaudit = bookKeepingSelect.value === '2';
        accountantFields.forEach(field => {
            if (field) {
                field.disabled = isTidakDiaudit;
                if (isTidakDiaudit) field.value = '';
            }
        });
    }

    if (bookKeepingSelect) {
        bookKeepingSelect.addEventListener('change', toggleAccountantFields);
        toggleAccountantFields();
    }
});