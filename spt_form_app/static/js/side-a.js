document.addEventListener("DOMContentLoaded", function () {
    const netIncomeField   = document.getElementById("id_net_income");
    const positiveAdjField = document.getElementById("id_total_positive_fiscal_adjustment");
    const negativeAdjField = document.getElementById("id_total_negative_fiscal_adjustment");
    const totalSideAField  = document.getElementById("id_total_side_a");

    function getValue(el) {
        if (!el) return 0;
        let val = el.value || el.textContent || el.innerText || "0";
        return parseFloat(val.replace(/[^0-9.-]/g, "")) || 0;
    }

    function calculateTotalSideA() {
        const netIncome   = getValue(netIncomeField);
        const positiveAdj = getValue(positiveAdjField);
        const negativeAdj = getValue(negativeAdjField);
        const total = netIncome + positiveAdj - negativeAdj;
        if (totalSideAField) totalSideAField.value = total;
    }

    calculateTotalSideA();
    setInterval(calculateTotalSideA, 500);
});