from edc_lab import LabProfile

from .infant_panels import infant_glucose_panel, infant_insulin, dna_pcr
from .infant_panels import serum_panel, infant_pbmc_pl_panel, dbs_panel

infant_lab_profile = LabProfile(
    name='td_maternal_infant_lab_profile',
    requisition_model='td_maternal.subjectrequisition')


infant_lab_profile.add_panel(infant_glucose_panel)
infant_lab_profile.add_panel(infant_insulin)
infant_lab_profile.add_panel(dna_pcr)
infant_lab_profile.add_panel(serum_panel)
infant_lab_profile.add_panel(infant_pbmc_pl_panel)
infant_lab_profile.add_panel(dbs_panel)
