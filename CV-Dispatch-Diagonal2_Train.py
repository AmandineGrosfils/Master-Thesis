import pandas as pd 
import os 
import numpy as np
from sklearn.utils import check_random_state
from tqdm import tqdm
from sklearn.model_selection import KFold

save_path = "cross-validation_folds_Diagonal2_Train/"
if not os.path.exists(save_path):
    os.mkdir(save_path)

_name_train            = "Train.txt"
_name_train_1 = "Train_CV-1.txt"
_name_train_2 = "Train_CV-2.txt"
_name_train_3 = "Train_CV-3.txt"
_name_train_4 = "Train_CV-4.txt"
_name_train_5 = "Train_CV-5.txt"

_name_test        = "Test.txt"
_name_test_1 = "Test_CV-1.txt"
_name_test_2 = "Test_CV-2.txt"
_name_test_3 = "Test_CV-3.txt"
_name_test_4 = "Test_CV-4.txt"
_name_test_5 = "Test_CV-5.txt"

name_train      = []
name_train_1 = []
name_train_2 = []
name_train_3 = []
name_train_4 = []
name_train_5 = []

name_test = []
name_test_1 = []
name_test_2 = []
name_test_3 = []
name_test_4 = []
name_test_5 = []

def write_in_file(i, l):
    return l.append(i)
def _write_in_file(l, name):
    with open(name, 'w', newline='') as csvfile:
        for li in tqdm(l):
            csvfile.write("{:0.0f}\n".format(li))

def is_diagonal(PAIR_12_CELL, entrie, doses1, doses2):

    if PAIR_12_CELL.iloc[i]["Conc1"]==doses1[0] and  PAIR_12_CELL.iloc[i]["Conc2"]==doses2[0]:
        diagonal = 1
    elif PAIR_12_CELL.iloc[i]["Conc1"]==doses1[1] and  PAIR_12_CELL.iloc[i]["Conc2"]==doses2[1]:
        diagonal = 1
    elif PAIR_12_CELL.iloc[i]["Conc1"]==doses1[2] and  PAIR_12_CELL.iloc[i]["Conc2"]==doses2[2]:
        diagonal = 1
    else:
        diagonal = 0

    return diagonal


# Drugs of interest
Taxol      = 'Paclitaxel'   #= 125973
Cisplatin = 'Cisplatin' #= 119875       
Doxorubicin = 'Doxorubicin hydrochloride' #123127

# Load almanac
data = pd.read_csv('NCI-ALMANAC.csv')

# number of inner folds
n_inner = 5

# For sake of simplicity, add index as a column
data["index"] = list(data.index)

##########################################
mask_mono = np.logical_or(data["Conc1"] == 0, data["Conc2"] == 0) 


PAIR = data[~mask_mono]

all_cell_li = np.unique(PAIR["CellLine"])
all_drugs_1 = np.unique(PAIR["Drug1"])
all_drugs_2 = np.unique(PAIR["Drug2"])

mask_interest1 = np.logical_and(np.logical_and(PAIR['Drug1'] == Doxorubicin, PAIR['Drug2'] == Taxol), PAIR['CellLine'] == "A549/ATCC")
mask_interest2 = np.logical_and(np.logical_and(PAIR['Drug1'] == Cisplatin, PAIR['Drug2'] == Doxorubicin), PAIR['CellLine'] == "A549/ATCC")
mask_interest3 = np.logical_and(np.logical_and(PAIR['Drug1'] == Cisplatin, PAIR['Drug2'] == Taxol), PAIR['CellLine'] == "A549/ATCC")
mask_interest_total = np.logical_or(np.logical_or(mask_interest1, mask_interest2), mask_interest3)

PAIR1 = PAIR[mask_interest1]
PAIR2 = PAIR[mask_interest2]
PAIR3 = PAIR[mask_interest3]

PAIR_NoInterest = PAIR[~mask_interest_total]


#### PART 1 : PAIRS OF INTEREST
# PAIR 1
get_index_pair12  = PAIR1["index"].values

d1 = np.sort(np.unique(PAIR1["Conc1"]))
d2 = np.sort(np.unique(PAIR1["Conc2"]))

for i in range(9):
    diagonal = is_diagonal(PAIR1, i, d1, d2)
    if diagonal == 0:
        write_in_file(get_index_pair12[i], name_test)
    else : 
        write_in_file(get_index_pair12[i], name_train)
        for k in range(1,n_inner+1):
            write_in_file(get_index_pair12[i], eval('name_train_'+str(int(k))))

# PAIR 2
get_index_pair12  = PAIR2["index"].values
d1 = np.sort(np.unique(PAIR2["Conc1"]))
d2 = np.sort(np.unique(PAIR2["Conc2"]))

for i in range(9):
    diagonal = is_diagonal(PAIR2, i, d1, d2)
    if diagonal == 0:
        write_in_file(get_index_pair12[i], name_test)
    else : 
        write_in_file(get_index_pair12[i], name_train)
        for k in range(1,n_inner+1):
            write_in_file(get_index_pair12[i], eval('name_train_'+str(int(k))))

# PAIR 3
get_index_pair12  = PAIR3["index"].values
d1 = np.sort(np.unique(PAIR3["Conc1"]))
d2 = np.sort(np.unique(PAIR3["Conc2"]))
for i in range(9):
    diagonal = is_diagonal(PAIR3, i, d1, d2)
    if diagonal == 0:
        write_in_file(get_index_pair12[i], name_test)
    else : 
        write_in_file(get_index_pair12[i], name_train)
        for k in range(1,n_inner+1):
            write_in_file(get_index_pair12[i], eval('name_train_'+str(int(k))))


#### PART 2 : OTHER PAIRS
random_state = 0
from sklearn.utils import check_random_state
random_state = check_random_state(random_state)

for d1 in tqdm(all_drugs_1):
    m = PAIR_NoInterest['Drug1'] == d1
    m1 = PAIR_NoInterest[m]
    all_drugs_2 = np.unique(m1['Drug2'])
    for d2 in all_drugs_2:
        mask_pair =  np.logical_and(m1["Drug1"] == d1, m1["Drug2"] == d2) 
        PAIR_12 = m1[mask_pair]
        cells = np.unique(PAIR_12['CellLine'])
        for c in cells:
            mask_cell = PAIR_12['CellLine'] == c
            PAIR_12_CELL = PAIR_12[mask_cell]
            get_index_pair12  = PAIR_12_CELL["index"].values
            doses1 = np.sort(np.unique(PAIR_12_CELL["Conc1"]))
            doses2 = np.sort(np.unique(PAIR_12_CELL["Conc2"]))
            fold_test = random_state.randint(5)+1

            for i in range(9):
                entrie = PAIR_12_CELL.iloc[i]
                diagonal = is_diagonal(PAIR_12_CELL, i, doses1, doses2)

                if diagonal == 0:
                    write_in_file(get_index_pair12[i], eval('name_test_'+str(int(fold_test))))
                    for k in range(1,n_inner+1):
                        if k != fold_test:
                            write_in_file(get_index_pair12[i], eval('name_train_'+str(int(k))))  
                else :
                    for k in range(1,n_inner+1):
                        write_in_file(get_index_pair12[i], eval('name_train_'+str(int(k))))   

                write_in_file(get_index_pair12[i], name_train)




MONO = data[mask_mono]
MONO_IDX = MONO["index"].values

print('Writing mono')
# Add mono to every fold
for i in MONO_IDX:
    write_in_file(i, name_train)
    write_in_file(i, name_train_1)
    write_in_file(i, name_train_2)
    write_in_file(i, name_train_3)
    write_in_file(i, name_train_4)
    write_in_file(i, name_train_5)

print("Writing the files")
# Save into CSV files
_write_in_file(name_train, save_path+_name_train)
_write_in_file(name_test, save_path+_name_test)

_write_in_file(name_train_1, save_path+_name_train_1)
_write_in_file(name_train_2, save_path+_name_train_2)
_write_in_file(name_train_3, save_path+_name_train_3)
_write_in_file(name_train_4, save_path+_name_train_4)
_write_in_file(name_train_5, save_path+_name_train_5)

_write_in_file(name_test_1, save_path+_name_test_1)
_write_in_file(name_test_2, save_path+_name_test_2)
_write_in_file(name_test_3, save_path+_name_test_3)
_write_in_file(name_test_4, save_path+_name_test_4)
_write_in_file(name_test_5, save_path+_name_test_5)
