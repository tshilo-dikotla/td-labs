from edc_lab import RequisitionPanel

from .aliquot_types import wb

from .processing_profiles import viral_load_processing, pbmc_vl_processing
from .processing_profiles import glucose_processing, elisa_processing
from .processing_profiles import pbmc_plasma_processing
from .processing_profiles import cd4_processing, insulin

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
