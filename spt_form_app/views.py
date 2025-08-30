import io
import os

from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from openpyxl import load_workbook

from . import settings
from .forms import Forms01c
from .forms import (
    FormsSpt1111Header, FormsSpt1111, FormsSpt1111Ab, Forms01a, Form01a1770III, Form01a1770IHal2,
    Form01a1770IHal1, Form1770, Form01aPHMTCalculate
)
from .models import (
    Form01c, FormSptPPN1111Header, FormSptPPN1111, FormSptPPN1111AB, FormSptPPN1111A1
, FormSptPPN1111A2, FormSptPPN1111B1, FormSptPPN1111B2, FormSptPPN1111B3, Form01aIdentity,
    Form01aSheet1770IVA, Form01aSheet1770IVB, Form01aSheet1770IVC, Form01aSheetOpptPayment,
    Form01aSheetPp462013Payment, Form01aSheet1770III
)


def home(request):
    return render(request, 'main/main.html', {})


def form_01a(request):
    if request.method == 'POST':
        identity_form = Forms01a(request.POST)
        form1770III = Form01a1770III(request.POST)
        form1770Ihal2 = Form01a1770IHal2(request.POST)
        form1770Ihal1 = Form01a1770IHal1(request.POST)
        form1770 = Form1770(request.POST)
        form01aPhMtCalculate = Form01aPHMTCalculate(request.POST)


        if identity_form.is_valid():
            clean = identity_form.cleaned_data
            header_instance = Form01aIdentity.objects.create(
                npwp = clean['npwp'],
                nwp = clean['nwp'],
                address = clean['address'],
                tax_year= clean['tax_year'],
                start_date= clean['start_date'],
                end_date = clean['end_date'],
                spt_option = clean['spt_option'],
                business_type = clean['business_type'],
                klu_code = clean['klu_code'],
                phone = clean['phone'],
                facsimile = clean['facsimile'],
                tax_status = clean['tax_status'],
                spouse_npwp = clean['spouse_npwp'],
            )

            #IV-A
            asset_codes = request.POST.getlist('asset_code[]')
            asset_names = request.POST.getlist('asset_name[]')
            year_of_acquisitions = request.POST.getlist('year_of_acquisition[]')
            descriptions = request.POST.getlist('description[]')

            for a_code, a_name, ac_year, iva_desc in zip ( asset_codes, asset_names, year_of_acquisitions, descriptions):
                Form01aSheet1770IVA.objects.create(
                    id_form01aIdentity = header_instance,
                    asset_code = a_code,
                    asset_name = a_name,
                    year_of_acquisition = ac_year,
                    description = iva_desc
                )

            #IV-B
            debt_codes = request.POST.getlist('debt_code[]')
            lender_names = request.POST.getlist('lender_name[]')
            lender_address = request.POST.getlist('lender_address[]')
            loan_years = request.POST.getlist('loan_year[]')
            amounts = request.POST.getlist('amount[]')

            for d_code, l_name, l_address, lo_years, d_amount in zip(debt_codes,lender_names,lender_address,loan_years, amounts):
                Form01aSheet1770IVB.objects.create(
                    id_form01aIdentity=header_instance,
                    debt_code=d_code,
                    lender_name=l_name,
                    lender_address=l_address,
                    loan_year = lo_years,
                    amount = d_amount
                )

            #IV-C
            family_member_names = request.POST.getlist('family_member_name[]')
            id_numbers = request.POST.getlist('id_number[]')
            family_relationships  = request.POST.getlist('family_relationship[]')
            occupations = request.POST.getlist('occupation[]')

            for fm_name, id_num, f_relation, fm_occupation in zip(family_member_names,id_numbers, family_relationships, occupations):
                Form01aSheet1770IVC.objects.create(
                    id_form01aIdentity=header_instance,
                    family_member_name= fm_name,
                    id_number = id_num,
                    family_relationship = f_relation,
                    occupation = fm_occupation
                )

            #OPPT
            oppt_business_place_npwps = request.POST.getlist('oppt_business_place_npwp[]')
            oppt_address = request.POST.getlist('oppt_address[]')
            retail_gross_incomes = request.POST.getlist('retail_gross_income[]')
            income_tax_25_paids = request.POST.getlist('income_tax_25_paid[]')

            for oppt_bp_npwp, o_address, re_gross_income, income_25 in zip(oppt_business_place_npwps,oppt_address, retail_gross_incomes, income_tax_25_paids):
                Form01aSheetOpptPayment.objects.create(
                    id_form01aIdentity=header_instance,
                    oppt_business_place_npwp= oppt_bp_npwp,
                    oppt_address  = o_address,
                    retail_gross_income = re_gross_income,
                    income_tax_25_paid = income_25
                )

            #PP46
            pp46_business_place_npwps = request.POST.getlist('pp46_business_place_npwp[]')
            pp46_address = request.POST.getlist('pp46_address[]')
            gross_turnovers = request.POST.getlist('gross_turnover[]')
            pph_final_1_paids = request.POST.getlist('pph_final_1_paid[]')

            for pp46_bp_npwp, p_address, g_turnover, pph_paid in zip(pp46_business_place_npwps,  pp46_address, gross_turnovers, pph_final_1_paids):
                Form01aSheetPp462013Payment.objects.create(
                    id_form01aIdentity=header_instance,
                    pp46_business_place_npwp  = pp46_bp_npwp,
                    pp46_address = p_address,
                    gross_turnover = g_turnover,
                    pph_final_1_paid = pph_paid
                )

            messages.success(request, "Form Success")
            return redirect('form_01a_manage')
        else:
            messages.error(request, "Error detected")
    else:
        identity_form= Forms01a()
        form1770III = Form01a1770III()
        form1770Ihal2 = Form01a1770IHal2()
        form1770Ihal1 = Form01a1770IHal1()
        form1770  = Form1770()
        form01aPhMtCalculate = Form01aPHMTCalculate()

    return render(request, 'form/form_01a.html', {
        'form': identity_form,
        'form1770III' : form1770III,
        'form1770Ihal2' : form1770Ihal2,
        'form1770Ihal1' : form1770Ihal1,
        '1770' : form1770,
        'form01aPhMtCalculate' : form01aPhMtCalculate
    })


def form_01b(request):
    return render(request, 'form/form_01b.html', {})


def form_01c(request):
    if request.method == 'POST':
        form = Forms01c(request.POST)
        if form.is_valid():
            Form01c.objects.create(
                nwp=form.cleaned_data['nwp'],
                npwp=form.cleaned_data['npwp'],
                tax_year=form.cleaned_data['tax_year'],
                gross_income=form.cleaned_data['gross_income'],
                deduction=form.cleaned_data['deduction'],
                non_taxable_income_option=form.cleaned_data['non_taxable_income_option'],
                non_taxable_income=form.cleaned_data['non_taxable_income'],
                taxable_income=form.cleaned_data['taxable_income'],
                income_tax_payable=form.cleaned_data['income_tax_payable'],
                withheld_income_tax=form.cleaned_data['withheld_income_tax'],
                income_tax_option=form.cleaned_data['income_tax_option'],
                income_tax_option_field=form.cleaned_data['income_tax_option_field'],
                tax_base=form.cleaned_data['tax_base'],
                final_income_tax_payable=form.cleaned_data['final_income_tax_payable'],
                income_exempt_from_tax=form.cleaned_data['income_exempt_from_tax'],
                yearEnd_total=form.cleaned_data['yearEnd_total'],
                yearEnd_tax_liability=form.cleaned_data['yearEnd_tax_liability'],
                date=form.cleaned_data['date']
            )
            messages.success(request, "Form Berhasil Dibuat!")
            return redirect('form_01c_manage')
        else:
            messages.error(request, "Error Detected")
    else:
        form = Forms01c()
    return render(request, 'form/form_01c.html', {'form': form})


def form_spt_1111(request):
    if request.method == 'POST':
        header_form = FormsSpt1111Header(request.POST)
        spt1111_form = FormsSpt1111(request.POST)
        spt1111_ab_form = FormsSpt1111Ab(request.POST)

        if header_form.is_valid() and spt1111_form.is_valid() and spt1111_ab_form.is_valid():
            # Simpan data header
            cd = header_form.cleaned_data
            header_instance = FormSptPPN1111Header.objects.create(
                pkp_name=cd['pkp_name'],
                pkp_address=cd['pkp_address'],
                phone_number=cd['phone_number'],
                hp_number=cd['hp_number'],
                klu_code=cd['klu_code'],
                npwp=cd['npwp'],
                start_date=cd['start_date'],
                expire_date=cd['expire_date'],
            )

            # Simpan data utama SPT1111
            cd1111 = spt1111_form.cleaned_data
            spt1111_instance = FormSptPPN1111.objects.create(
                id_formSpt_ppn1111_header=header_instance,
                dpp_export_value=cd1111['dpp_export_value'],
                dpp_self_assessed_value=cd1111['dpp_self_assessed_value'],
                dpp_collected_by_collector_value=cd1111['dpp_collected_by_collector_value'],
                dpp_not_collected_value=cd1111['dpp_not_collected_value'],
                dpp_exempt_from_ppn_value=cd1111['dpp_exempt_from_ppn_value'],
                ppn_export_value=cd1111['ppn_export_value'],
                ppn_self_assessed_value=cd1111['ppn_self_assessed_value'],
                ppn_collected_by_collector_value=cd1111['ppn_collected_by_collector_value'],
                ppn_not_collected_value=cd1111['ppn_not_collected_value'],
                exempt_from_ppn_value=cd1111['exempt_from_ppn_value'],
                no_subject_to_ppn=cd1111['no_subject_to_ppn'],
                prepaid_ppn=cd1111['prepaid_ppn'],
                input_tax=cd1111['input_tax'],
                underpaid_or_overpaid_ppn_on_corrected_spt=cd1111['underpaid_or_overpaid_ppn_on_corrected_spt'],
                settlement_of_underpaid_ppn=cd1111['settlement_of_underpaid_ppn'],
                ntpp_code_1=cd1111['ntpp_code_1'],
                overpaid_ppn_option=cd1111['overpaid_ppn_option'],
                overpayer_of_ppn_option=cd1111['overpayer_of_ppn_option'],
                request_for_excess_ppn_option=cd1111['request_for_excess_ppn_option'],
                refund_for_pkp_option=cd1111['refund_for_pkp_option'],
                tax_base=cd1111['tax_base'],
                settlement_of_ppn_payable_1=cd1111['settlement_of_ppn_payable_1'],
                ntpp_code_2=cd1111['ntpp_code_2'],
                ppn_payable_2=cd1111['ppn_payable_2'],
                settlement_of_ppn_payable_2=cd1111['settlement_of_ppn_payable_2'],
                ntpp_code_3=cd1111['ntpp_code_3'],
                ppn_on_luxury_goods_self_assessed=cd1111['ppn_on_luxury_goods_self_assessed'],
                prepaid_ppn_on_luxury_goods=cd1111['prepaid_ppn_on_luxury_goods'],
                underpaid_or_overpaid_ppn_on_luxury_goods_on_corrected_spt=cd1111[
                    'underpaid_or_overpaid_ppn_on_luxury_goods_on_corrected_spt'],
                settlement_of_ppn_on_luxury_goods=cd1111['settlement_of_ppn_on_luxury_goods'],
                ntpp_code_4=cd1111['ntpp_code_4'],
                spt_requirements_option=cd1111['spt_requirements_option'],
                name=cd1111['name'],
                position=cd1111['position'],
                form_option=cd1111['form_option'],
            )

            # Simpan data AB
            cdAb = spt1111_ab_form.cleaned_data
            FormSptPPN1111AB.objects.create(
                id_formSpt_ppn1111_header=header_instance,
                dpp_of_with_tax_invoices_stated=cdAb['dpp_of_with_tax_invoices_stated'],
                ppn_of_with_tax_invoices_not_stated=cdAb['ppn_of_with_tax_invoices_not_stated'],
                ppn_of_with_tax_invoices_stated=cdAb['ppn_of_with_tax_invoices_stated'],
                ppnbm_of_with_tax_invoices_not_stated=cdAb['ppnbm_of_with_tax_invoices_not_stated'],
                ppnbm_of_with_tax_invoices_stated=cdAb['ppnbm_of_with_tax_invoices_stated'],
                dpp_of_self_assessed=cdAb['dpp_of_self_assessed'],
                dpp_of_collected_by_ppn_collector=cdAb['dpp_of_collected_by_ppn_collector'],
                dpp_of_not_collected=cdAb['dpp_of_not_collected'],
                dpp_of_exempt_from_ppn=cdAb['dpp_of_exempt_from_ppn'],
                ppn_of_self_assessed=cdAb['ppn_of_self_assessed'],
                ppn_of_collected_by_ppn_collector=cdAb['ppn_of_collected_by_ppn_collector'],
                ppn_of_not_collected=cdAb['ppn_of_not_collected'],
                ppn_of_exempt_from_ppn=cdAb['ppn_of_exempt_from_ppn'],
                ppnbm_of_self_assessed=cdAb['ppnbm_of_self_assessed'],
                ppnbm_of_collected_by_ppn_collector=cdAb['ppnbm_of_collected_by_ppn_collector'],
                ppnbm_of_not_collected=cdAb['ppnbm_of_not_collected'],
                ppnbm_of_exempt_from_ppn=cdAb['ppnbm_of_exempt_from_ppn'],
                dpp_of_bkp_import=cdAb['dpp_of_bkp_import'],
                dpp_of_acquisition_of_bkp_or_jkp=cdAb['dpp_of_acquisition_of_bkp_or_jkp'],
                dpp_of_acquisition_import=cdAb['dpp_of_acquisition_import'],
                ppn_of_bkp_import=cdAb['ppn_of_bkp_import'],
                ppn_of_acquisition_of_bkp_or_jkp=cdAb['ppn_of_acquisition_of_bkp_or_jkp'],
                ppn_of_acquisition_import=cdAb['ppn_of_acquisition_import'],
                ppnbm_of_bkp_import=cdAb['ppnbm_of_bkp_import'],
                ppnbm_of_acquisition_of_bkp_or_jkp=cdAb['ppnbm_of_acquisition_of_bkp_or_jkp'],
                ppnbm_of_acquisition_import=cdAb['ppnbm_of_acquisition_import'],
                ppn_of_compensation_of_excess_ppn=cdAb['ppn_of_compensation_of_excess_ppn'],
                ppn_of_compensation_due_to_correction=cdAb['ppn_of_compensation_due_to_correction'],
                ppn_of_recalculated_result=cdAb['ppn_of_recalculated_result'],
            )

            # Function to handle all dynamic tables (looped input)
            def parse_table(prefix, model, extra_fields=None, main_fields=None, fields_map=None):
                data_list = []
                index = 0

                if fields_map is None:
                    fields_map = {
                        'npwp_number': f'{prefix}-npwp_number[]',
                        'tax_invoice_serial_number': f'{prefix}-tax_invoice_serial_number[]',
                        'tax_invoice_date': f'{prefix}-tax_invoice_date[]',
                        'dpp_value': f'{prefix}-dpp_value[]',
                        'ppn_value': f'{prefix}-ppn_value[]',
                        'ppnbm_value': f'{prefix}-ppnbm_value[]',
                        'changed_tax_invoice_serial_number': f'{prefix}-changed_tax_invoice_serial_number[]',
                    }

                bkp_name_list = request.POST.getlist(f'{prefix}-{main_fields}')
                while index < len(bkp_name_list):
                    bkp_name = bkp_name_list[index]
                    if not bkp_name:
                        index += 1
                        continue

                    instance = model(id_formSpt_ppn1111_header=header_instance)

                    if main_fields == 'bkp_buyer_name[]':
                        instance.bkp_buyer_name = bkp_name
                    else:
                        instance.bkp_saler_name = bkp_name

                    for field, post_key in fields_map.items():
                        values = request.POST.getlist(post_key)
                        if index < len(values):
                            setattr(instance, field, values[index])

                    if extra_fields:
                        for field, post_key in extra_fields.items():
                            values = request.POST.getlist(post_key)
                            if index < len(values):
                                setattr(instance, field, values[index])

                    instance.save()
                    index += 1

            # Simpan seluruh subform dinamis
            parse_table('spt1111_b3', FormSptPPN1111B3)
            parse_table('spt1111_b2', FormSptPPN1111B2)
            parse_table('spt1111_a2', FormSptPPN1111A2, main_fields='bkp_buyer_name[]')
            parse_table(
                'spt1111_b1', FormSptPPN1111B1,
                extra_fields={
                    'document_number': 'spt1111_b1-document_number[]',
                    'document_date': 'spt1111_b1-document_date[]',
                    'description': 'spt1111_b1-description[]',
                },
                main_fields='bkp_saler_name[]',
                fields_map={
                    'dpp_value': 'spt1111_b1-dpp_value[]',
                    'ppn_value': 'spt1111_b1-ppn_value[]',
                    'ppnbm_value': 'spt1111_b1-ppnbm_value[]',
                }
            )
            parse_table(
                'spt1111_a1', FormSptPPN1111A1,
                extra_fields={
                    'document_number': 'spt1111_a1-document_number[]',
                    'document_date': 'spt1111_a1-document_date[]',
                    'description': 'spt1111_a1-description[]',
                },
                main_fields='bkp_buyer_name[]',
                fields_map={
                    'dpp_value': 'spt1111_a1-dpp_value[]',
                }
            )

            return redirect('form_spt_1111_manage')
        else:
            print("Form Error", header_form.errors, spt1111_form.errors, spt1111_ab_form.errors)

    else:
        header_form = FormsSpt1111Header()
        spt1111_form = FormsSpt1111()
        spt1111_ab_form = FormsSpt1111Ab()

    context = {
        'forms': {
            'header': header_form,
            'spt1111': spt1111_form,
            'spt1111_ab': spt1111_ab_form,
        }
    }

    return render(request, 'form/form_spt_1111.html', context)


# Form Manage
def form_01a_manage(request):
    return render(request, 'form_manage/form_01a_manage.html', {})


def form_01b_manage(request):
    return render(request, 'form_manage/form_01b_manage.html', {})


def form_01c_manage(request):
    o1c_form_data = Form01c.objects.all()
    return render(request, 'form_manage/form_01c_manage.html', {'data_list': o1c_form_data})


def form_spt_1111_manage(request):
    return render(request, 'form_manage/form_spt_1111_manage.html', {})


# Form Edit
def edit_form_01c(request, form_id):
    instance = get_object_or_404(Form01c, id=form_id)

    if request.method == 'POST':
        form = Forms01c(request.POST)
        if form.is_valid():
            # Manual assign setiap field
            instance.nwp = form.cleaned_data['nwp']
            instance.npwp = form.cleaned_data['npwp']
            instance.tax_year = form.cleaned_data['tax_year']
            instance.gross_income = form.cleaned_data['gross_income']
            instance.deduction = form.cleaned_data['deduction']
            instance.non_taxable_income_option = form.cleaned_data['non_taxable_income_option']
            instance.non_taxable_income = form.cleaned_data['non_taxable_income']
            instance.taxable_income = form.cleaned_data['taxable_income']
            instance.income_tax_payable = form.cleaned_data['income_tax_payable']
            instance.withheld_income_tax = form.cleaned_data['withheld_income_tax']
            instance.income_tax_option = form.cleaned_data['income_tax_option']
            instance.income_tax_option_field = form.cleaned_data['income_tax_option_field']
            instance.tax_base = form.cleaned_data['tax_base']
            instance.final_income_tax_payable = form.cleaned_data['final_income_tax_payable']
            instance.income_exempt_from_tax = form.cleaned_data['income_exempt_from_tax']
            instance.yearEnd_total = form.cleaned_data['yearEnd_total']
            instance.yearEnd_tax_liability = form.cleaned_data['yearEnd_tax_liability']
            instance.date = form.cleaned_data['date']

            instance.save()
            messages.success(request, "Form berhasil diperbarui!")
            return redirect('form_01c_manage')
        else:
            messages.error(request, "Gagal menyimpan perubahan. Periksa kembali data yang dimasukkan.")
    else:
        # Set data awal ke form
        form = Forms01c(initial={
            'nwp': instance.nwp,
            'npwp': instance.npwp,
            'tax_year': instance.tax_year,
            'gross_income': instance.gross_income,
            'deduction': instance.deduction,
            'non_taxable_income_option': instance.non_taxable_income_option,
            'non_taxable_income': instance.non_taxable_income,
            'taxable_income': instance.taxable_income,
            'income_tax_payable': instance.income_tax_payable,
            'withheld_income_tax': instance.withheld_income_tax,
            'income_tax_option': instance.income_tax_option,
            'income_tax_option_field': instance.income_tax_option_field,
            'tax_base': instance.tax_base,
            'final_income_tax_payable': instance.final_income_tax_payable,
            'income_exempt_from_tax': instance.income_exempt_from_tax,
            'yearEnd_total': instance.yearEnd_total,
            'yearEnd_tax_liability': instance.yearEnd_tax_liability,
            'date': instance.date,
        })

    return render(request, 'form_edit/form_01c_edit.html', {'form': form})


# Form Delete
def delete_form_01c(request, form_id):
    form = get_object_or_404(Form01c, id=form_id)
    form.delete()
    messages.success(request, "Form berhasil dihapus!")
    return redirect('form_01c_manage')


# Form Export
def export_form_01c(request, form_id):
    instance = Form01c.objects.get(id=form_id)

    template_path = os.path.join(settings.BASE_DIR, 'spt_form_app', 'static', 'template_excel',
                                 '01C_SPT OP_Formulir SPT 1770 SS.xlsx')

    wb = load_workbook(template_path)
    sheet = wb.active

    data_source = {
        'nwp': instance.nwp,
        'npwp': instance.npwp,
        'tax_year': instance.tax_year,
        'date': instance.date,

        'gross_income': instance.gross_income,
        'deduction': instance.deduction,
        'non_taxable_income_option': instance.non_taxable_income_option,
        'non_taxable_income': instance.non_taxable_income,
        'taxable_income': instance.taxable_income,
        'income_tax_payable': instance.income_tax_payable,
        'withheld_income_tax': instance.withheld_income_tax,
        'income_tax_option': instance.income_tax_option,
        'income_tax_option_field': instance.income_tax_option_field,

        'tax_base': instance.tax_base,
        'final_income_tax_payable': instance.final_income_tax_payable,
        'income_exempt_from_tax': instance.income_exempt_from_tax,

        'yearEnd_total': instance.yearEnd_total,
        'yearEnd_tax_liability': instance.yearEnd_tax_liability,

    }

    tax_year = str(data_source['tax_year'])
    npwp = str(data_source['npwp'])
    nwp = str(data_source['nwp'])
    gross_income = int(data_source['gross_income'])
    deduction = int(data_source['deduction'])
    non_taxable_income = int(data_source['non_taxable_income'])
    taxable_income = int(data_source['taxable_income'])
    income_tax_payable = int(data_source['income_tax_payable'])
    withheld_income_tax = int(data_source['withheld_income_tax'])
    income_tax_option_field = data_source['income_tax_option_field']
    tax_base = int(data_source['tax_base'])
    final_income_tax_payable = int(data_source['final_income_tax_payable'])
    income_exempt_from_tax = int(data_source['income_exempt_from_tax'])
    year_end_total = int(data_source['yearEnd_total'])
    year_end_tax_liability = int(data_source['yearEnd_tax_liability'])
    date_object = data_source['date']
    day = date_object.strftime("%d")
    month = date_object.strftime("%m")
    year = date_object.strftime("%Y")

    sheet['AK5'] = tax_year[0]
    sheet['AL5'] = tax_year[1]
    sheet['AM5'] = tax_year[2]
    sheet['AN5'] = tax_year[3]
    sheet['N22'] = npwp[:9]
    sheet['AJ22'] = npwp[9:12]
    sheet['AN22'] = npwp[12:]
    sheet['N25'] = nwp
    sheet['AJ33'] = gross_income
    sheet['AJ36'] = deduction

    # Non-Taxable Income
    choose = data_source['non_taxable_income_option']
    value = 'X'

    if choose == 'U39':
        sheet['U39'] = value
        sheet['Z39'] = ''
        sheet['AE39'] = ''
    elif choose == 'Z39':
        sheet['U39'] = ''
        sheet['Z39'] = value
        sheet['AE39'] = ''
    elif choose == 'AE39':
        sheet['U39'] = ''
        sheet['Z39'] = ''
        sheet['AE39'] = value
    else:
        sheet['U39'] = ''
        sheet['Z39'] = ''
        sheet['AE39'] = ''

    sheet['AJ39'] = non_taxable_income
    sheet['AJ43'] = taxable_income
    sheet['AJ46'] = income_tax_payable
    sheet['AJ49'] = withheld_income_tax

    choose = data_source['income_tax_option']

    if choose == 'H52':
        sheet['H52'] = 'X'
        sheet['H55'] = ''
    elif choose == 'H55':
        sheet['H52'] = ''
        sheet['H55'] = 'X'
    else:
        sheet['H52'] = ''
        sheet['H55'] = ''

    sheet['AJ52'] = income_tax_option_field

    sheet['AJ61'] = tax_base
    sheet['AJ64'] = final_income_tax_payable
    sheet['AJ67'] = income_exempt_from_tax
    sheet['AJ73'] = year_end_total
    sheet['AJ76'] = year_end_tax_liability
    sheet['T88'] = day
    sheet['W88'] = month
    sheet['Z88'] = year

    output = io.BytesIO()
    wb.save(output)
    output.seek(0)

    filename = f"Form-01C_{instance.npwp}_{instance.tax_year}.xlsx"
    response = HttpResponse(
        output,
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = f'attachment; filename={filename}'
    return response
