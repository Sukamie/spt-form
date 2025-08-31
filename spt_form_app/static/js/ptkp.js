   document.addEventListener("DOMContentLoaded", function () {
    const optionField = document.getElementById("id_ptkp_option");
    const amountField = document.getElementById("id_ptkp_amount");

    if (amountField) {
        amountField.disabled = true; // awalnya disable
    }

    if (optionField) {
        optionField.addEventListener("change", function () {
            if (optionField.value && optionField.value.trim() !== "") {
                amountField.disabled = false;
            } else {
                amountField.disabled = true;
            }
        });
    }
});