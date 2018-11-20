from edc_lab import RequisitionPanel, LabProfile
from edc_lab.site_labs import site_labs

from .aliquot_types import wb
from .processing_profiles import cd4_processing, insulin
from .processing_profiles import glucose_processing, elisa_processing
from .processing_profiles import pbmc_plasma_processing
from .processing_profiles import viral_load_processing, pbmc_vl_processing

maternal_lab_profile = LabProfile(
    name='td_maternal_lab_profile',
    requisition_model='td_maternal.maternalrequisition')

cd4_panel = RequisitionPanel(
    name='cd4',
    verbose_name='CD4',
    aliquot_type=wb,
    processing_profile=cd4_processing)

viral_load_panel = RequisitionPanel(
    name='viral_load',
    verbose_name='Viral Load',
    aliquot_type=wb,
    processing_profile=viral_load_processing)

pbmc_vl_panel = RequisitionPanel(
    name='pbmc_vl',
    verbose_name='PBMC VL',
    aliquot_type=wb,
    processing_profile=pbmc_vl_processing)

fasting_glucose_panel = RequisitionPanel(
    name='fasting_glucose',
    verbose_name='Fasting Glucose',
    aliquot_type=wb,
    processing_profile=glucose_processing)

glucose_1h_panel = RequisitionPanel(
    name='glucose_1h',
    verbose_name='Glucose 1h',
    aliquot_type=wb,
    processing_profile=glucose_processing)

glucose_2h_panel = RequisitionPanel(
    name='glucose_2h',
    verbose_name='Glucose 2h',
    aliquot_type=wb,
    processing_profile=glucose_processing)

pbmc_pl_panel = RequisitionPanel(
    name='pbmc_pl_store',
    verbose_name='PBMC Plasma (STORE ONLY)',
    aliquot_type=wb,
    processing_profile=pbmc_plasma_processing)

elisa_panel = RequisitionPanel(
    name='elisa',
    verbose_name='ELISA',
    aliquot_type=wb,
    processing_profile=elisa_processing)

insulin_panel = RequisitionPanel(
    name='insulin',
    verbose_name='Insulin',
    aliquot_type=wb,
    processing_profile=insulin)

maternal_lab_profile.add_panel(cd4_panel)
maternal_lab_profile.add_panel(viral_load_panel)
maternal_lab_profile.add_panel(pbmc_vl_panel)
maternal_lab_profile.add_panel(fasting_glucose_panel)
maternal_lab_profile.add_panel(glucose_1h_panel)
maternal_lab_profile.add_panel(glucose_2h_panel)
maternal_lab_profile.add_panel(pbmc_pl_panel)
maternal_lab_profile.add_panel(elisa_panel)
maternal_lab_profile.add_panel(insulin_panel)

site_labs.register(maternal_lab_profile)
