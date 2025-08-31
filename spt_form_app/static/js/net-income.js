// TOTAL NET INCOME
document.addEventListener("DOMContentLoaded", function () {
    const fieldIds = [
        "id_net_domestic_income",
        "id_employment_net_income",
        "id_other_net_domestic_income",
        "id_foreign_net_income"
    ];
    const totalField = document.getElementById("id_total_net_income");

    function getValue(el) {
        if (!el) return 0;
        let val = el.value || el.textContent || el.innerText || "0";
        return parseFloat(val.replace(/[^0-9.-]/g, "")) || 0;
    }

    function calculateTotal() {
        let sum = 0;
        fieldIds.forEach(id => {
            const el = document.getElementById(id);
            sum += getValue(el);
        });
        totalField.value = sum;
    }

    calculateTotal();
    const foreignField = document.getElementById("id_foreign_net_income");
    if (foreignField) {
        foreignField.addEventListener("input", calculateTotal);
    }
    fieldIds.slice(0, 3).forEach(id => {
        const el = document.getElementById(id);
        if (!el) return;
        const observer = new MutationObserver(calculateTotal);
        observer.observe(el, { attributes: true, attributeFilter: ["value"] });
        setInterval(calculateTotal, 1000);
    });
});

// AFTER ZAKAT
document.addEventListener("DOMContentLoaded", function () {
    const totalField = document.getElementById("id_total_net_income");
    const zakatField = document.getElementById("id_zakat");
    const resultField = document.getElementById("id_net_income_after_zakat");

    function getValue(el) {
        if (!el) return 0;
        let val = el.value || el.textContent || el.innerText || "0";
        return parseFloat(val.replace(/[^0-9.-]/g, "")) || 0;
    }

    function calculateResult() {
        const total = getValue(totalField);
        const zakat = getValue(zakatField);
        if (zakat > 0) {
            resultField.value = total - zakat;
        } else {
            resultField.value = "";
        }
    }

    zakatField.addEventListener("input", calculateResult);
});

// AFTER COMPENSATION
document.addEventListener("DOMContentLoaded", function () {
    const zakatResultField = document.getElementById("id_net_income_after_zakat");
    const lossCompField   = document.getElementById("id_loss_compensation");
    const resultField     = document.getElementById("id_net_income_after_compensation");

    function getValue(el) {
        if (!el) return 0;
        let val = el.value || el.textContent || el.innerText || "0";
        return parseFloat(val.replace(/[^0-9.-]/g, "")) || 0;
    }

    function calculateResult() {
        const zakatResult = getValue(zakatResultField);
        const lossComp = getValue(lossCompField);
        if (lossComp > 0) {
            resultField.value = zakatResult - lossComp;
        } else {
            resultField.value = "";
        }
    }

    lossCompField.addEventListener("input", calculateResult);
});

// TAXABLE INCOME
document.addEventListener("DOMContentLoaded", function () {
    const netAfterCompField = document.getElementById("id_net_income_after_compensation");
    const nonTaxableField   = document.getElementById("id_non_taxable_income");
    const taxableField      = document.getElementById("id_taxable_income");

    function getValue(el) {
        if (!el) return 0;
        let val = el.value || el.textContent || el.innerText || "0";
        return parseFloat(val.replace(/[^0-9.-]/g, "")) || 0;
    }

    function calculateTaxable() {
        const netAfterComp = getValue(netAfterCompField);
        const nonTaxable   = getValue(nonTaxableField);
        if (nonTaxable > 0) {
            taxableField.value = netAfterComp - nonTaxable;
        } else {
            taxableField.value = "";
        }
    }

    nonTaxableField.addEventListener("input", calculateTaxable);
});