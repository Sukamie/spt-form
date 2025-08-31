// TAX PAYABLE (versi id-ID)
document.addEventListener("DOMContentLoaded", function () {
    const payableField   = document.getElementById("id_tax_payable");
    const reductionField = document.getElementById("id_tax_reduction");
    const totalField     = document.getElementById("id_total_tax_payable");

    if (totalField) {
        totalField.readOnly = true;
    }

    function calcTotal() {
        const payable   = parseFloat(payableField.value.replace(/,/g, ""))   || 0;
        const reduction = parseFloat(reductionField.value.replace(/,/g, "")) || 0;
        const total = payable + reduction;
        totalField.value = total.toLocaleString("id-ID");
    }

    payableField.addEventListener("input", calcTotal);
    reductionField.addEventListener("input", calcTotal);
    calcTotal();
});

// TAX PAYABLE (versi default)
document.addEventListener("DOMContentLoaded", function () {
    const payableField   = document.getElementById("id_tax_payable");
    const reductionField = document.getElementById("id_tax_reduction");
    const totalField     = document.getElementById("id_total_tax_payable");

    function calcTotal() {
        const payable   = parseFloat(payableField.value.replace(/,/g, ""))   || 0;
        const reduction = parseFloat(reductionField.value.replace(/,/g, "")) || 0;
        const total = payable + reduction;
        totalField.value = total.toLocaleString();
    }

    payableField.addEventListener("input", calcTotal);
    reductionField.addEventListener("input", calcTotal);
});