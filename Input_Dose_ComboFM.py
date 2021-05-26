import pandas as pd
import numpy as np
import sys
from sys import argv

all_matrices_dose = pd.read_csv('VALIDATION_DOSE.csv')


path = str(sys.argv[1])

Pred_COMBOFM = pd.read_csv(path+'/results/'+ str(sys.argv[2])+'.txt',header = None)

lines = pd.read_csv(path+'/Test.txt', header = None)

almanac = pd.read_csv('ALMANAC_ALL_INTEREST.csv')

almanac_ComboFM = pd.read_csv('NCI-ALMANAC.csv')
matrix_interest = almanac_ComboFM.iloc[lines.values.ravel()]


mask1 = np.logical_and(np.logical_and(almanac['NSC1'] == 123127,almanac['NSC2'] == 125973), almanac['CELLNAME']=='A549/ATCC')
mask2 = np.logical_and(np.logical_and(almanac['NSC2'] == 123127,almanac['NSC1'] == 119875 ), almanac['CELLNAME']=='A549/ATCC')
mask3 = np.logical_and(np.logical_and(almanac['NSC2'] == 125973,almanac['NSC1'] == 119875 ), almanac['CELLNAME']=='A549/ATCC')
mask = np.logical_or(mask1, np.logical_or(mask2, mask3))
sub_almanac = almanac[mask][["NSC1","NSC2","CELLNAME","CONC1","CONC2","TESTVALUE","CONTROLVALUE","TZVALUE"]]

pair1 = almanac[mask1][["NSC1","NSC2","CELLNAME","CONC1","CONC2","TESTVALUE","CONTROLVALUE","TZVALUE"]]
pair1_TZ = pair1["TZVALUE"].mean()
pair1_C = pair1["CONTROLVALUE"].mean()

pair2 = almanac[mask2][["NSC1","NSC2","CELLNAME","CONC1","CONC2","TESTVALUE","CONTROLVALUE","TZVALUE"]]
pair2_TZ = pair2["TZVALUE"].mean()
pair2_C = pair2["CONTROLVALUE"].mean()

pair3 = almanac[mask3][["NSC1","NSC2","CELLNAME","CONC1","CONC2","TESTVALUE","CONTROLVALUE","TZVALUE"]]
pair3_TZ = pair3["TZVALUE"].mean()
pair3_C = pair3["CONTROLVALUE"].mean()

# 123127 Doxo
# 119875 Cis
# 125973 Taxol
# pair 1 : 123127 Doxo & 125973 Taxol
# pair 2 : 123127 Doxo & 119875 Cis
# pair 3 : 125973 Taxol & 119875 Cis

New_percentNOTZ = []


for i in range(matrix_interest.shape[0]):
   
    d1 = matrix_interest.iloc[i]["Drug1"]
    d2 = matrix_interest.iloc[i]["Drug2"]
    
    if d1 == "Doxorubicin hydrochloride" and d2 == "Paclitaxel":
        C = pair1_C
        Tz = pair1_TZ
        C = pair2_C
        Tz = pair2_TZ
    if d1 == "Cisplatin" and d2 == "Paclitaxel":
        C = pair3_C
        Tz = pair3_TZ
        
    value = np.asarray(Pred_COMBOFM)[i][0]
    line = np.asarray(lines)[i][0]

    if value > 0:
        new_Ti = (value/100*(C-Tz)) + Tz

    else : 
        new_Ti = (value/100*Tz) + Tz

    New_percentNOTZ.append(new_Ti/C)



for i in range(matrix_interest.shape[0]):
    line = matrix_interest.iloc[i]
    d1 = line["Drug1"]
    d2 = line["Drug2"]
    c1 = line["Conc1"]*1e6
    c2 = line["Conc2"]*1e6
    c1 = np.around(c1, decimals=5)
    c2 = np.around(c2, decimals=5)

    if d1 == "Doxorubicin hydrochloride":
        d1 = "Doxorubicin"
    if d2 == "Doxorubicin hydrochloride":
        d2 = "Doxorubicin"

    m1 = np.isclose(all_matrices_dose[d1], c1)
    m2 = np.isclose(all_matrices_dose[d2], c2)
    m = np.logical_and(m1,m2)

    all_matrices_dose.loc[m,"Var4"] = New_percentNOTZ[i]
    all_matrices_dose[d1] = np.around(all_matrices_dose[d1], decimals = 3)
    all_matrices_dose[d2] = np.around(all_matrices_dose[d2], decimals = 3)

all_matrices_dose.to_csv('Dose-'+str(sys.argv[1])+'.csv' , sep = ",", index = False)





