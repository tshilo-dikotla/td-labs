from edc_lab import RequisitionPanel

from .aliquot_types import wb

from .processing_profiles import infant_glucose_processing
from .processing_profiles import infant_serum_processing, infant_pbmc_pl_processing
from .processing_profiles import dbs_processing, infant_insulin, dna_pcr

infant_glucose_panel = RequisitionPanel(
    name='infant_glucose',
    verbose_name='Infant Glucose',
    aliquot_type=wb,
    processing_profile=infant_glucose_processing)

infant_insulin = RequisitionPanel(
    name='infant_insulin',
    verbose_name='Infant Insulin',
    aliquot_type=wb,
    processing_profile=infant_insulin)

dna_pcr = RequisitionPanel(
    name='dna_pcr',
    verbose_name='DNA PCR',
    aliquot_type=wb,
    processing_profile=dna_pcr)

serum_panel = RequisitionPanel(
    name='serum_storage',
    verbose_name='Infant Serum (Store Only)',
    aliquot_type=wb,
    processing_profile=infant_serum_processing)

infant_pbmc_pl_panel = RequisitionPanel(
    name='infant_pbmc_pl_store',
    verbose_name='Infant PBMC PL',
    aliquot_type=wb,
    processing_profile=infant_pbmc_pl_processing)

dbs_panel = RequisitionPanel(
    name='DBS',
    verbose_name='DBS (Store Only)',
    aliquot_type=wb,
    processing_profile=dbs_processing)
