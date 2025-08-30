
from django.db import models
from django.utils.translation import gettext_lazy as _
from pkg_resources import require


class Form01aIdentity(models.Model):
    npwp = models.CharField(max_length=20)
    nwp = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    tax_year = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    spt_option = models.CharField(max_length=20)
    business_type = models.CharField(max_length=20)
    klu_code = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    facsimile = models.CharField(max_length=20)
    tax_status = models.CharField(max_length=20)
    spouse_npwp = models.CharField(max_length=20)

    class Meta:
        verbose_name = _('Form01aIdentity')
        verbose_name_plural = _('Form01aIdentities')

    def __str__(self):
        return self.npwp

class Form01aSheet1770(models.Model):
    id_form01aIdentity = models.ForeignKey(Form01aIdentity, on_delete=models.CASCADE)

    # net_domestic_income = formula
    employment_net_income = models.CharField(max_length=20)
    other_net_domestic_income = models.CharField(max_length=20)
    foreign_net_income = models.CharField(max_length=20)
    # total_net_income = formula
    zakat = models.CharField(max_length=20)
    # net_income_after_zakat = formula

    loss_compensation = models.CharField(max_length=20)
    # net_income_after_compensation = formula
    non_taxable_income = models.CharField(max_length=20)
    non_taxable_income_option = models.CharField(max_length=20)
    # taxable_income = formula

    tax_payable = models.CharField(max_length=20)
    tax_reduction = models.CharField(max_length=20)
    # total_tax_payable = formula

    withheld_income_tax = models.CharField(max_length=20)
    tax_credit_option = models.CharField(max_length=20)
    tax_credit_option_field  = models.CharField(max_length=20)
    self_assessed_income_tax_1 = models.CharField(max_length=20)
    self_assessed_income_tax_2 = models.CharField(max_length=20)
    # total_tax_credit = formula

    paid_option_income_tax = models.CharField(max_length=20)
    settlement_date = models.DateField()
    # paid_option_income_tax_field = formula
    application_option = models.CharField(max_length=20)

    income_tax_installment = models.CharField(max_length=20)
    income_tax_installment_option = models.CharField(max_length=20)

    attachment_option = models.JSONField()

    tax_option = models.CharField(max_length=20)
    form_date = models.DateField()

    class Meta:
        verbose_name = _('Form01a_Sheet_1770')
        verbose_name_plural = _('Form01a_Sheet_1770')

    def __str__(self):
        return self.id_form01aIdentity

class Form01aSheet1770IHal1(models.Model):
    id_form01aIdentity = models.ForeignKey(Form01aIdentity, on_delete=models.CASCADE)

    book_keeping_option = models.CharField(max_length=20)
    public_accountant = models.CharField(max_length=255)
    public_accountant_npwp = models.CharField(max_length=20)
    public_accountant_office = models.CharField(max_length=255)
    public_accountant_office_npwp = models.CharField(max_length=20)
    tax_consultant = models.CharField(max_length=255)
    tax_consultant_npwp =  models.CharField(max_length=20)
    tax_consultant_office = models.CharField(max_length=255)
    tax_consultant_office_npwp = models.CharField(max_length=80)

    business_turnover = models.CharField(max_length=20)
    cost_of_goods_sold = models.CharField(max_length=20)
    # total_gross_revenue  = formula
    business_expenses = models.CharField(max_length=20)
    # net_income = formula

    personal_expenses = models.CharField(max_length=20)
    insurance_premium = models.CharField(max_length=20)
    compensation = models.CharField(max_length=20)
    excess_rp_payment = models.CharField(max_length=20)
    gifted_assets = models.CharField(max_length=20)
    income_tax = models.CharField(max_length=20)
    owner_salary = models.CharField(max_length=20)
    administrative_sanction = models.CharField(max_length=20)
    positive_depreciation_difference = models.CharField(max_length=20)
    income_maintenance_expenses = models.CharField(max_length=20)
    positive_fiscal_adjustment = models.CharField(max_length=20)
    # total_positive_fiscal_adjustment = formula

    business_turnover_income = models.CharField(max_length=20)
    negative_depreciation_difference = models.CharField(max_length=20)
    negative_fiscal_adjustment = models.CharField(max_length=20)
    # total_negative_fiscal_adjustment = formula

    # total_side_a = formula

    class Meta:
        verbose_name = _('Form01a_1770_I_Hal1')
        verbose_name_plural = _('Form01a_1770_I_Hal1s')

    def __str__(self):
        return self.id_form01aIdentity

class Form01aSheet1770IHal2(models.Model):
    id_form01aIdentity = models.ForeignKey(Form01aIdentity, on_delete=models.CASCADE)

    trading_business_turnover  = models.CharField(max_length=20)
    trading_norms= models.CharField(max_length=20)
    net_trading_income = models.CharField(max_length=20)
    industry_business_turnover = models.CharField(max_length=20)
    industry_norms = models.CharField(max_length=20)
    net_industry_income = models.CharField(max_length=20)
    service_business_income = models.CharField(max_length=20)
    service_norms = models.CharField(max_length=20)
    net_service_income = models.CharField(max_length=20)
    hard_labor_business_turnover = models.CharField(max_length=20)
    hard_labor_norms = models.CharField(max_length=20)
    net_hard_labor_income = models.CharField(max_length=20)
    other_business_turnover = models.CharField(max_length=20)
    other_business_norms = models.CharField(max_length=20)
    net_other_business_income = models.CharField(max_length=20)

    total_net_interest = models.CharField(max_length=20)
    total_net_royalties = models.CharField(max_length=20)
    total_net_rental_income = models.CharField(max_length=20)
    total_net_prize = models.CharField(max_length=20)
    total_net_capital_gains = models.CharField(max_length=20)
    total_net_other_income = models.CharField(max_length=20)


    class Meta:
        verbose_name = _('Form01a_1770_I_Hal2')
        verbose_name_plural = _('Form01a_1770_I_Hal2s')

    def __str__(self):
        return self.id_form01aIdentity

class Form01aSheet1770Ihal2C(models.Model):
    id_form01aIdentity = models.ForeignKey(Form01aIdentity, on_delete=models.CASCADE)

    employer_npwp = models.CharField(max_length=255)
    gross_income = models.CharField(max_length=20)
    income_deduction = models.CharField(max_length=20)
    net_income = models.CharField(max_length=20)

    class Meta:
        verbose_name = _('Form01a_1770_I_hal2C')
        verbose_name_plural = _('Form01a_1770_I_hal2Cs')

class Form01aSheet1770II(models.Model):
    id_form01aIdentity = models.ForeignKey(Form01aIdentity, on_delete=models.CASCADE)

    withholder_name = models.CharField(max_length=255)
    withholder_npwp = models.CharField(max_length=20)
    receipt_number = models.CharField(max_length=20)
    receipt_date = models.DateField()
    tax_type = models.CharField(max_length=255)
    pph_amount = models.CharField(max_length=20)

    class Meta:
        verbose_name = _('Form01a_1770_II')
        verbose_name_plural = _('Form01a_1770_IIs')

    def __str__(self):
        return self.id_form01aIdentity

class Form01aSheet1770III(models.Model):
    id_form01aIdentity = models.ForeignKey(Form01aIdentity, on_delete=models.CASCADE)

    saving_tax_base = models.CharField(max_length=20)
    interest_tax_base = models.CharField(max_length=20)
    share_sale_tax_base = models.CharField(max_length=20)
    prize_tax_base = models.CharField(max_length=20)
    severance_pay_tax_base = models.CharField(max_length=20)
    honorarium_tax_base = models.CharField(max_length=20)
    transfer_of_land_right_tax_base = models.CharField(max_length=20)
    received_buildings_tax_base = models.CharField(max_length=20)
    land_lease_tax_base = models.CharField(max_length=20)
    construction_service_tax_base = models.CharField(max_length=20)
    distributor_tax_base = models.CharField(max_length=20)
    interest_on_deposits_pay_tax_base = models.CharField(max_length=20)
    derivative_income_tax_base = models.CharField(max_length=20)
    dividend_tax_base = models.CharField(max_length=20)
    wife_income_tax_base = models.CharField(max_length=20)
    other_income_tax_base = models.CharField(max_length=20)

    assistance_gross_income = models.CharField(max_length=20)
    inheritance_gross_income = models.CharField(max_length=20)
    partnership_gross_income = models.CharField(max_length=20)
    insurance_gross_income = models.CharField(max_length=20)
    scholarship_gross_income = models.CharField(max_length=20)
    foreign_income_expert_wna = models.CharField(max_length=20)
    non_taxable_benefit = models.CharField(max_length=20)
    natura_exempt_income = models.CharField(max_length=20)

    spouse_net_income = models.CharField(max_length=20)

    class Meta:
        verbose_name = _('Form01a_1770_III')
        verbose_name_plural = _('Form01a_1770_IIIs')

    def __str__(self):
        return self.id_form01aIdentity

class Form01aSheet1770IVA(models.Model):
    id_form01aIdentity = models.ForeignKey(Form01aIdentity, on_delete=models.CASCADE)

    asset_code = models.CharField(max_length=20)
    asset_name = models.CharField(max_length=255)
    acq_cost = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    class Meta:
        verbose_name = _('FormSpt_01a_IVA')
        verbose_name_plural = _('FormSpt_01a_IVAs')

    def __str__(self):
        return self.id_form01aIdentity

class Form01aSheet1770IVB(models.Model):
    id_form01aIdentity = models.ForeignKey(Form01aIdentity, on_delete=models.CASCADE)

    debt_code = models.CharField(max_length=20)
    lender_name = models.CharField(max_length=255)
    lender_address = models.CharField(max_length=255)
    loan_year = models.IntegerField()
    amount = models.IntegerField()

    class Meta:
        verbose_name = _('FormSpt_01a_IVB')
        verbose_name_plural = _('FormSpt_01a_IVBs')

    def __str__(self):
        return self.id_form01aIdentity

class Form01aSheet1770IVC(models.Model):
    id_form01aIdentity = models.ForeignKey(Form01aIdentity, on_delete=models.CASCADE)

    family_member_name = models.CharField(max_length=20)
    id_number = models.CharField(max_length=20)
    family_relationship = models.CharField(max_length=20)
    occupation = models.CharField(max_length=50)

    class Meta:
        verbose_name = _('FormSpt_01a_IVC')
        verbose_name_plural = _('FormSpt_01a_IVCs')

    def __str__(self):
        return self.id_form01aIdentity

class Form01aSheetPhMtCalculation(models.Model):
    id_form01aIdentity = models.ForeignKey(Form01aIdentity, on_delete=models.CASCADE)

    husband_net_domestic_income = models.CharField(max_length=20)
    wife_net_domestic_income = models.CharField(max_length=20)
    husband_net_domestic_employment_income = models.CharField(max_length=20)
    wife_net_domestic_employment_income = models.CharField(max_length=20)
    husband_net_foreign_income = models.CharField(max_length=20)
    wife_net_foreign_income = models.CharField(max_length=20)
    husband_net_income_after_zakat = models.CharField(max_length=20)
    wife_net_income_after_zakat = models.CharField(max_length=20)
    # husband_total = formula
    # wife_total = formula
    husband_loss_compensation = models.CharField(max_length=20)
    wife_loss_compensation = models.CharField(max_length=20)
    # husband_total_net_income = formula
    # wife_total_net_income = formula

    # spouse_total_net_income = formula
    non_taxable_income = models.CharField(max_length=20)
    # taxable_income = formula
    five_percen_income_tax_payable = models.CharField(max_length=20)
    fifteen_percen_income_tax_payable = models.CharField(max_length=20)
    twenty_five_percen_income_tax_payable = models.CharField(max_length=20)
    thirty_percen_income_tax_payable = models.CharField(max_length=20)
    # total_of_income_tax_payable = formula

    # income_tax_payable_borne_by_husband = formula
    # income_tax_payable_borne_by_wife = formula

    husband_name = models.CharField(max_length=255)
    husband_npwp = models.CharField(max_length=20)
    wife_name = models.CharField(max_length=255)
    wife_npwp = models.CharField(max_length=20)


    class Meta:
        verbose_name = _('Form01a_Ph_Mt_Calculation')
        verbose_name_plural = _('Form01a_Ph_Mt_Calculations')

    def __str__(self):
        return self.id_form01aIdentity

class Form01aSheetOpptPayment(models.Model):
    id_form01aIdentity = models.ForeignKey(Form01aIdentity, on_delete=models.CASCADE)

    oppt_business_place_npwp = models.CharField(max_length=20)
    oppt_address = models.CharField(max_length=255)
    retail_gross_income = models.CharField(max_length=20)
    income_tax_25_paid = models.CharField(max_length=20)

    class Meta:
        verbose_name = _('Form01a_Oppt_Payment')
        verbose_name_plural = _('Form01a_Oppt_Payment')

    def __str__(self):
        return self.id_form01aIdentity

class Form01aSheetPp462013Payment(models.Model):
    id_form01aIdentity = models.ForeignKey(Form01aIdentity, on_delete=models.CASCADE)

    pp46_npwp = models.CharField(max_length=20)
    tax_period = models.CharField(max_length=20)
    pp46_address = models.CharField(max_length=255)
    gross_turnover = models.CharField(max_length=20)
    final_pph_paid = models.CharField(max_length=20)

    class Meta:
        verbose_name = _('Form01a_Pp_46_2013_Payment')
        verbose_name_plural = _('Form01a_Pp_46_2013_Payment')

    def __str__(self):
        return self.id_form01aIdentity


class Form01bIdentity(models.Model):
    npwp = models.CharField(max_length=20)
    nwp = models.CharField(max_length=255)
    tax_year = models.IntegerField()
    businessType = models.CharField(max_length=255)
    businessCode = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    facsimile = models.CharField(max_length=20)
    tax_status = models.CharField(max_length=10)
    spouseNpwp = models.CharField(max_length=20)

    class Meta:
        verbose_name = _('Form01bIdentity')
        verbose_name_plural = _('Form01bIdentities')

    def __str__(self):
        return self.npwp

class Form01bSheet1770S(models.Model):
    id_form01bIdentity = models.IntegerField()

    employmentNetIncome = models.CharField(max_length=20)
    otherNetDomesticIncome = models.CharField(max_length=20)
    foreignNetIncome = models.CharField(max_length=20)
    # totalNetIncome = formula
    zakat = models.CharField(max_length=20)
    # netIncomeAfterZakat = formula

    nonTaxableIncome = models.CharField(max_length=20)
    nonTaxableIncomeOption = models.CharField(max_length=10)
    # taxableIncome = formula

    taxPayable = models.CharField(max_length=20)
    taxReduction = models.CharField(max_length=20)
    # totalTaxPayable = formula

    withheldIncomeTax = models.CharField(max_length=20)
    taxCreditOption = models.CharField(max_length=10)
    # taxCreditOption_field = formula
    selfAssessedIncomeTax_1 = models.CharField(max_length=20)
    selfAssessedIncomeTax_2 = models.CharField(max_length=20)
    # totalTaxCredit = formula

    paidOptionIncomeTax = models.CharField(max_length=10)
    settlementDate = models.DateField()
    # paidOptionIncomeTax_field = formula
    applicationOption = models.CharField(max_length=10)

    incomeTaxInstallment = models.CharField(max_length=20)
    incomeTaxInstallmentOption = models.CharField(max_length=10)

    attachmentOption = models.JSONField()

    taxOption = models.CharField(max_length=10)
    formDate = models.DateField()

    class Meta:
        verbose_name = _('Form01b_1770S')
        verbose_name_plural = _('Form01b_1770Ss')

    def __str__(self):
        return self.id_form01bIdentity

class Form01bLamp1(models.Model):
    id_form01bIdentity = models.IntegerField()

    interest = models.CharField(max_length=20)
    royalty = models.CharField(max_length=20)
    rent = models.CharField(max_length=20)
    reward = models.CharField(max_length=20)
    profit = models.CharField(max_length=20)
    other_income = models.CharField(max_length=20)
    # total_side_a = formula

    assistance = models.CharField(max_length=20)
    inheritance = models.CharField(max_length=20)
    partnership = models.CharField(max_length=20)
    insurance = models.CharField(max_length=20)
    scholarship = models.CharField(max_length=20)
    other_income_2 = models.CharField(max_length=20)
    # total_side_b = formula

    class Meta:
        verbose_name  = _('Form01bLamp1')
        verbose_name_plural = _('Form01bLamp1s')

    def __str__(self):
        return self.id_form01bIdentity

class Form01bLamp2(models.Model):
    id_form01bIdentity = models.IntegerField()

    saving_tax_base = models.CharField(max_length=20)
    # saving_income_tax_payable = formula
    interest_tax_base = models.CharField(max_length=20)
    # interest_income_tax_payable = formula
    sale_of_shares_tax_base = models.CharField(max_length=20)
    # sale_of_shares_income_tax_payable = formula
    prize_tax_base = models.CharField(max_length=20)
    # prize_income_tax_payable = formula
    severance_pay_tax_base = models.CharField(max_length=20)
    # severance_pay_income_tax_payable = formula
    honorarium_tax_base = models.CharField(max_length=20)
    # honorarium_income_tax_payable = formula
    transfer_of_land_rights_tax_base = models.CharField(max_length=20)
    # transfer_of_land_rights_income_tax_payable = formula
    lend_lease_tax_base = models.CharField(max_length=20)
    # land_lease_income_tax_payable = formula
    building_received_tax_base = models.CharField(max_length=20)
    # building_received_income_tax_payable = formula
    deposit_interest_tax_base = models.CharField(max_length=20)
    # deposit_interest_income_tax_payable = formula
    derivative_tax_base = models.CharField(max_length=20)
    # derivative_income_tax_payable = formula
    dividend_tax_base = models.CharField(max_length=20)
    # dividend_income_tax_payable = formula
    wife_income_tax_base = models.CharField(max_length=20)
    # wife_income_tax_payable = formula
    other_income_tax_base = models.CharField(max_length=20)
    # other_income_tax_payable = formula
    # total_side_a = formula

    class Meta:
        verbose_name = _('Form01bLamp2')
        verbose_name_plural = _('Form01bLamp2s')

    def __self__(self):
        return self.id_form01bIdentity

class Form01bPhMtCalculation(models.Model):
    id_form01bIdentity = models.IntegerField()

    husband_net_domestic_income = models.CharField(max_length=20)
    wife_net_domestic_income = models.CharField(max_length=20)
    husband_net_domestic_employment_income = models.CharField(max_length=20)
    wife_net_domestic_employment_income = models.CharField(max_length=20)
    other_husband_net_domestic_income = models.CharField(max_length=20)
    other_wife_net_domestic_income = models.CharField(max_length=20)
    husband_net_foreign_income = models.CharField(max_length=20)
    wife_net_foreign_income = models.CharField(max_length=20)
    husband_net_income_after_zakat = models.CharField(max_length=20)
    wife_net_income_after_zakat = models.CharField(max_length=20)
    husband_total = models.CharField(max_length=20)
    wife_total = models.CharField(max_length=20)
    husband_loss_compensation = models.CharField(max_length=20)
    wife_loss_compensation = models.CharField(max_length=20)
    # husband_total_net_income = formula
    # wife_total_net_income = formula

    # spouse_total_net_income = formula
    non_taxable_income = models.CharField(max_length=20)
    # taxable_income = formula
    five_percen_income_tax_payable = models.CharField(max_length=20)
    fifteen_percen_income_tax_payable = models.CharField(max_length=20)
    twenty_five_percen_income_tax_payable = models.CharField(max_length=20)
    thirty_percen_income_tax_payable = models.CharField(max_length=20)
    # total_of_income_tax_payable = formula

    # income_tax_payable_borne_by_husband = formula
    # income_tax_payable_borne_by_wife = formula

    husband_name = models.CharField(max_length=255)
    husband_npwp = models.CharField(max_length=20)
    wife_name = models.CharField(max_length=255)
    wife_npwp = models.CharField(max_length=20)


    class Meta:
        verbose_name = _('Form01bPhMtCalculation')
        verbose_name_plural = _('Form01bPhMtCalculations')

    def __self__(self):
        return self.id_form01bIdentity

class FormLamp1IncomeTaxWithholdingsList(models.Model):
    id_form01b_lamp1 = models.IntegerField()

    withholder_name = models.CharField(max_length=255)
    withholder_npwp = models.CharField(max_length=20)
    withholding_number = models.CharField(max_length=20)
    withholding_date = models.DateField()
    tax_type = models.CharField(max_length=255)
    withheld_income_tax = models.CharField(max_length=20)

    class Meta:
        verbose_name = _('FormLamp1IncomeTaxWithholdingsList')
        verbose_name_plural = _('FormLamp1IncomeTaxWithholdingsLists')

    def __self__(self):
        return self.id_form01b_lamp1

class FormLamp2YearEndAssets(models.Model):
    id_form01b_lamp2 = models.IntegerField()

    code = models.CharField(max_length=20)
    name = models.CharField(max_length=255)
    year = models.IntegerField()
    price = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    class Meta:
        verbose_name = _('FormLamp2YearEndAsset')
        verbose_name_plural = _('FormLamp2YearEndAssets')

    def __self__(self):
        return self.id_form01b_lamp2

class FormLamp2YearEndDebt(models.Model):
    id_form01b_lamp2 = models.IntegerField()

    code_debt = models.CharField(max_length=20)
    lender_name = models.CharField(max_length=255)
    lender_address = models.CharField(max_length=255)
    year_debt = models.IntegerField()
    total = models.CharField(max_length=20)

    class Meta:
        verbose_name = _('FormLamp2YearEndDebt')
        verbose_name_plural = _('FormLamp2YearEndDebt')

    def __self__(self):
        return self.id_form01b_lamp2

class FormLamp2FamilyMemberList(models.Model):
    id_form01b_lamp2 = models.IntegerField()

    name = models.CharField(max_length=255)
    family_member_id = models.CharField(max_length=20)
    family_relation = models.CharField(max_length=255)
    jobs = models.CharField(max_length=255)

    class Meta:
        verbose_name = _('FormLamp2FamilyMemberList')
        verbose_name_plural = _('FormLamp2FamilyMemberLists')

    def __self__(self):
        return self.id_form01b_lamp2


class Form01c(models.Model):
    nwp = models.CharField(max_length=255)
    npwp = models.CharField(max_length=20)
    tax_year = models.IntegerField()
    date = models.DateField()

    gross_income = models.CharField(max_length=20)
    deduction = models.CharField(max_length=20)
    non_taxable_income_option = models.CharField(max_length=10)
    non_taxable_income = models.CharField(max_length=20)
    taxable_income = models.CharField(max_length=20)
    income_tax_payable = models.CharField(max_length=20)
    withheld_income_tax = models.CharField(max_length=20)
    income_tax_option = models.CharField(max_length=10)
    income_tax_option_field = models.CharField(max_length=20)

    tax_base = models.CharField(max_length=20)
    final_income_tax_payable = models.CharField(max_length=20)
    income_exempt_from_tax = models.CharField(max_length=20)

    yearEnd_total = models.CharField(max_length=20)
    yearEnd_tax_liability = models.CharField(max_length=20)

    class Meta:
        verbose_name = _('Form01c')
        verbose_name_plural = _('Form01cs')

    def __str__(self):
        return self.npwp


class FormSptPPN1111Header(models.Model):
    pkp_name  = models.CharField(max_length=255)
    pkp_address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    hp_number = models.CharField(max_length=20)
    klu_code = models.CharField(max_length=20)
    npwp = models.CharField(max_length=20)
    start_date = models.DateField()
    expire_date = models.DateField()

    class Meta:
        verbose_name = _('FormSpt_PPN1111_Header')
        verbose_name_plural = _('FormSpt_PPN1111s_Headers')

    def __str__(self):
        return self.pkp_name

class FormSptPPN1111(models.Model):
    id_formSpt_ppn1111_header = models.ForeignKey(FormSptPPN1111Header, on_delete=models.CASCADE)

    # I. Delivery of goods and services
    # PPN Payable (side-A)
    # DPP Value
    dpp_export_value = models.CharField(max_length=20)
    dpp_self_assessed_value = models.CharField(max_length=20)
    dpp_collected_by_collector_value = models.CharField(max_length=20)
    dpp_not_collected_value = models.CharField(max_length=20)
    dpp_exempt_from_ppn_value = models.CharField(max_length=20)
    # dpp_total = formula

    # PPN Value
    ppn_export_value = models.CharField(max_length=20)
    ppn_self_assessed_value = models.CharField(max_length=20)
    ppn_collected_by_collector_value = models.CharField(max_length=20)
    ppn_not_collected_value = models.CharField(max_length=20)
    exempt_from_ppn_value = models.CharField(max_length=20)
    # ppn_total = formula

    # (side-B)
    no_subject_to_ppn = models.CharField(max_length=20)

    # (side-C)
    # total_all_deliveries = formula

    # II. Calculation of Underpaid/Overpaid PPN
    # output_tax_self_assessment = formula
    prepaid_ppn = models.CharField(max_length=20)
    input_tax = models.CharField(max_length=20)
    # underpaid_or_overpaid_ppn = formula
    underpaid_or_overpaid_ppn_on_corrected_spt = models.CharField(max_length=20)
    # underpaid_or_overpaid_ppn_due_to_correction = formula
    settlement_of_underpaid_ppn = models.DateField()
    ntpp_code_1 = models.CharField(max_length=20)

    # Option Side
    overpaid_ppn_option = models.CharField(max_length=20)
    overpayer_of_ppn_option = models.CharField(max_length=20)
    request_for_excess_ppn_option = models.CharField(max_length=20)
    refund_for_pkp_option = models.CharField(max_length=20)

    # III. PPN Payable on Self-Constructed Activities
    tax_base = models.CharField(max_length=20)
    # ppn_payable_1 = formula
    settlement_of_ppn_payable_1 = models.DateField()
    ntpp_code_2 = models.CharField(max_length=20)

    # IV. Refund of input tax for PPN-Registered taxpayers who failed to produce
    ppn_payable_2 = models.CharField(max_length=20)
    settlement_of_ppn_payable_2 = models.DateField()
    ntpp_code_3 = models.CharField(max_length=20)

    # V. Luxury goods sales tax
    ppn_on_luxury_goods_self_assessed = models.CharField(max_length=20)
    prepaid_ppn_on_luxury_goods = models.CharField(max_length=20)
    # underpaid_or_overpaid_ppn_on_luxury_goods = formula
    underpaid_or_overpaid_ppn_on_luxury_goods_on_corrected_spt = models.CharField(max_length=20)
    # underpaid_or_overpaid_ppn_on_luxury_goods_due_to_correction = formula
    settlement_of_ppn_on_luxury_goods  = models.DateField()
    ntpp_code_4 = models.CharField(max_length=20)

    # VI. SPT Requirements
    spt_requirements_option = models.JSONField()

    # Footer
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)

    # Option Side
    form_option = models.CharField(max_length=20)

    class Meta:
        verbose_name = _('FormSpt_PPN1111')
        verbose_name_plural = _('FormSpt_PPN1111s')

    def __str__(self):
        return self.id_formSpt_ppn1111_header

class FormSptPPN1111AB(models.Model):
    id_formSpt_ppn1111_header = models.ForeignKey(FormSptPPN1111Header, on_delete=models.CASCADE)

    # I. Recap of Deliveries
    # I.A.Export of Tangible BKP/Intangible BKP/JKP
    # dpp_of_export_of_bkp_or_jkp = formula

    # I.B.Domestic Delivery (DPP)
    # dpp_of_with_tax_invoices_not_stated = formula
    dpp_of_with_tax_invoices_stated = models.CharField(max_length=20)
    # I.B.Domestic Delivery (PPN)
    ppn_of_with_tax_invoices_not_stated = models.CharField(max_length=20)
    ppn_of_with_tax_invoices_stated = models.CharField(max_length=20)
    # I.B.Domestic Delivery (PPnBM)
    ppnbm_of_with_tax_invoices_not_stated = models.CharField(max_length=20)
    ppnbm_of_with_tax_invoices_stated = models.CharField(max_length=20)

    # I.C.Details of Domestic Deliveries (DPP)
    dpp_of_self_assessed = models.CharField(max_length=20)
    dpp_of_collected_by_ppn_collector = models.CharField(max_length=20)
    dpp_of_not_collected = models.CharField(max_length=20)
    dpp_of_exempt_from_ppn = models.CharField(max_length=20)
    # I.C.Details of Domestic Deliveries (PPN)
    ppn_of_self_assessed  = models.CharField(max_length=20)
    ppn_of_collected_by_ppn_collector = models.CharField(max_length=20)
    ppn_of_not_collected = models.CharField(max_length=20)
    ppn_of_exempt_from_ppn = models.CharField(max_length=20)
    # I.C.Details of Domestic Deliveries (PPnBM)
    ppnbm_of_self_assessed = models.CharField(max_length=20)
    ppnbm_of_collected_by_ppn_collector = models.CharField(max_length=20)
    ppnbm_of_not_collected = models.CharField(max_length=20)
    ppnbm_of_exempt_from_ppn = models.CharField(max_length=20)

    # II. Recap of Acquisition (DPP)
    dpp_of_bkp_import = models.CharField(max_length=20)
    dpp_of_acquisition_of_bkp_or_jkp = models.CharField(max_length=20)
    dpp_of_acquisition_import = models.CharField(max_length=20)
    # total_of_dpp = formula

    # II. Recap of Acquisition (PPN)
    ppn_of_bkp_import = models.CharField(max_length=20)
    ppn_of_acquisition_of_bkp_or_jkp = models.CharField(max_length=20)
    ppn_of_acquisition_import = models.CharField(max_length=20)
    # total_of_ppn = formula

    # II. Recap of Acquisition (PPnBM)
    ppnbm_of_bkp_import = models.CharField(max_length=20)
    ppnbm_of_acquisition_of_bkp_or_jkp = models.CharField(max_length=20)
    ppnbm_of_acquisition_import = models.CharField(max_length=20)
    # total_of_ppnbm = formula

    # III. Calculation of Creditable Input Tax
    # III. A. Input Tax on Purchases that Can Be Credited
    # ppn_of_input_tax = formula

    # III. B.Other Input Tax
    ppn_of_compensation_of_excess_ppn = models.CharField(max_length=20)
    ppn_of_compensation_due_to_correction = models.CharField(max_length=20)
    ppn_of_recalculated_result = models.CharField(max_length=20)
    # ppn_of_total_calculation = formula

    # III. C. Total Input Tax that Can Be Credited
    # total_of_input_tax = formula

    class Meta:
        verbose_name = _('FormSpt_PPN1111_AB')
        verbose_name_plural = _('FormSpt_PPN1111_ABs')

    def __str__(self):
        return self.id_formSpt_ppn1111_header

class FormSptPPN1111A1(models.Model):
    id_formSpt_ppn1111_header = models.ForeignKey(FormSptPPN1111Header, on_delete=models.CASCADE)

    bkp_buyer_name = models.CharField(max_length=255)
    document_number = models.IntegerField()
    document_date = models.DateField()
    dpp_value = models.CharField(max_length=20)
    description = models.CharField(max_length=255)

    class Meta:
        verbose_name = _('FormSpt_PPN1111_A1')
        verbose_name_plural = _('FormSpt_PPN1111_A1s')

    def __str__(self):
        return self.id_formSpt_ppn1111_header

class FormSptPPN1111A2(models.Model):
    id_formSpt_ppn1111_header = models.ForeignKey(FormSptPPN1111Header, on_delete=models.CASCADE)

    bkp_buyer_name = models.CharField(max_length=255)
    npwp_number = models.CharField(max_length=20)
    tax_invoice_serial_number = models.CharField(max_length=20)
    tax_invoice_date = models.DateField()
    dpp_value = models.CharField(max_length=20)
    ppn_value = models.CharField(max_length=20)
    ppnbm_value = models.CharField(max_length=20)
    changed_tax_invoice_serial_number = models.CharField(max_length=20)

    class Meta:
        verbose_name = _('FormSpt_PPN1111_A2')
        verbose_name_plural = _('FormSpt_PPN1111_A2s')

    def __str__(self):
        return self.id_formSpt_ppn1111_header

class FormSptPPN1111B1(models.Model):
    id_formSpt_ppn1111_header = models.ForeignKey(FormSptPPN1111Header, on_delete=models.CASCADE)

    bkp_saler_name = models.CharField(max_length=255)
    document_number = models.IntegerField()
    document_date = models.DateField()
    dpp_value = models.CharField(max_length=20)
    ppn_value = models.CharField(max_length=20)
    ppnbm_value = models.CharField(max_length=20)
    description = models.CharField(max_length=255)

    class Meta:
        verbose_name = _('FormSpt_PPN1111_B1')
        verbose_name_plural = _('FormSpt_PPN1111_B1s')

    def __str__(self):
        return self.id_formSpt_ppn1111_header

class FormSptPPN1111B2(models.Model):
    id_formSpt_ppn1111_header = models.ForeignKey(FormSptPPN1111Header, on_delete=models.CASCADE)

    bkp_saler_name = models.CharField(max_length=255)
    npwp_number = models.CharField(max_length=20)
    tax_invoice_serial_number = models.CharField(max_length=20)
    tax_invoice_date = models.DateField()
    dpp_value = models.CharField(max_length=20)
    ppn_value = models.CharField(max_length=20)
    ppnbm_value = models.CharField(max_length=20)
    changed_tax_invoice_serial_number = models.CharField(max_length=255)

    class Meta:
        verbose_name = _('FormSpt_PPN1111_B2')
        verbose_name_plural = _('FormSpt_PPN1111_B2s')

    def __str__(self):
        return self.id_formSpt_ppn1111_header

class FormSptPPN1111B3(models.Model):
    id_formSpt_ppn1111_header = models.ForeignKey(FormSptPPN1111Header, on_delete=models.CASCADE)

    bkp_saler_name = models.CharField(max_length=255)
    npwp_number = models.CharField(max_length=20)
    tax_invoice_serial_number = models.CharField(max_length=20)
    tax_invoice_date = models.DateField()
    dpp_value = models.CharField(max_length=20)
    ppn_value = models.CharField(max_length=20)
    ppnbm_value = models.CharField(max_length=20)
    changed_tax_invoice_serial_number = models.CharField(max_length=255)

    class Meta:
        verbose_name = _('FormSpt_PPN1111_B3')
        verbose_name_plural = _('FormSpt_PPN1111_B3s')

    def __str__(self):
        return self.id_formSpt_ppn1111_header


