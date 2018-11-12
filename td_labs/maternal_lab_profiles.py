from edc_lab import LabProfile

from .maternal_panels import cd4_panel, viral_load, pbmc_vl_panel
from .maternal_panels import fasting_glucose, glucose_1h, glucose_2h
from .maternal_panels import pbmc_pl_panel, elisa_panel, insulin

maternal_lab_profile = LabProfile(
    name='td_maternal_maternal_lab_profile',
    requisition_model='td_maternal.subjectrequisition')


maternal_lab_profile.add_panel(cd4_panel)
maternal_lab_profile.add_panel(viral_load)
maternal_lab_profile.add_panel(pbmc_vl_panel)
maternal_lab_profile.add_panel(fasting_glucose)
maternal_lab_profile.add_panel(glucose_1h)
maternal_lab_profile.add_panel(glucose_2h)
maternal_lab_profile.add_panel(pbmc_pl_panel)
maternal_lab_profile.add_panel(elisa_panel)
maternal_lab_profile.add_panel(insulin)
