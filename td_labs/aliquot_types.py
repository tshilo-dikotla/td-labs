from edc_lab import AliquotType

pl = AliquotType(name='Plasma', alpha_code='PL', numeric_code='32')

bc = AliquotType(name='Buffy Coat', alpha_code='BC', numeric_code='16')

serum = AliquotType(name='Serum', alpha_code='SERUM', numeric_code='06')

wb = AliquotType(name='Whole Blood', alpha_code='WB', numeric_code='02')

pbmc = AliquotType(name='PBMC', alpha_code='PBMC', numeric_code='31')

wb.add_derivatives(bc, pl, serum, pbmc, wb)
