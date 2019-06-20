from edc_lab import RequisitionPanel, LabProfile
from edc_lab.site_labs import site_labs

from .aliquot_types import wb
from .processing_profiles import dbs_processing, infant_insulin, dna_pcr
from .processing_profiles import infant_glucose_processing, elisa_processing
from .processing_profiles import infant_serum_processing, infant_pbmc_pl_processing
from .processing_profiles import infant_wholeblood_processing, infant_paxgene_processing

infant_lab_profile = LabProfile(
    name='td_infant_lab_profile',
    requisition_model='td_infant.infantrequisition')

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
    name='dbs',
    verbose_name='DBS (Store Only)',
    aliquot_type=wb,
    processing_profile=dbs_processing)

infant_elisa_panel = RequisitionPanel(
    name='infant_elisa',
    verbose_name='Infant Elisa',
    aliquot_type=wb,
    processing_profile=elisa_processing)

karabo_wb_pbmc_pl_panel = RequisitionPanel(
    name='karabo_wb_pbmc_pl',
    verbose_name='Karabo WBA/PBMC/PLA ',
    aliquot_type=wb,
    processing_profile=infant_wholeblood_processing
)

infant_paxgene_panel = RequisitionPanel(
    name='infant_paxgene',
    verbose_name='Infant Paxgene',
    aliquot_type=wb,
    processing_profile=infant_paxgene_processing
)

infant_lab_profile.add_panel(infant_glucose_panel)
infant_lab_profile.add_panel(infant_insulin)
infant_lab_profile.add_panel(dna_pcr)
infant_lab_profile.add_panel(serum_panel)
infant_lab_profile.add_panel(infant_pbmc_pl_panel)
infant_lab_profile.add_panel(dbs_panel)
infant_lab_profile.add_panel(infant_elisa_panel)
infant_lab_profile.add_panel(infant_paxgene_panel)
infant_lab_profile.add_panel(karabo_wb_pbmc_pl_panel)

site_labs.register(infant_lab_profile)
