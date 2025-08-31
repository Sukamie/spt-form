document.addEventListener("DOMContentLoaded", function () {

    /* ========================================================
       1. KALKULASI TOTAL OTOMATIS 1770-III Side A
    ======================================================== */
    const sideA1770III_fields = [
        'id_saving_income_tax_payable',
        'id_interest_income_tax_payable',
        'id_share_sale_income_tax_payable',
        'id_prize_income_tax_payable',
        'id_severance_pay_income_tax_payable',
        'id_honorarium_income_tax_payable',
        'id_transfer_of_land_right_income_tax_payable',
        'id_received_buildings_income_tax_payable',
        'id_land_lease_income_tax_payable',
        'id_construction_service_income_tax_payable',
        'id_distributor_income_tax_payable',
        'id_interest_on_deposits_income_tax_payable',
        'id_derivative_income_tax_payable',
        'id_dividend_income_tax_payable',
        'id_wife_income_tax_payable',
        'id_other_income_tax_payable',
    ];
    const totalSideA1770III = document.getElementById('id_total_final_income');

    function calculateSideA1770IIITotal() {
        let total = 0;
        sideA1770III_fields.forEach(id => {
            const el = document.getElementById(id);
            total += parseFloat(el?.value) || 0;
        });
        if (totalSideA1770III) totalSideA1770III.value = total.toFixed(2);
    }


    /* ========================================================
       2. KALKULASI TOTAL OTOMATIS 1770-I-Hal 2 Side B
    ======================================================== */
    const sideB_1770IHal2_fields = [
        'id_net_trading_income',
        'id_net_industry_income',
        'id_net_service_income',
        'id_net_hard_labor_income',
        'id_net_other_business_income'
    ];
    const totalSideB_1770IHal2 = document.getElementById('id_total_net_income_b');

    function calculateSideB_1770IHal2Total() {
        let total = 0;
        sideB_1770IHal2_fields.forEach(id => {
            const el = document.getElementById(id);
            total += parseFloat(el?.value) || 0;
        });
        if (totalSideB_1770IHal2) totalSideB_1770IHal2.value = total.toFixed(2);
    }


    /* ========================================================
       3. KALKULASI TOTAL OTOMATIS 1770-I-Hal 2 Side D
    ======================================================== */
    const sideD_1770IHal2_fields = [
        'id_total_net_interest',
        'id_total_net_royalties',
        'id_total_net_rental_income',
        'id_total_net_prize',
        'id_total_net_capital_gains',
        'id_total_net_other_income'
    ];
    const totalSideD_1770IHal2 = document.getElementById('id_total_net_income_d');

    function calculateSideD_1770IHal2Total() {
        let total = 0;
        sideD_1770IHal2_fields.forEach(id => {
            const el = document.getElementById(id);
            total += parseFloat(el?.value) || 0;
        });
        if (totalSideD_1770IHal2) totalSideD_1770IHal2.value = total.toFixed(2);
    }


    /* ========================================================
       4. KALKULASI TOTAL Side B (1770-III-B)
    ======================================================== */
    const sideBFields = [
        'id_assistance_gross_income',
        'id_inheritance_gross_income',
        'id_partnership_gross_income',
        'id_insurance_gross_income',
        'id_scholarship_gross_income',
        'id_other_gross_income',
    ];
    const totalSideB = document.getElementById('id_total_side_b');

    function calculateSideBTotal() {
        let total = 0;
        sideBFields.forEach(id => {
            const el = document.getElementById(id);
            total += parseFloat(el?.value.replace(/,/g, '')) || 0;
        });
        if (totalSideB) totalSideB.value = total;
    }


    /* ========================================================
       5. KALKULASI TOTAL OTHER GROSS INCOME (1770-III-B)
    ======================================================== */
    const sideB_otherGrossIncome_fields = [
        'id_foreign_income_expert_wna',
        'id_non_taxable_benefit',
        'id_natura_exempt_income',
    ];
    const totalSideB_otherGrossIncome = document.getElementById('id_other_gross_income');

    function calculateSideB_otherGrossIncomeTotal() {
        let total = 0;
        sideB_otherGrossIncome_fields.forEach(id => {
            const el = document.getElementById(id);
            total += parseFloat(el?.value.replace(/,/g, '')) || 0;
        });
        if (totalSideB_otherGrossIncome) totalSideB_otherGrossIncome.value = total;
    }


    /* ========================================================
       6. FUNGSI KALKULASI UMUM
    ======================================================== */

    // Perhitungan dengan multiplier tetap
    function autoCalc(baseId, resultId, multiplier) {
        const baseInput = document.getElementById(baseId);
        const resultInput = document.getElementById(resultId);

        function calculate() {
            const baseValue = parseFloat(baseInput.value) || 0;
            resultInput.value = (baseValue * multiplier).toFixed(2);
            calculateSideA1770IIITotal();
        }

        baseInput?.addEventListener("input", calculate);
    }

    // Perhitungan dengan multiplier dari field lain
    function autoCalcWithField(baseId, percentageId, resultId) {
        const baseInput = document.getElementById(baseId);
        const percentageInput = document.getElementById(percentageId);
        const resultInput = document.getElementById(resultId);

        function calculate() {
            const baseValue = parseFloat(baseInput.value) || 0;
            const percentageValue = parseFloat(percentageInput.value) || 0;
            resultInput.value = (baseValue * (percentageValue / 100)).toFixed(2);
            calculateSideA1770IIITotal();
        }

        baseInput?.addEventListener("input", calculate);
        percentageInput?.addEventListener("input", calculate);
    }

    // Perhitungan berdasarkan pilihan dropdown
    function autoCalcSelect(selectId, baseId, resultId, rateMap) {
        const selectInput = document.getElementById(selectId);
        const baseInput = document.getElementById(baseId);
        const resultInput = document.getElementById(resultId);

        function calculate() {
            const baseValue = parseFloat(baseInput.value) || 0;
            const multiplier = rateMap[selectInput.value] || 0;
            resultInput.value = (baseValue * multiplier).toFixed(2);
            calculateSideA1770IIITotal();
        }

        selectInput?.addEventListener("change", calculate);
        baseInput?.addEventListener("input", calculate);
    }


    // Perhitungan Kabataku dengan field lain
    function kabatakuCalcWithField(baseId, base2Id, resultId) {
        const baseInput = document.getElementById(baseId);
        const base2Input = document.getElementById(base2Id);
        const resultInput = document.getElementById(resultId);

        function calculate() {
            const baseValue = parseFloat(baseInput.value) || 0;
            const base2Value = parseFloat(base2Input.value) || 0;

            const result = baseValue - base2Value;
            resultInput.value = result.toFixed(2);
        }

        baseInput?.addEventListener("input", calculate);
        base2Input?.addEventListener("input", calculate);
    }

    // Perhitungan Kabataku dengan field lain (readonly)
    function kabatakuCalcWithRField(baseId, base2Id, resultId) {
        const baseInput = document.getElementById(baseId);
        const base2Input = document.getElementById(base2Id);
        const resultInput = document.getElementById(resultId);

        function calculate() {
            const baseVal = parseFloat(baseInput?.value) || 0;
            const base2Val = parseFloat(base2Input?.value) || 0;
            resultInput.value = (baseVal - base2Val).toFixed(2);

        }

        baseInput?.addEventListener("input", calculate);
        base2Input?.addEventListener("input", calculate);

        calculate();
    }


    /* ========================================================
       7. PERHITUNGAN DENGAN ROW (Event Delegation)
    ======================================================== */
    function setupGrossTurnoverDelegation(tableId, multiplier = 0.005) {
        const tbody = document.querySelector(`#${tableId} tbody`);
        if (!tbody) return;

        tbody.addEventListener("input", function (e) {
            if (e.target.classList.contains("gross_turnover")) {
                const value = parseFloat(e.target.value.replace(/,/g, "")) || 0;
                const row = e.target.closest("tr");
                const resultInput = row?.querySelector(".final_pph_paid");
                if (resultInput) {
                    resultInput.value = (value * multiplier).toFixed(2);
                }
                calculatePP46Total();
            }
        });
    }

    function calculatePP46Total() {
        let total = 0;
        document.querySelectorAll(".final_pph_paid").forEach(input => {
            total += parseFloat(input.value) || 0;
        });
        const totalInput = document.getElementById("id_total_pp46");
        if (totalInput) totalInput.value = total.toFixed(2);
    }


    /* ========================================================
       8. KALKULASI TOTAL OTOMATIS 1770-I-Hal-1 Side 2
    ======================================================== */

    const side2_1770IHal1_fields = [
        'id_personal_expenses',
        'id_insurance_premium',
        'id_compensation',
        'id_excess_rp_payment',
        'id_gifted_assets',
        'id_income_tax',
        'id_owner_salary',
        'id_administrative_sanction',
        'id_positive_depreciation_difference',
        'id_income_maintenance_expenses',
        'id_positive_fiscal_adjustment',
    ];
    const totalSide2_1770IHal1 = document.getElementById('id_total_positive_fiscal_adjustment');

    function calculateSide2_1770IHal1Total() {
        let total = 0;
        side2_1770IHal1_fields.forEach(id => {
            const el = document.getElementById(id);
            total += parseFloat(el?.value.replace(/,/g, '')) || 0;
        });
        if (totalSide2_1770IHal1) totalSide2_1770IHal1.value = total;
    }

    /* ========================================================
       9. KALKULASI TOTAL OTOMATIS 1770-I-Hal-1 Side 3
    ======================================================== */

    const side3_1770IHal1_fields = [
        'id_business_turnover_income',
        'id_negative_depreciation_difference',
        'id_negative_fiscal_adjustment',
    ];
    const totalSide3_1770IHal1 = document.getElementById('id_total_negative_fiscal_adjustment');

    function calculateSide3_1770IHal1Total() {
        let total = 0;
        side3_1770IHal1_fields.forEach(id => {
            const el = document.getElementById(id);
            total += parseFloat(el?.value.replace(/,/g, '')) || 0;
        });
        if (totalSide3_1770IHal1) totalSide3_1770IHal1.value = total;
    }



    /* ========================================================
       10. PEMANGGILAN FUNGSI KALKULASI
    ======================================================== */

    // Fixed rate
    autoCalc("id_saving_tax_base", "id_saving_income_tax_payable", 0.2);
    autoCalc("id_share_sale_tax_base", "id_share_sale_income_tax_payable", 0.001);
    autoCalc("id_prize_tax_base", "id_prize_income_tax_payable", 0.25);
    autoCalc("id_transfer_of_land_right_tax_base", "id_transfer_of_land_right_income_tax_payable", 0.025);
    autoCalc("id_land_lease_tax_base", "id_land_lease_income_tax_payable", 0.1);
    autoCalc("id_interest_on_deposits_pay_tax_base", "id_interest_on_deposits_income_tax_payable", 0.1);
    autoCalc("id_other_income_tax_base", "id_other_income_tax_payable", 0.005);

    // With-row
    setupGrossTurnoverDelegation("asset-table-5", 0.005);
    calculatePP46Total();

    // Field persen
    autoCalcWithField("id_severance_pay_tax_base", "id_percentage_for_severance_pay_income_tax_payable", "id_severance_pay_income_tax_payable");
    autoCalcWithField("id_honorarium_tax_base", "id_percentage_for_honorarium_income_tax_payable", "id_honorarium_income_tax_payable");
    autoCalcWithField("id_received_buildings_tax_base", "id_percentage_for_received_buildings_income_tax_payable", "id_received_buildings_income_tax_payable");
    autoCalcWithField("id_construction_service_tax_base", "id_percentage_for_construction_service_income_tax_payable", "id_construction_service_income_tax_payable");
    autoCalcWithField("id_derivative_income_tax_base", "id_percentage_for_derivative_income_tax_payable", "id_derivative_income_tax_payable");
    autoCalcWithField("id_wife_income_tax_base", "id_percentage_for_wife_income_tax_payable", "id_wife_income_tax_payable");

    // Dropdown rate
    autoCalcSelect("id_obligation_option", "id_interest_tax_base", "id_interest_income_tax_payable", { "1": 0.15, "2": 0.2 });
    autoCalcSelect("id_dividend_option", "id_dividend_tax_base", "id_dividend_income_tax_payable", { "1": 1, "2": 0.1 });
    autoCalcSelect("id_distributor_option", "id_distributor_tax_base", "id_distributor_income_tax_payable", { "1": 0.0025, "2": 0.003 });

    //Kabataku
    kabatakuCalcWithField("id_business_turnover", "id_cost_of_goods_sold", "id_total_gross_revenue");

    //With readonly Field
    kabatakuCalcWithRField("id_total_gross_revenue", "id_business_expenses", "id_net_income");


    /* ========================================================
       11. EVENT LISTENER UNTUK FIELD MANUAL
    ======================================================== */
    sideA1770III_fields.forEach(id => {
        document.getElementById(id)?.addEventListener('input', calculateSideA1770IIITotal);
    });
    sideB_1770IHal2_fields.forEach(id => {
        document.getElementById(id)?.addEventListener('input', calculateSideB_1770IHal2Total);
    });
    sideD_1770IHal2_fields.forEach(id => {
        document.getElementById(id)?.addEventListener('input', calculateSideD_1770IHal2Total);
    });
    sideBFields.forEach(id => {
        document.getElementById(id)?.addEventListener('input', calculateSideBTotal);
    });
    sideB_otherGrossIncome_fields.forEach(id => {
        document.getElementById(id)?.addEventListener('input', calculateSideB_otherGrossIncomeTotal);
    });
    side2_1770IHal1_fields.forEach(id => {
        document.getElementById(id)?.addEventListener('input', calculateSide2_1770IHal1Total);
    });
    side3_1770IHal1_fields.forEach(id => {
        document.getElementById(id)?.addEventListener('input', calculateSide3_1770IHal1Total);
    });

    /* ========================================================
       12. HITUNG NILAI AWAL
    ======================================================== */
    calculateSideB_1770IHal2Total();
    calculateSideD_1770IHal2Total();
    calculateSideBTotal();
    calculateSideB_otherGrossIncomeTotal();
    calculateSide2_1770IHal1Total();
    calculateSide3_1770IHal1Total();

});
