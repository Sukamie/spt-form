// TOTAL PPH
document.addEventListener("DOMContentLoaded", function () {
    function calculateTotalPph() {
        let total = 0;
        document.querySelectorAll('input[name="pph_amount[]"]').forEach(function (el) {
            let val = parseFloat(el.value.replace(/,/g, '')) || 0;
            total += val;
        });

        let totalField = document.getElementById("id_total_pph_amount");
        let targetField = document.getElementById("id_withheld_income_tax");

        if (totalField) {
            totalField.value = total;
        }
        if (targetField) {
            targetField.value = total;
        }
    }

    document.addEventListener("input", function (e) {
        if (e.target && e.target.name === "pph_amount[]") {
            calculateTotalPph();
        }
    });

    calculateTotalPph();
});

// PPH OPTION
document.addEventListener("DOMContentLoaded", function () {
    function parseNumber(val) {
        if (!val) return 0;
        val = val.replace(/[^0-9.-]/g, "");
        return parseFloat(val) || 0;
    }

    function updatePphOption() {
        const totalTaxField = document.getElementById("id_total_tax_payable");
        const withheldTaxField = document.getElementById("id_withheld_income_tax");
        const optionField = document.getElementById("id_pph_option_field");

        if (totalTaxField && withheldTaxField && optionField) {
            const total = parseNumber(totalTaxField.value);
            const withheld = parseNumber(withheldTaxField.value);
            const result = total - withheld;
            console.log("DEBUG total:", total, "withheld:", withheld, "result:", result);
            optionField.value = result;
        }
    }

    updatePphOption();

    ["id_total_tax_payable", "id_withheld_income_tax"].forEach(id => {
        const el = document.getElementById(id);
        if (el) {
            el.addEventListener("input", updatePphOption);
            el.addEventListener("change", updatePphOption);
        }
    });

    setInterval(updatePphOption, 1000);
});

// TAX CREDIT
document.addEventListener("DOMContentLoaded", function () {
    const tax1 = document.getElementById("id_self_assessed_income_tax_1");
    const tax2 = document.getElementById("id_self_assessed_income_tax_2");
    const total = document.getElementById("id_total_tax_credit");

    function hitungTotal() {
        const val1 = parseFloat(tax1.value.replace(/,/g, "")) || 0;
        const val2 = parseFloat(tax2.value.replace(/,/g, "")) || 0;
        total.value = val1 + val2;
    }

    tax1.addEventListener("input", hitungTotal);
    tax2.addEventListener("input", hitungTotal);
    hitungTotal();
});

// PAID OPTION
document.addEventListener("DOMContentLoaded", function () {
    const pphOption = document.getElementById("id_pph_option_field");
    const totalCredit = document.getElementById("id_total_tax_credit");
    const paidOption = document.getElementById("id_paid_option_income_tax_field");

    function toNumber(val) {
        if (!val) return 0;
        return parseFloat(val.replace(/[^0-9.-]/g, "")) || 0;
    }

    function hitungPaidOption() {
        if (!pphOption || !totalCredit || !paidOption) return;
        const val1 = toNumber(pphOption.value);
        const val2 = toNumber(totalCredit.value);
        const hasil = val1 - val2;
        paidOption.value = hasil;
        paidOption.setAttribute("value", hasil);
    }

    setInterval(hitungPaidOption, 500);
});