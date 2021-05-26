import pandas as pd
import numpy as np

ALMANAC = pd.read_csv('ALMANAC_ALL_INTEREST.csv')

mask = np.logical_and(np.logical_and(ALMANAC['NSC1'] == 123127,ALMANAC['NSC2'] == 125973), ALMANAC['CELLNAME']=='A549/ATCC')
doxo_tax = ALMANAC[mask]
doxo_tax = doxo_tax[['CONC1', 'CONC2', 'NSC1', 'NSC2', 'PERCENTGROWTHNOTZ']]

mask = np.logical_and(np.logical_and(ALMANAC['NSC2'] == 123127,ALMANAC['NSC1'] == 119875 ), ALMANAC['CELLNAME']=='A549/ATCC')
doxo_cis = ALMANAC[mask]
doxo_cis = doxo_cis[['CONC1', 'CONC2', 'NSC1', 'NSC2', 'PERCENTGROWTHNOTZ']]

mask = np.logical_and(np.logical_and(ALMANAC['NSC2'] == 125973,ALMANAC['NSC1'] == 119875 ), ALMANAC['CELLNAME']=='A549/ATCC')
cis_tax = ALMANAC[mask]
cis_tax = cis_tax[['CONC1', 'CONC2', 'NSC1', 'NSC2', 'PERCENTGROWTHNOTZ']]

all_matrices = pd.concat([doxo_tax, doxo_cis, cis_tax])

mono_mask = ALMANAC['NSC2'] == 0
mono = ALMANAC[mono_mask][['STUDY','NSC1', 'NSC2','CONC1', 'CONC2' ,'PERCENTGROWTHNOTZ', 'CELLNAME']]
mono_tax = mono[np.logical_or(np.logical_and(mono['NSC1'] == 125973, mono['STUDY'] == 'CD040CP38'),  np.logical_and(mono['NSC1'] == 125973, mono['STUDY'] == 'CD086CP130B'))]
mono_tax = mono_tax[mono_tax['CELLNAME'] == 'A549/ATCC']
mono_cis = mono[ np.logical_and(mono['NSC1'] == 119875, mono['STUDY'] == 'CD086CP130B')]
mono_cis = mono_cis[mono_cis['CELLNAME'] == 'A549/ATCC']
mono_dox = mono[np.logical_or(np.logical_and(mono['NSC1'] == 123127, mono['STUDY'] == 'CD040CP38'),  np.logical_and(mono['NSC1'] == 123127, mono['STUDY'] == 'CD086CP130B'))]
mono_dox = mono_dox[mono_dox['CELLNAME'] == 'A549/ATCC']
mono_tax = mono_tax[['CONC1', 'CONC2', 'NSC1', 'NSC2', 'PERCENTGROWTHNOTZ']]
mono_cis = mono_cis[['CONC1', 'CONC2', 'NSC1', 'NSC2', 'PERCENTGROWTHNOTZ']]
mono_dox = mono_dox[['CONC1', 'CONC2', 'NSC1', 'NSC2', 'PERCENTGROWTHNOTZ']]

all_matrices = all_matrices.append(mono_cis, ignore_index = True)
all_matrices = all_matrices.append(mono_tax, ignore_index = True)
all_matrices = all_matrices.append(mono_dox, ignore_index = True)

all_matrices_dose = pd.DataFrame(columns = ['Cisplatin', 'Doxorubicin', 'Paclitaxel', 'Var4'])

for i in range(all_matrices.shape[0]):
	if all_matrices.iloc[i]['NSC1'] == 119875 and all_matrices.iloc[i]['NSC2'] == 125973:
	    cis = all_matrices.iloc[i]['CONC1']
	    pac = all_matrices.iloc[i]['CONC2']
	    rep = all_matrices.iloc[i]['PERCENTGROWTHNOTZ']
	    a_series = pd.Series([cis, 0, pac, rep], index = all_matrices_dose.columns)
	    all_matrices_dose = all_matrices_dose.append(a_series, ignore_index=True)
	    
	if all_matrices.iloc[i]['NSC1'] == 123127 and all_matrices.iloc[i]['NSC2'] == 125973:
	    dox = all_matrices.iloc[i]['CONC1']
	    pac = all_matrices.iloc[i]['CONC2']
	    rep = all_matrices.iloc[i]['PERCENTGROWTHNOTZ']
	    a_series = pd.Series([0, dox, pac, rep], index = all_matrices_dose.columns)
	    all_matrices_dose = all_matrices_dose.append(a_series, ignore_index=True)
	    
	if all_matrices.iloc[i]['NSC2'] == 123127 and all_matrices.iloc[i]['NSC1'] == 119875:
	    cis = all_matrices.iloc[i]['CONC1']
	    dox = all_matrices.iloc[i]['CONC2']
	    rep = all_matrices.iloc[i]['PERCENTGROWTHNOTZ']
	    a_series = pd.Series([cis, dox, 0, rep], index = all_matrices_dose.columns)
	    all_matrices_dose = all_matrices_dose.append(a_series, ignore_index=True)
	    
	if all_matrices.iloc[i]['NSC1'] == 119875  and all_matrices.iloc[i]['NSC2'] == 0:
	    cis = all_matrices.iloc[i]['CONC1']
	    rep = all_matrices.iloc[i]['PERCENTGROWTHNOTZ']
	    a_series = pd.Series([cis, 0, 0, rep], index = all_matrices_dose.columns)
	    all_matrices_dose = all_matrices_dose.append(a_series, ignore_index=True)
	    
	if all_matrices.iloc[i]['NSC1'] == 123127  and all_matrices.iloc[i]['NSC2'] == 0:
	    dox = all_matrices.iloc[i]['CONC1']
	    rep = all_matrices.iloc[i]['PERCENTGROWTHNOTZ']
	    a_series = pd.Series([0, dox, 0, rep], index = all_matrices_dose.columns)
	    all_matrices_dose = all_matrices_dose.append(a_series, ignore_index=True)
	    
	if all_matrices.iloc[i]['NSC1'] == 125973 and all_matrices.iloc[i]['NSC2'] == 0:
	    pax = all_matrices.iloc[i]['CONC1']
	    rep = all_matrices.iloc[i]['PERCENTGROWTHNOTZ']
	    a_series = pd.Series([0, 0, pax, rep], index = all_matrices_dose.columns)
	    all_matrices_dose = all_matrices_dose.append(a_series, ignore_index=True)



all_matrices_dose['Cisplatin'] *= 1e6
all_matrices_dose['Doxorubicin'] *= 1e6
all_matrices_dose['Paclitaxel'] *= 1e6
all_matrices_dose['Var4'] /= 100


triplets = pd.read_csv("A549_paper.csv", delimiter = ';')

triplets = triplets.rename(columns={'Taxol': 'Paclitaxel', 'Experiments ': 'Var4'})
all_matrices_dose = all_matrices_dose.append(triplets)

all_matrices_dose.to_csv('VALIDATION_DOSE.csv', index=False, float_format='%.5f')
