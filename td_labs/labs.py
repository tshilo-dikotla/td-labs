from edc_lab.site_labs import site_labs

# from .infant_lab_profiles import infant_lab_profile
from .maternal_lab_profiles import maternal_lab_profile

site_labs.register(maternal_lab_profile)
