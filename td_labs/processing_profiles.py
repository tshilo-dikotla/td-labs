from edc_lab import Process, ProcessingProfile

from .aliquot_types import wb, pl, bc, serum, pbmc

viral_load_processing = ProcessingProfile(name='viral_load', aliquot_type=wb)
vl_pl_process = Process(aliquot_type=pl, aliquot_count=3)
vl_bc_process = Process(aliquot_type=bc, aliquot_count=1)
viral_load_processing.add_processes(vl_pl_process, vl_bc_process)

pbmc_vl_processing = ProcessingProfile(name='pbmc_vl', aliquot_type=wb)
pbmc_pl_process = Process(aliquot_type=pl, aliquot_count=4)
pbmc_process = Process(aliquot_type=pbmc, aliquot_count=4)
pbmc_vl_processing.add_processes(pbmc_pl_process, pbmc_process)

glucose_processing = ProcessingProfile(name='glucose', aliquot_type=wb)
glucose_pl_process = Process(aliquot_type=pl, aliquot_count=3)
glucose_processing.add_processes(glucose_pl_process)

elisa_processing = ProcessingProfile(name='elisa', aliquot_type=wb)
elisa_pl_process = Process(aliquot_type=pl, aliquot_count=1)
elisa_pbmc_process = Process(aliquot_type=pbmc, aliquot_count=1)
elisa_processing.add_processes(elisa_pl_process, elisa_pbmc_process)

infant_pbmc_plasma_processing = ProcessingProfile(
    name='pbmc_plasma_store', aliquot_type=wb)
pl_plasma_process = Process(aliquot_type=pl, aliquot_count=4)
pbmc_plasma_process = Process(aliquot_type=pbmc, aliquot_count=4)
infant_pbmc_plasma_processing.add_processes(
    pl_plasma_process, pbmc_plasma_process)

pbmc_plasma_processing = ProcessingProfile(
    name='pbmc_plasma_store', aliquot_type=wb)
pbmc_plasma_processing.add_processes(
    pl_plasma_process, pbmc_plasma_process)

infant_glucose_processing = ProcessingProfile(
    name='infant_glucose', aliquot_type=wb)
infant_gluc_process = Process(aliquot_type=pl, aliquot_count=1)
infant_glucose_processing.add_processes(infant_gluc_process)

infant_serum_processing = ProcessingProfile(name='serum', aliquot_type=wb)
infant_serum_process = Process(aliquot_type=serum, aliquot_count=1)
infant_serum_processing.add_processes(infant_serum_process)

infant_pbmc_pl_processing = ProcessingProfile(
    name='infant_pbmc_pl', aliquot_type=wb)
infant_pl_process = Process(aliquot_type=pl, aliquot_count=2)
infant_pbmc_process = Process(aliquot_type=pbmc, aliquot_count=7)
infant_pbmc_pl_processing.add_processes(
    infant_pl_process, infant_pbmc_process)

karabo_wb_pbmc_pl_processing = ProcessingProfile(
    name='karabo_wb_pbmc_pl', aliquot_type=wb)

karabo_pbmc_pl_processing = ProcessingProfile(
    name='karabo_pbmc_pl', aliquot_type=wb)

karabo_pl_process = Process(aliquot_type=pl, aliquot_count=3)
karabo_pbmc_process = Process(aliquot_type=pbmc, aliquot_count=3)

karabo_pbmc_pl_processing.add_processes(
    karabo_pl_process, karabo_pbmc_process)

karabo_wb_pbmc_pl_processing.add_processes(
    karabo_pl_process, karabo_pbmc_process)

dbs_processing = ProcessingProfile(name='dbs', aliquot_type=wb)

cd4_processing = ProcessingProfile(name='CD4', aliquot_type=wb)

infant_insulin = ProcessingProfile(name='infant_insulin', aliquot_type=wb)

insulin = ProcessingProfile(name='insulin', aliquot_type=wb)

dna_pcr = ProcessingProfile(name='dna_pcr', aliquot_type=wb)

infant_wholeblood_processing = ProcessingProfile(
    name='infant_wb', aliquot_type=wb)

infant_paxgene_processing = ProcessingProfile(
    name='infant_paxgene', aliquot_type=wb)
