document.addEventListener('DOMContentLoaded', function() {
    const steps = document.querySelectorAll('.form-wizard-step');
    let currentStep = 0;

    function toggleFormDisabled() {
        const sptOption = document.querySelector('[name="spt_option"]');
        const step1770Ihal1 = steps[7]; // index 7 = step ke-8
        if (sptOption && step1770Ihal1) {
            const allFields = step1770Ihal1.querySelectorAll('input, select, textarea');
            const isDisabled = sptOption.value === '2';
            allFields.forEach(el => el.disabled = isDisabled);
        }
    }

    function showStep(index) {
        steps.forEach((step, i) => step.classList.toggle('active', i === index));
        window.scrollTo({ top: 0, behavior: 'smooth' });
        toggleFormDisabled();
    }

    document.querySelectorAll('.next-step').forEach(btn => {
        btn.addEventListener('click', () => {
            if (currentStep < steps.length - 1) {
                currentStep++;
                showStep(currentStep);
            }
        });
    });

    document.querySelectorAll('.prev-step').forEach(btn => {
        btn.addEventListener('click', () => {
            if (currentStep > 0) {
                currentStep--;
                showStep(currentStep);
            }
        });
    });

    const sptOption = document.querySelector('[name="spt_option"]');
    if (sptOption) {
        sptOption.addEventListener('change', toggleFormDisabled);
        toggleFormDisabled();
    }

    showStep(currentStep);
});