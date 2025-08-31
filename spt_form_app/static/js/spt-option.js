document.addEventListener('DOMContentLoaded', function() {

    function toggleFormDisabled() {
        const sptOption = document.querySelector('[name="spt_option"]');
        const step1770Ihal1 = steps[7]; // index 7 = step ke-8

        if (sptOption && step1770Ihal1) {
            const allFields = step1770Ihal1.querySelectorAll('input, select, textarea');
            const isDisabled = sptOption.value === '2';
            allFields.forEach(el => el.disabled = isDisabled);
        }
    }
});