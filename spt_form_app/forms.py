from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms


class Forms01a(forms.Form):
    SPT_OPTION_CHOICES = [
        ('', '-- Pilih Jenis SPT --'),
        ('1', 'PEMBUKUAN'),
        ('2', 'PENCATATAN'),
    ]

    TAX_STATUS_CHOICES = [
        ('', '-- Pilih Jenis Status Pajak --'),
        ('1', 'KK'),
        ('2', 'HB'),
        ('3', 'PH'),
        ('4', 'MT'),
    ]

    npwp = forms.CharField(max_length=20, label='NPWP')
    nwp = forms.CharField(max_length=255, label='Nama Wajib Pajak')
    address = forms.CharField(max_length=255, label='Alamat')
    tax_year = forms.IntegerField(label='Tahun Pajak')
    start_date = forms.DateField(label='Tanggal Mulai', widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(label='Tanggal Akhir', widget=forms.DateInput(attrs={'type': 'date'}))

    spt_option = forms.ChoiceField(
        choices=SPT_OPTION_CHOICES,
        label='Jenis SPT',
        widget=forms.Select(attrs={'class': 'form-control'})

    )

    business_type = forms.CharField(max_length=20, label='Jenis Usaha')
    klu_code = forms.CharField(max_length=20, label='Kode KLU')
    phone = forms.CharField(max_length=20, label='Telepon')
    facsimile = forms.CharField(max_length=20, label='Faksimile')

    tax_status = forms.ChoiceField(
        choices=TAX_STATUS_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Status Kewajiban Perpajakan Suami-Istri'
    )

    spouse_npwp = forms.CharField(max_length=20, label='NPWP Suami/Istri')

    total_asset = forms.CharField(
        max_length=20,
        label='Jumlah Bagian A',
        widget=forms.TextInput(attrs={'readonly': 'readonly'})
    )

    total_debt = forms.CharField(
        max_length=20,
        label='Jumlah Bagian B',
        widget=forms.TextInput(attrs={'readonly': 'readonly'})
    )

    total_retail_gross_income = forms.CharField(
        max_length=20,
        label='Jumlah Peredaran Bruto Pedagang Pengecer',
        widget=forms.TextInput(attrs={'readonly': 'readonly'})
    )

    total_income_tax_25_paid = forms.CharField(
        max_length=20,
        label='Jumlah PPh Pasal 25 Dibayar',
        widget=forms.TextInput(attrs={'readonly': 'readonly'})
    )

    total_gross_turnover = forms.CharField(
        max_length=20,
        label='Jumlah Peredaran Bruto',
        widget=forms.TextInput(attrs={'readonly': 'readonly'})

    )
    total_pph_final_paid = forms.CharField(
        max_length=20,
        label='Jumlah PPh Final Dibayar',
        widget=forms.TextInput(attrs={'readonly': 'readonly'})
    )

    # 1770-III
    total_pph_amount = forms.CharField(
        max_length=20,
        label='Jumlah PPh yang Dipotong/Dipungut',
        widget=forms.TextInput(attrs={'readonly': 'readonly'})
    )

    def __init__(self, *args, **kwargs):
        super(Forms01a, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

class Form01a1770III(forms.Form):
    OBLIGATION_OPTION = [
        ('', '-- Pilih Jenis Obligasi --'),
        ('1', 'Obligasi di Bursa'),
        ('2', 'Non-Bursa'),
    ]

    DIVIDEND_OPTION = [
        ('', '-- Pilih Jenis Dividen --'),
        ('1', 'Investasi'),
        ('2', 'Non-Investasi'),
    ]

    DISTRIBUTOR_OPTION  = [
        ('', '-- Pilih Jenis Distributor --'),
        ('1', 'Beli Langsung ke Pertamina'),
        ('2', 'Dari Agen'),
    ]

    OTHER_INCOME_OPTION  =[
        ('', '-- Pilih Jenis Penghasilan Lain --'),
        ('1', 'Tanpa PP23/PP55'),
        ('2','PP23/PP55')
    ]

    saving_tax_base = forms.CharField(max_length=20, label='Dasar Pengenaan Pajak/Penghasilan Bruto')
    saving_income_tax_payable = forms.CharField(
        max_length=20,
        label='PPh Terutang (Rupiah)',
        widget=forms.TextInput(attrs={'readonly': 'readonly'})
    )

    obligation_option = forms.ChoiceField(
        choices=OBLIGATION_OPTION,
        label='',
        widget=forms.Select(attrs={'class': 'form-control'}))

    interest_tax_base = forms.CharField(max_length=20, label='')
    interest_income_tax_payable = forms.CharField(
        max_length=20,
        label='',
        widget=forms.TextInput(attrs={'readonly': 'readonly'})
    )

    share_sale_tax_base = forms.CharField(max_length=20, label='')
    share_sale_income_tax_payable = forms.CharField(
        max_length=20,
        label='',
        widget=forms.TextInput(attrs={'readonly': 'readonly'})
    )

    prize_tax_base = forms.CharField(max_length=20, label='')
    prize_income_tax_payable = forms.CharField(
        max_length=20,
        label='',
        widget=forms.TextInput(attrs={'readonly': 'readonly'})
    )

    severance_pay_tax_base = forms.CharField(max_length=20, label='')
    percentage_for_severance_pay_income_tax_payable = forms.CharField(
        max_length=20,
        label='',
        widget=forms.TextInput(attrs={'placeholder': '(%)'})
    )

    severance_pay_income_tax_payable = forms.CharField(
        max_length=20,
        label='',
        widget=forms.TextInput(attrs={'readonly': 'readonly'})
    )

    honorarium_tax_base = forms.CharField(max_length=20, label='')
    percentage_for_honorarium_income_tax_payable = forms.CharField(
        max_length=20,
        label='',
        widget=forms.TextInput(attrs={'placeholder': '(%)'})
    )

    honorarium_income_tax_payable = forms.CharField(
        max_length=20,
        label='',
        widget=forms.TextInput(attrs={'readonly': 'readonly'})
    )

    transfer_of_land_right_tax_base = forms.CharField(max_length=20, label='')
    transfer_of_land_right_income_tax_payable = forms.CharField(
        max_length=20,
        label='',
        widget=forms.TextInput(attrs={'readonly': 'readonly'})
    )

    received_buildings_tax_base = forms.CharField(max_length=20, label='')
    percentage_for_received_buildings_income_tax_payable = forms.CharField(
        max_length=20,
        label='',
        widget=forms.TextInput(attrs={'placeholder': '(%)'})
    )

    received_buildings_income_tax_payable = forms.CharField(
        max_length=20,
        label='',
        widget=forms.TextInput(attrs={'readonly': 'readonly'})
    )

    land_lease_tax_base = forms.CharField(max_length=20, label='')
    land_lease_income_tax_payable = forms.CharField(
        max_length=20,
        label='',
        widget=forms.TextInput(attrs={'readonly': 'readonly'})
    )

    construction_service_tax_base = forms.CharField(max_length=20, label='')
    percentage_for_construction_service_income_tax_payable = forms.CharField(
        max_length=20,
        label='',
        widget=forms.TextInput(attrs={'placeholder': '(%)'})
    )

    construction_service_income_tax_payable = forms.CharField(
        max_length=20,
        label='',
        widget=forms.TextInput(attrs={'readonly': 'readonly'})
    )

    distributor_option = forms.ChoiceField(
        choices=DISTRIBUTOR_OPTION,
        label='',
        widget=forms.Select(attrs={'class': 'form-control'}))

    distributor_tax_base = forms.CharField(max_length=20, label='')
    distributor_income_tax_payable = forms.CharField(
        max_length=20,
        label='',
        widget=forms.TextInput(attrs={'readonly': 'readonly'})
    )

    interest_on_deposits_pay_tax_base = forms.CharField(max_length=20, label='')
    interest_on_deposits_income_tax_payable = forms.CharField(
        max_length=20,
        label='',
        widget=forms.TextInput(attrs={'readonly': 'readonly'})
    )

    derivative_income_tax_base = forms.CharField(max_length=20, label='')
    percentage_for_derivative_income_tax_payable = forms.CharField(
        max_length=20,
        label='',
        widget=forms.TextInput(attrs={'placeholder': '(%)'})
    )

    derivative_income_tax_payable = forms.CharField(
        max_length=20,
        label='',
        widget=forms.TextInput(attrs={'readonly': 'readonly'})
    )

    dividend_option = forms.ChoiceField(
        choices=DIVIDEND_OPTION,
        label='',
        widget=forms.Select(attrs={'class': 'form-control'}))

    dividend_tax_base = forms.CharField(max_length=20, label='')
    dividend_income_tax_payable = forms.CharField(
        max_length=20,
        label='',
        widget=forms.TextInput(attrs={'readonly': 'readonly'})
    )

    wife_income_tax_base = forms.CharField(max_length=20, label='')
    percentage_for_wife_income_tax_payable = forms.CharField(
        max_length=20,
        label='',
        widget=forms.TextInput(attrs={'placeholder': '(%)'})
    )

    wife_income_tax_payable = forms.CharField(
        max_length=20,
        label='',
        widget=forms.TextInput(attrs={'readonly': 'readonly'})
    )

    other_income_tax_base = forms.CharField(max_length=20, label='')

    other_income_option = forms.ChoiceField(
        choices=OTHER_INCOME_OPTION,
        label='',
        widget=forms.Select(attrs={'class': 'form-control'}))

    other_income_tax_payable = forms.CharField(
        max_length=20,
        label='',
        widget=forms.TextInput(attrs={'readonly': 'readonly'})
    )

    total_final_income = forms.CharField(
        max_length=20,
        label='',
        widget=forms.TextInput(attrs={'readonly': 'readonly'})
    )

    assistance_gross_income = forms.CharField(max_length=20, label='')
    inheritance_gross_income = forms.CharField(max_length=20, label='')
    partnership_gross_income = forms.CharField(max_length=20, label='')
    insurance_gross_income = forms.CharField(max_length=20, label='')
    scholarship_gross_income = forms.CharField(max_length=20, label='')

    other_gross_income = forms.CharField(
        max_length=20,
        label='',
        widget=forms.TextInput(attrs={'readonly': 'readonly'})
    )

    foreign_income_expert_wna = forms.CharField(max_length=20, label='')
    non_taxable_benefit = forms.CharField(max_length=20, label='')
    natura_exempt_income = forms.CharField(max_length=20, label='')
    total_side_b = forms.CharField(
        max_length=20,
        label='',
        widget=forms.TextInput(attrs={'readonly': 'readonly'})
    )

    spouse_net_income = forms.CharField(
        max_length=20, label='Penghasilan Neto Isteri/Suami yang Dikenakan Pajak Secara Terpisah')

    def __init__(self, *args, **kwargs):
        super(Form01a1770III, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

class Form01a1770IHal1(forms.Form):
    BOOK_KEEPING_CHOICES = [
        ('', '-- Pilih Jenis Pembukuan --'),
        ('1', 'Diaudit'),
        ('2', 'Tidak Diaudit'),
    ]

    book_keeping_option = forms.ChoiceField(
        choices=BOOK_KEEPING_CHOICES,
        label='Jenis Pembukuan',
        widget=forms.Select(attrs={'class': 'form-control'}))

    public_accountant = forms.CharField(max_length=255, label='Nama Akuntan Publik')
    public_accountant_npwp = forms.CharField(max_length=20, label='NPWP Akuntan Publik')
    public_accountant_office = forms.CharField(max_length=255, label='Nama Kantor Akuntan Publik')
    public_accountant_office_npwp = forms.CharField(max_length=20, label='NPWP Kantor Akuntan')

    tax_consultant = forms.CharField(max_length=255, label='Nama Konsultan Pajak')
    tax_consultant_npwp = forms.CharField(max_length=20, label='NPWP Konsultan Pajak')
    tax_consultant_office = forms.CharField(max_length=255, label='Nama Kantor Konsultan Pajak')
    tax_consultant_office_npwp = forms.CharField(max_length=80, label='NPWP Kantor Konsultan')

    business_turnover = forms.CharField(max_length=20, label='')
    cost_of_goods_sold = forms.CharField(max_length=20, label='')

    total_gross_revenue = forms.CharField(
        max_length=20,
        label='',
        widget=forms.TextInput(attrs={'readonly': 'readonly'})
    )

    business_expenses = forms.CharField(max_length=20, label='')

    net_income = forms.CharField(
        max_length=20,
        label='',
        widget=forms.TextInput(attrs={
            'readonly': 'readonly',
            'data-target': 'id_net_domestic_income'
        })
    )  # formula

    personal_expenses = forms.CharField(max_length=20, label='')
    insurance_premium = forms.CharField(max_length=20, label='')
    compensation = forms.CharField(max_length=20, label='')
    excess_rp_payment = forms.CharField(max_length=20, label='')
    gifted_assets = forms.CharField(max_length=20, label='')
    income_tax = forms.CharField(max_length=20, label='')
    owner_salary = forms.CharField(max_length=20, label='')
    administrative_sanction = forms.CharField(max_length=20, label='')
    positive_depreciation_difference = forms.CharField(max_length=20, label='')
    income_maintenance_expenses = forms.CharField(max_length=20, label='')
    positive_fiscal_adjustment = forms.CharField(max_length=20, label='')

    total_positive_fiscal_adjustment = forms.CharField(
        max_length=20,
        label='',
        widget=forms.TextInput(attrs={'readonly': 'readonly'})
    )  # formula

    business_turnover_income = forms.CharField(max_length=20, label='')
    negative_depreciation_difference = forms.CharField(max_length=20, label='')
    negative_fiscal_adjustment = forms.CharField(max_length=20, label='')

    total_negative_fiscal_adjustment = forms.CharField(
        max_length=20,
        label='',
        widget=forms.TextInput(attrs={'readonly': 'readonly'})
    )  # formula

    total_side_a = forms.CharField(
        max_length=20,
        label='',
        widget=forms.TextInput(attrs={'readonly': 'readonly'})
    ) # formula

    def __init__(self, *args, **kwargs):
        super(Form01a1770IHal1, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

class Form01a1770IHal2(forms.Form):
    trading_business_turnover = forms.CharField(max_length=20, label='Peredaran Usaha (Rupiah)')
    trading_norms = forms.CharField(max_length=20, label='Norma (%)')
    net_trading_income = forms.CharField(max_length=20, label='Penghasilan Neto (Rupiah)')

    industry_business_turnover = forms.CharField(max_length=20, label='')
    industry_norms = forms.CharField(max_length=20, label='')
    net_industry_income = forms.CharField(max_length=20, label='')

    service_business_income = forms.CharField(max_length=20, label='')
    service_norms = forms.CharField(max_length=20, label='')
    net_service_income = forms.CharField(max_length=20, label='')

    hard_labor_business_turnover = forms.CharField(max_length=20, label='')
    hard_labor_norms = forms.CharField(max_length=20, label='')
    net_hard_labor_income = forms.CharField(max_length=20, label='')

    other_business_turnover = forms.CharField(max_length=20, label='')
    other_business_norms = forms.CharField(max_length=20, label='')
    net_other_business_income = forms.CharField(max_length=20, label='')

    total_net_interest = forms.CharField(max_length=20, label='Jumlah Penghasilan Neto (Rupiah)')
    total_net_royalties = forms.CharField(max_length=20, label='')
    total_net_rental_income = forms.CharField(max_length=20, label='')
    total_net_prize = forms.CharField(max_length=20, label='')
    total_net_capital_gains = forms.CharField(max_length=20, label='')
    total_net_other_income = forms.CharField(max_length=20, label='')

    total_net_income_b = forms.CharField(
        max_length=20,
        label='Jumlah Bagian B',
        widget=forms.TextInput(attrs={'readonly': 'readonly'})
    )

    total_net_income_c = forms.CharField(
        max_length=20,
        label='Jumlah Bagian C',
        widget=forms.TextInput(attrs={
            'readonly': 'readonly',
            'data-target': 'id_employment_net_income'
        })
    )

    total_net_income_d = forms.CharField(
        max_length=20,
        label='Jumlah Bagian D',
        widget=forms.TextInput(attrs={
            'readonly': 'readonly',
            'data-target':  'id_other_net_domestic_income'
        })
    )

    def __init__(self, *args, **kwargs):
        super(Form01a1770IHal2, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

class Form1770(forms.Form):
    PTKP_OPTION_CHOICES = [
        ('', '-- Pilih Status PTKP --'),
        ('1', 'TK/'),
        ('2', 'K/'),
        ('3', 'K/I/'),
    ]

    PPH_OPTION_CHOICES = [
        ('', '-- Pilih Jenis PPh --'),
        ('1', 'PPh yang Harus Dibayar Sendiri'),
        ('2', 'PPh yang Lebih Dipotong/Dipungut'),
    ]

    PAID_OPTION_CHOICES = [
        ('', '-- Pilih Jenis PPh Kurang/Lebih Bayar --'),
        ('1', 'PPh yang Kurang Dibayar (PPh Pasal 29)'),
        ('2', 'PPh yang Lebih Dibayar (PPh Pasal 28 A)'),
    ]

    APPLICATION_OPTION_CHOICES = [
        ('', '-- Pilih Jenis Permohonan --'),
        ('1', 'Direstitusikan'),
        ('2', 'Diperhitungkan dengan Utang Pajak'),
        ('3', 'Dikembalikan dengan SKPPKP Pasal 17C (WP dengan Kriteria Tertentu)'),
        ('4', 'Dikembalikan dengan SKPPKP Pasal 17D (WP yang Memenuhi Persyaratan Tertentu)'),
    ]

    ATTACHMENT_OPTION_CHOICES = [
        ('1', 'Surat Kuasa Khusus (Bila Dikuasakan)'),
        ('2', 'SSP Lembar Ke-3 PPh Pasal 29'),
        ('3', 'Neraca dan Lap. Laba Rugi / Rekapitulasi Bulanan '
                'Peredaran Bruto dan/atau Penghasilan Lain dan Biaya '),

        ('4', 'Perhitungan Kompensasi Kerugian Fiskal'),
        ('5', 'Bukti Pemotongan/Pemungutan Oleh Pihak Lain/Ditanggung '
                'Pemerintah dan yang Dibayar/Dipotong di Luar Negeri'),

        ('6', 'Fotokopi Formulir 1721-A1 dan/atau 1721-A2 (........Lembar)'),
        ('7', 'Perhitungan Angsuran PPh Pasal 25 Tahun Pajak Berikutnya'),
        ('8', 'Perhitungan PPh Terutang Bagi Wajib Pajak Dengan Status Perpajakan PH atau MT'),
        ('9', 'Daftar Jumlah Penghasilan dan Pembayaran PPh Pasal 25 '
                 '(Khusus Untuk Orang Pribadi Pengusaha Tertentu)'),

        ('10', 'Daftar Jumlah Penghasilan Bruto dan Pembayaran PPh Final '
                  'Berdasarkan PP 46 Tahun 2013 Per Masa Pajak dan Per Tempat'),
    ]

    INCOME_TAX_INSTALLMENT_OPTION_CHOICES = [
        ('', '-- Pilih Dasar Perhitungan --'),
        ('1', '1/12 x Jumlah Pada Angka 16 '),
        ('2', 'Perhitungan Wajib Pajak Orang Pribadi Pengusaha Tertentu'),
        ('3', 'Perhitungan Dalam Lampiran Tersendiri'),
    ]

    TAX_OPTION_CHOICES = [
        ('', '-- Pilih Opsi Pajak --'),
        ('1', 'Wajib Pajak'),
        ('2', 'Kuasa'),
    ]

    net_domestic_income = forms.CharField(
        max_length=20,
        label='',
        widget=forms.TextInput(attrs={'readonly': 'readonly'})
    )

    employment_net_income = forms.CharField(
        max_length=20,
        label='',
        widget=forms.TextInput(attrs={'readonly': 'readonly'})
    )

    other_net_domestic_income = forms.CharField(
        max_length=20,
        label='',
        widget=forms.TextInput(attrs={'readonly': 'readonly'})
    )

    foreign_net_income = forms.CharField(max_length=20,label='',)

    total_net_income = forms.CharField(
        max_length=20,
        label='',
        widget=forms.TextInput(attrs={'readonly': 'readonly'})
    )

    zakat = forms.CharField(max_length=20, label='')
    net_income_after_zakat = forms.CharField(
        max_length=20,
        label='',
        widget=forms.TextInput(attrs={'readonly': 'readonly'})
    )

    loss_compensation = forms.CharField(max_length=20, label='8. Kompensasi Kerugian')
    net_income_after_compensation = forms.CharField(
        max_length=20,
        label='9. Jumlah Penghasilan Neto Setelah Kompensasi Kerugian (7-8)',
        widget=forms.TextInput(attrs={'readonly': 'readonly'})
    )

    ptkp_option = forms.ChoiceField(
        choices=PTKP_OPTION_CHOICES,
        label='Status PTKP',
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    ptkp_amount = forms.IntegerField(label='Jumlah PTKP')
    non_taxable_income = forms.CharField(max_length=20,label='10. Penghasilan Tidak Kena Pajak')

    taxable_income = forms.CharField(
        max_length=20,
        label='11. Penghasilan Kena Pajak (9-10)',
        widget=forms.TextInput(attrs={'readonly': 'readonly'})
    )

    tax_payable = forms.CharField(max_length=20, label='12. PPh Terutang (Tarif Pasal 17 UU PPh X Angka 11')
    tax_reduction = forms.CharField(max_length=20, label='13. Pengembalian/Pengurangan PPh Pasal 24 yang Telah Dikreditkan')
    total_tax_payable = forms.CharField(
        max_length=20,
        label='14. Jumlah PPh Terutang (12 + 13)',
        widget=forms.TextInput(attrs={'readonly': 'readonly'})
    )

    withheld_income_tax = forms.CharField(
        max_length=20,
        label='15. PPh yang Dipotong/Dipungut Oleh Pihak Lain, '
              'PPh yang Dibayar/Dipotong di Luar Negeri dan PPh Ditanggung Pemerintah',
        widget=forms.TextInput(attrs={'readonly': 'readonly'})
    )

    pph_option = forms.ChoiceField(
        choices=PPH_OPTION_CHOICES,
        label='Jenis PPh',
        widget=forms.Select(attrs={'class': 'form-control'}))


    pph_option_field = forms.CharField(
        max_length=20,
        label='16. Jumlah PPh',
        widget=forms.TextInput(attrs={'readonly': 'readonly'})
    )
    self_assessed_income_tax_1 = forms.CharField(max_length=20, label='17a. PPh Pasal 25 Bulanan')
    self_assessed_income_tax_2 = forms.CharField(max_length=20, label='17b. STP PPh Pasal 25 (Hanya Pokok Pajak)')
    total_tax_credit = forms.CharField(
        max_length=20,
        label='18. Jumlah Kredit Pajak (17a + 17b)',
        widget=forms.TextInput(attrs={'readonly': 'readonly'})
    )  # formula

    paid_option_income_tax = forms.ChoiceField(
        choices=PAID_OPTION_CHOICES,
        label='Jenis PPh Kurang/Lebih Bayar',
        widget=forms.Select(attrs={'class': 'form-control'}))

    settlement_date = forms.DateField(label='Tanggal Pelunasan', widget=forms.DateInput(attrs={'type': 'date'}))
    paid_option_income_tax_field = forms.CharField(
        max_length=20,
        label='19. Jumlah PPh yang Kurang/Lebih Bayar (16-18)',
        widget=forms.TextInput(attrs={'readonly': 'readonly'})
    )  # formula

    application_option = forms.ChoiceField(
        choices=APPLICATION_OPTION_CHOICES,
        label='20. Jenis Permohonan',
        widget=forms.Select(attrs={'class': 'form-control'}))

    income_tax_installment = forms.CharField(max_length=20, label='21. Jumlah Angsuran PPh Pasal 25 Tahun Pajak Berikutnya')
    income_tax_installment_option = forms.ChoiceField(
        choices=INCOME_TAX_INSTALLMENT_OPTION_CHOICES,
        label='Jenis Dasar Perhitungan',
        widget=forms.Select(attrs={'class': 'form-control'}))

    attachment_option = forms.MultipleChoiceField(
        choices=ATTACHMENT_OPTION_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label='Lampiran'
    )

    tax_option = forms.ChoiceField(
        choices=TAX_OPTION_CHOICES,
        label='Opsi Pajak',
        widget=forms.Select(attrs={'class': 'form-control'}))

    form_date = forms.DateField(label='Tanggal', widget=forms.DateInput(attrs={'type': 'date'}))

    def __init__(self, *args, **kwargs):
        super(Form1770, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

class Form01aPHMTCalculate(forms.Form):
    husband_net_domestic_income = forms.CharField(max_length=20, label='Penghasilan Neto Suami')
    wife_net_domestic_income = forms.CharField(max_length=20, label='Penghasilan Neto Istri')
    husband_net_domestic_employment_income = forms.CharField(max_length=20, label='')
    wife_net_domestic_employment_income = forms.CharField(max_length=20, label='')
    husband_net_foreign_income = forms.CharField(max_length=20, label='')
    wife_net_foreign_income = forms.CharField(max_length=20, label='')
    husband_net_income_after_zakat = forms.CharField(max_length=20, label='')
    wife_net_income_after_zakat = forms.CharField(max_length=20, label='')

    husband_zakat = forms.CharField(max_length=20, label='')
    wife_zakat = forms.CharField(max_length=20, label='')

    # Yang tadinya formula sekarang juga dibuat sebagai form field:
    husband_total = forms.CharField(max_length=20, label='')
    wife_total = forms.CharField(max_length=20, label='')

    husband_loss_compensation = forms.CharField(max_length=20, label='')
    wife_loss_compensation = forms.CharField(max_length=20, label='')

    husband_total_net_income = forms.CharField(max_length=20, label='')
    wife_total_net_income = forms.CharField(max_length=20, label='')

    spouse_total_net_income = forms.CharField(max_length=20, label='Nilai')
    non_taxable_income = forms.CharField(max_length=20, label='')
    taxable_income = forms.CharField(max_length=20, label='')

    five_percen_income_tax_payable = forms.CharField(max_length=20, label='')
    fifteen_percen_income_tax_payable = forms.CharField(max_length=20, label='')
    twenty_five_percen_income_tax_payable = forms.CharField(max_length=20, label='')
    thirty_percen_income_tax_payable = forms.CharField(max_length=20, label='')

    total_of_income_tax_payable = forms.CharField(max_length=20, label='')
    income_tax_payable_borne_by_husband = forms.CharField(max_length=20, label='')
    income_tax_payable_borne_by_wife = forms.CharField(max_length=20, label='')

    husband_name = forms.CharField(max_length=255, label='Nama Suami')
    husband_npwp = forms.CharField(max_length=20, label='NPWP Suami')
    wife_name = forms.CharField(max_length=255, label='Nama Istri')
    wife_npwp = forms.CharField(max_length=20, label='NPWP Istri')

    def __init__(self, *args, **kwargs):
        super(Form01aPHMTCalculate, self).__init__(*args, **kwargs)
        self.helper = FormHelper()


class Forms01c(forms.Form):
    NON_TAXABLE_INCOME_CHOICES = [
        ('U39', 'TK/'),
        ('Z39', 'K/'),
        ('AE39', 'K/I/'),
    ]

    INCOME_TAX_OPTION_CHOICES = [
        ('H52', 'Pajak Penghasilan yang harus Dibayar Sendiri *'),
        ('H55', 'Pajak Penghasilan yang Lebih Dipotong'),
    ]

    nwp = forms.CharField(max_length=255, label='NWP')
    tax_year = forms.IntegerField(label='Tahun Pajak')
    npwp = forms.CharField(max_length=20, label='NPWP')

    gross_income = forms.CharField(
        max_length=20,
        label='Penghasilan Bruto dalam Negeri Sehubungan dengan '
              'Pekerjaan dan Penghasilan Netto dalam Negeri Lainnya'
    )

    deduction = forms.CharField(max_length=20, label='Pengurangan')

    non_taxable_income_option = forms.ChoiceField(
        choices=NON_TAXABLE_INCOME_CHOICES,
        widget=forms.RadioSelect
    )

    non_taxable_income = forms.CharField(max_length=20)
    taxable_income = forms.CharField(max_length=20)
    income_tax_payable = forms.CharField(max_length=20)
    withheld_income_tax = forms.CharField(max_length=20)

    income_tax_option = forms.ChoiceField(
        choices=INCOME_TAX_OPTION_CHOICES,
        widget=forms.RadioSelect
    )

    income_tax_option_field = forms.CharField(max_length=20)
    tax_base = forms.CharField(max_length=20)
    final_income_tax_payable = forms.CharField(max_length=20)
    income_exempt_from_tax = forms.CharField(max_length=20)
    yearEnd_total = forms.CharField(max_length=20)
    yearEnd_tax_liability = forms.CharField(max_length=20)
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    def __init__(self, *args, **kwargs):
        super(Forms01c, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Submit'))


class FormsSpt1111Header(forms.Form):
    pkp_name = forms.CharField(max_length=255, label='Nama PKP')
    pkp_address = forms.CharField(max_length=255, label='Alamat')
    phone_number = forms.CharField(max_length=20, label='Telepon')
    hp_number = forms.CharField(max_length=20, label='Hp')
    klu_code = forms.CharField(max_length=20, label='Klu')
    npwp = forms.CharField(max_length=20, label='NPWP')
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    expire_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    def __init__(self, *args, **kwargs):
        super(FormsSpt1111Header, self).__init__(*args, **kwargs)
        self.helper = FormHelper()


class FormsSpt1111(forms.Form):
    OVERPAID_PPN_OPTION_CHOICES = [
        ('J52', 'Butir II.D (Diisi dalam hal SPT Bukan Pembetulan'),
        ('Z52', 'Butir II.D'),
        ('AE52', 'Butir II.F (Diisi dalam hal SPT Pembetulan'),
    ]

    OVERPAYER_OF_PPN_OPTION_CHOICES = [
        ('P54', 'PKP Pasal 9 ayat (4b) PPN'),
        ('AE54', 'Selain PKP Pasal 9 ayat (4b) PPN'),
    ]

    REQUEST_FOR_EXCESS_PPN_OPTION_CHOICES = [
        ('P56', 'Dikompensasikan ke Masa Pajak berikutnya'),
        ('AE56', 'Dikompensasikan ke Masa Pajak ....'),
        ('P58', 'Dikembalikan (Restitusi)'),
    ]

    REFUND_FOR_PKP_OPTION_CHOICES = [
        ('Q61', 'Pasal 17C KUP'),
        ('Q63', 'Pasal 17D KUP'),
        ('Q65', 'Pasal 9 ayat (4C) PPN dilakukan dengan Pengembalian Pendahuluan'),
    ]

    FORM_OPTION_CHOICES = [
        ('T107', 'PKP'),
        ('T108', 'Kuasa'),
    ]

    SPT_REQUIREMENTS_OPTION_CHOICES = [
        ('H99', 'Formulir 1111 AB'),
        ('H101', 'Formulir 1111 A1'),
        ('O99', 'Formulir 1111 A2'),
        ('O101', 'Formulir 1111 B1'),
        ('V99', 'Formulir 1111 B2'),
        ('V101', 'Formulir 1111 B3'),
        ('AB99', 'SSP PPN... Lembar'),
        ('AB101', 'SSP PPN... Lembar'),
        ('AI99', 'Surat Kuasa Khusus'),
        ('AI101', '..... , ..... Lembar'),
    ]

    dpp_export_value = forms.CharField(max_length=20, label='Ekspor DPP')
    dpp_self_assessed_value = forms.CharField(max_length=20, label='Penyerahan yang DPP-nya harus dipungut sendiri')
    dpp_collected_by_collector_value = forms.CharField(max_length=20,
                                                       label='Penyerahan yang DPP-nya dipungut oleh pemungut DPP')
    dpp_not_collected_value = forms.CharField(max_length=20, label='Penyerahan yang DPP-nya tidak dipungut')
    dpp_exempt_from_ppn_value = forms.CharField(max_length=20, label='Penyerahan yang dibebaskan dari pengenaan DPP')
    dpp_total = forms.CharField(label='Total DPP', widget=forms.TextInput(attrs={'readonly': 'readonly'}),
                                required=False)

    ppn_export_value = forms.CharField(max_length=20, label='Ekspor PPN')
    ppn_self_assessed_value = forms.CharField(max_length=20, label='Penyerahan yang PPN-nya harus dipungut sendiri')
    ppn_collected_by_collector_value = forms.CharField(max_length=20,
                                                       label='Penyerahan yang PPN-nya dipungut oleh pemungut DPP')
    ppn_not_collected_value = forms.CharField(max_length=20, label='Penyerahan yang PPN-nya tidak dipungut')
    exempt_from_ppn_value = forms.CharField(max_length=20, label='Penyerahan yang dibebaskan dari pengenaan PPN')
    ppn_total = forms.CharField(label='Total PPN', widget=forms.TextInput(attrs={'readonly': 'readonly'}),
                                required=False)

    no_subject_to_ppn = forms.CharField(max_length=20, label='Tidak Terutang PPN')
    total_all_deliveries = forms.CharField(
        label='Jumlah Seluruh Penyerahan', widget=forms.TextInput(attrs={'readonly': 'readonly'}), required=False)

    output_tax_self_assesment = forms.CharField(
        label='Pajak Keluaran yang harus dipungut sendiri', widget=forms.TextInput(attrs={'readonly': 'readonly'}),
        required=False)

    prepaid_ppn = forms.CharField(max_length=20, label='PPN Disetor Dimuka Dalam Masa Pajak Yang Sama')
    input_tax = forms.CharField(max_length=20, label='Pajak Masukan yang dapat diperhitungkan')
    underpaid_or_overpaid_ppn = forms.CharField(
        label='PPN yang kurang atau (lebih) bayar', widget=forms.TextInput(attrs={'readonly': 'readonly'}),
        required=False)

    underpaid_or_overpaid_ppn_on_corrected_spt = forms.CharField(
        max_length=20, label='PPN yang kurang atau (lebih) bayar pada SPT yang dibetulkan')

    underpaid_or_overpaid_ppn_due_to_correction = forms.CharField(
        label='PPN yang kurang atau (lebih) bayar karena pembetulan',
        widget=forms.TextInput(attrs={'readonly': 'readonly'}), required=False)

    settlement_of_underpaid_ppn = forms.DateField(
        label='Tanggal pembayaran PPN yang kurang', widget=forms.DateInput(attrs={'type': 'date'}))
    ntpp_code_1 = forms.CharField(max_length=20, label='NTPP')

    overpaid_ppn_option = forms.ChoiceField(
        choices=OVERPAID_PPN_OPTION_CHOICES,
        widget=forms.RadioSelect
    )

    overpayer_of_ppn_option = forms.ChoiceField(
        choices=OVERPAYER_OF_PPN_OPTION_CHOICES,
        widget=forms.RadioSelect
    )

    request_for_excess_ppn_option = forms.ChoiceField(
        choices=REQUEST_FOR_EXCESS_PPN_OPTION_CHOICES,
        widget=forms.RadioSelect
    )

    refund_for_pkp_option = forms.ChoiceField(
        choices=REFUND_FOR_PKP_OPTION_CHOICES,
        widget=forms.RadioSelect
    )

    tax_base = forms.CharField(max_length=20, label='Jumlah Dasar Pengenaan Pajak')
    ppn_payable_1 = forms.CharField(label='PPN Terutang', widget=forms.TextInput(attrs={'readonly': 'readonly'}),
                                    required=False)
    settlement_of_ppn_payable_1 = forms.DateField(
        label='Tanggal Pelunasan', widget=forms.DateInput(attrs={'type': 'date'}))

    ntpp_code_2 = forms.CharField(max_length=20, label='NTPP')

    ppn_payable_2 = forms.CharField(max_length=20, label='PPN yang wajib dibayar kembali')
    settlement_of_ppn_payable_2 = forms.DateField(
        label='Tanggal Pelunasan', widget=forms.DateInput(attrs={'type': 'date'}))

    ntpp_code_3 = forms.CharField(max_length=20, label='NTPP')

    ppn_on_luxury_goods_self_assessed = forms.CharField(max_length=20, label='PPn BM yang harus dipungut sendiri')
    prepaid_ppn_on_luxury_goods = forms.CharField(
        max_length=20, label='PPn BM yang Disetor Dimuka Dalam Masa Pajak Yang Sama')

    underpaid_or_overpaid_ppn_on_luxury_goods = forms.CharField(
        label='PPn BM yang kurang atau (lebih) bayar', widget=forms.TextInput(attrs={'readonly': 'readonly'}),
        required=False)

    underpaid_or_overpaid_ppn_on_luxury_goods_on_corrected_spt = forms.CharField(
        max_length=20, label='PPn BM yang kurang atau (lebih) bayar pada SPT yang dibetulkan')

    underpaid_or_overpaid_ppn_on_luxury_goods_due_to_correction = forms.CharField(
        label='PPn BM yang kurang atau (lebih) bayar karena pembetulan',
        widget=forms.TextInput(attrs={'readonly': 'readonly'}), required=False)

    settlement_of_ppn_on_luxury_goods = forms.DateField(
        label='Tanggal Pelunasan', widget=forms.DateInput(attrs={'type': 'date'}))

    ntpp_code_4 = forms.CharField(max_length=20, label='NTPP')

    spt_requirements_option = forms.MultipleChoiceField(
        choices=SPT_REQUIREMENTS_OPTION_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label='Kelengkapan SPT'
    )

    name = forms.CharField(max_length=255, label='Nama Jelas')
    position = forms.CharField(max_length=255, label='Posisi')

    form_option = forms.ChoiceField(
        choices=FORM_OPTION_CHOICES,
        widget=forms.RadioSelect
    )

    def __init__(self, *args, **kwargs):
        super(FormsSpt1111, self).__init__(*args, **kwargs)
        self.helper = FormHelper()


class FormsSpt1111Ab(forms.Form):
    dpp_of_export_of_bkp_or_jkp = forms.CharField(
        max_length=20, label='DPP dari Ekspor BKP Berwujud/BKP Tidak Berwujud/JKP')

    dpp_of_with_tax_invoices_not_stated = forms.CharField(
        max_length=20, label='DPP dari Penyerahan Dalam Negeri dengan Faktur Pajak yang Tidak Digunggung')

    dpp_of_with_tax_invoices_stated = forms.CharField(
        max_length=20, label='DPP dari Penyerahan Dalam Negeri dengan Faktur Pajak yang Digunggung')

    ppn_of_with_tax_invoices_not_stated = forms.CharField(
        max_length=20, label='PPN dari Penyerahan Dalam Negeri dengan Faktur Pajak yang Tidak Digunggung')

    ppn_of_with_tax_invoices_stated = forms.CharField(
        max_length=20, label='PPN dari Penyerahan Dalam Negeri dengan Faktur Pajak yang Digunggung')

    ppnbm_of_with_tax_invoices_not_stated = forms.CharField(
        max_length=20, label='PpnBM dari Penyerahan Dalam Negeri dengan Faktur Pajak yang Tidak Digunggung')

    ppnbm_of_with_tax_invoices_stated = forms.CharField(
        max_length=20, label='PpnBM dari Penyerahan Dalam Negeri dengan Faktur Pajak yang Digunggung')

    dpp_of_self_assessed = forms.CharField(
        max_length=20, label='DPP dari Penyerahan yang PPN atau PPN dan PPn BM-nya harus dipungut sendiri')

    dpp_of_collected_by_ppn_collector = forms.CharField(
        max_length=20, label='DPP dari Penyerahan yang PPN atau PPN dan PPn BM-nya dipungut oleh Pemungut PPN')

    dpp_of_not_collected = forms.CharField(
        max_length=20, label='DPP dari Penyerahan yang PPN atau PPN dan PPn BM-nya tidak dipungut')

    dpp_of_exempt_from_ppn = forms.CharField(
        max_length=20, label='DPP dari Penyerahan yang dibebaskan dari pengenaan PPN atau PPN dan PPn BM')

    ppn_of_self_assessed = forms.CharField(
        max_length=20, label='PPN dari Penyerahan yang PPN atau PPN dan PPn BM-nya harus dipungut sendiri')

    ppn_of_collected_by_ppn_collector = forms.CharField(
        max_length=20, label='PPN dari Penyerahan yang PPN atau PPN dan PPn BM-nya dipungut oleh Pemungut PPN')

    ppn_of_not_collected = forms.CharField(
        max_length=20, label='PPN dari Penyerahan yang PPN atau PPN dan PPn BM-nya tidak dipungut')

    ppn_of_exempt_from_ppn = forms.CharField(
        max_length=20, label='PPN dari Penyerahan yang dibebaskan dari pengenaan PPN atau PPN dan PPn BM')

    ppnbm_of_self_assessed = forms.CharField(
        max_length=20, label='PpnBM dari Penyerahan yang PPN atau PPN dan PPn BM-nya harus dipungut sendiri')

    ppnbm_of_collected_by_ppn_collector = forms.CharField(
        max_length=20, label='PpnBm dari Penyerahan yang PPN atau PPN dan PPn BM-nya dipungut oleh Pemungut PPN')

    ppnbm_of_not_collected = forms.CharField(
        max_length=20, label='PpnBM dari Penyerahan yang PPN atau PPN dan PPn BM-nya tidak dipungut')

    ppnbm_of_exempt_from_ppn = forms.CharField(
        max_length=20, label='PpnBm dari Penyerahan yang dibebaskan dari pengenaan PPN atau PPN dan PPn BM')

    dpp_of_bkp_import = forms.CharField(max_length=20, label='DPP dari Impor BKP')
    dpp_of_acquisition_of_bkp_or_jkp = forms.CharField(
        max_length=20, label='DPP dari Perolehan BKP/JKP dari Dalam Negeri Yang PM-nya Dapat Dikreditkan')

    dpp_of_acquisition_import = forms.CharField(
        max_length=20, label='DPP dari Impor atau Perolehan Yang PM-nya Tidak Dapat dikreditkan dan'
                             '/atau Impor atau Perolehan Yang Mendapat Fasilitas')

    total_of_dpp = forms.CharField(
        label='Total DPP', widget=forms.TextInput(attrs={'readonly': 'readonly'}), required=False)

    ppn_of_bkp_import = forms.CharField(max_length=20, label='PPN dari Impor BKP')
    ppn_of_acquisition_of_bkp_or_jkp = forms.CharField(
        max_length=20, label='PPN dari Perolehan BKP/JKP dari Dalam Negeri Yang PM-nya Dapat Dikreditkan')

    ppn_of_acquisition_import = forms.CharField(
        max_length=20, label='PPN dari Impor atau Perolehan Yang PM-nya Tidak Dapat dikreditkan dan'
                             '/atau Impor atau Perolehan Yang Mendapat Fasilitas')

    total_of_ppn = forms.CharField(
        label='Total PPN', widget=forms.TextInput(attrs={'readonly': 'readonly'}), required=False)

    ppnbm_of_bkp_import = forms.CharField(max_length=20, label='PPnBM dari Impor BKP')
    ppnbm_of_acquisition_of_bkp_or_jkp = forms.CharField(
        max_length=20, label='PPnBM dari Perolehan BKP/JKP dari Dalam Negeri Yang PM-nya Dapat Dikreditkan')

    ppnbm_of_acquisition_import = forms.CharField(
        max_length=20, label='PPnBM dari Impor atau Perolehan Yang PM-nya Tidak Dapat dikreditkan dan'
                             '/atau Impor atau Perolehan Yang Mendapat Fasilitas')

    total_of_ppnbm = forms.CharField(
        label='Total PPnBM', widget=forms.TextInput(attrs={'readonly': 'readonly'}), required=False)

    ppn_of_input_tax = forms.CharField(
        label='Pajak Masukan atas Perolehan yang Dapat Dikreditkan',
        widget=forms.TextInput(attrs={'readonly': 'readonly'}), required=False)

    ppn_of_compensation_of_excess_ppn = forms.CharField(
        max_length=20, label='Kompensasi kelebihan PPN Masa Pajak sebelumnya')

    ppn_of_compensation_due_to_correction = forms.CharField(
        max_length=20, label='Kompensasi kelebihan PPN karena pembetulan SPT PPN Masa Pajak')

    ppn_of_recalculated_result = forms.CharField(
        max_length=20, label='Hasil Penghitungan Kembali Pajak Masukan yang telah dikreditkan '
                             'sebagai penambah (pengurang) Pajak Masukan')

    ppn_of_total_calculation = forms.CharField(
        label='Total', widget=forms.TextInput(attrs={'readonly': 'readonly'}), required=False)

    total_of_input_tax = forms.CharField(
        label='Jumlah Pajak Masukan yang Dapat Diperhitungkan',
        widget=forms.TextInput(attrs={'readonly': 'readonly'}), required=False)

    def __init__(self, *args, **kwargs):
        super(FormsSpt1111Ab, self).__init__(*args, **kwargs)
        self.helper = FormHelper()


class FormsSpt1111A1(forms.Form):
    bkp_buyer_name = forms.CharField(
        max_length=255, label='Nama Pembeli BKP /Penerima Manfaat BKP Tidak Berwujud/Penerima JKP')

    document_number = forms.IntegerField(label='Nomor Dokumen')
    document_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label='Tanggal Dokumen')
    dpp_value = forms.CharField(max_length=20, label='DPP')
    description = forms.CharField(max_length=255, label='Keterangan')

    def __init__(self, *args, **kwargs):
        super(FormsSpt1111A1, self).__init__(*args, **kwargs)
        self.helper = FormHelper()


class FormsSpt1111A2(forms.Form):
    bkp_buyer_name = forms.CharField(
        max_length=255, label='Nama Pembeli BKP /Penerima Manfaat BKP Tidak Berwujud/Penerima JKP')

    npwp_number = forms.CharField(label='NPWP', max_length=20)
    tax_invoice_serial_number = forms.CharField(max_length=20, label='Nomor Seri Faktur Pajak')
    tax_invoice_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label='Tanggal Faktur Pajak')
    dpp_value = forms.CharField(max_length=20, label='DPP')
    ppn_value = forms.CharField(max_length=20, label='PPN')
    ppnbm_value = forms.CharField(max_length=20, label='PpnBM')
    changed_tax_invoice_serial_number = forms.CharField(
        max_length=20, label='Kode dan No.Seri Faktur Pajak Yang Diganti Diretur')

    def __init__(self, *args, **kwargs):
        super(FormsSpt1111A2, self).__init__(*args, **kwargs)
        self.helper = FormHelper()


class FormsSpt1111B1(forms.Form):
    bkp_saler_name = forms.CharField(
        max_length=255, label='Nama Penjual BKP/BKP Tidak Berwujud/Pemberi JKP')

    document_number = forms.IntegerField(label='Nomor Dokumen')
    document_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label='Tanggal Dokumen')
    dpp_value = forms.CharField(max_length=20, label='DPP')
    ppn_value = forms.CharField(max_length=20, label='PPN')
    ppnbm_value = forms.CharField(max_length=20, label='PpnBM')
    description = forms.CharField(max_length=255, label='Deskripsi')

    def __init__(self, *args, **kwargs):
        super(FormsSpt1111B1, self).__init__(*args, **kwargs)
        self.helper = FormHelper()


class FormsSpt1111B2(forms.Form):
    bkp_saler_name = forms.CharField(
        max_length=255, label='Nama Penjual BKP/Penerima Manfaat BKP Tidak Berwujud/Penerima JKP')
    npwp_number = forms.CharField(label='NPWP', max_length=20)
    tax_invoice_serial_number = forms.CharField(max_length=20, label='Nomor Seri Faktur Pajak')
    tax_invoice_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label='Tanggal Faktur Pajak')
    dpp_value = forms.CharField(max_length=20, label='DPP')
    ppn_value = forms.CharField(max_length=20, label='PPN')
    ppnbm_value = forms.CharField(max_length=20, label='PpnBM')
    changed_tax_invoice_serial_number = forms.CharField(
        max_length=20, label='Kode dan No.Seri Faktur Pajak Yang Diganti Diretur')

    def __init__(self, *args, **kwargs):
        super(FormsSpt1111B2, self).__init__(*args, **kwargs)
        self.helper = FormHelper()


class FormsSpt1111B3(forms.Form):
    bkp_saler_name = forms.CharField(
        max_length=255, label='Nama Penjual BKP/Penerima Manfaat BKP Tidak Berwujud/Penerima JKP')
    npwp_number = forms.CharField(label='NPWP', max_length=20)
    tax_invoice_serial_number = forms.CharField(max_length=20, label='Nomor Seri Faktur Pajak')
    tax_invoice_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label='Tanggal Faktur Pajak')
    dpp_value = forms.CharField(max_length=20, label='DPP')
    ppn_value = forms.CharField(max_length=20, label='PPN')
    ppnbm_value = forms.CharField(max_length=20, label='PpnBM')
    changed_tax_invoice_serial_number = forms.CharField(
        max_length=20, label='Kode dan No.Seri Faktur Pajak Yang Diganti Diretur')

    def __init__(self, *args, **kwargs):
        super(FormsSpt1111B3, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
