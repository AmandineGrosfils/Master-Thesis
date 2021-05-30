import numpy as np
import pandas as pd
from tqdm import tqdm

# Read the full almanac dataset
data = pd.read_csv('/Users/mcadamsjr/Documents/Master_2_Inge/TFE/ComboFM_code/comboFM_data/NCI-ALMANAC_full_data.csv')

# Remove the NaN values
data_without_nan = data[~np.isnan(data["PercentageGrowth"])]

mask = np.logical_or(data_without_nan["Conc1"]==0, data_without_nan["Conc2"]==0)
data_without_nan_only_mono = data_without_nan[mask]
data_without_nan_only_pair = data_without_nan[~mask]


mask_to_keep = np.ones((data_without_nan_only_pair.shape[0],), dtype=bool)


# Keep only 3x3 dose-response matrices
un = data_without_nan_only_pair.groupby(["Drug1","Drug2","CellLine"]).count().index[data_without_nan_only_pair.groupby(["Drug1","Drug2","CellLine"]).count()["Conc1"]>9]
for d1,d2,cl in tqdm(un):
    mask1 = data_without_nan_only_pair["Drug1"] == d1
    mask2 = data_without_nan_only_pair["Drug2"] == d2
    mask3 = data_without_nan_only_pair["CellLine"] == cl
    mask = np.logical_and(mask1, np.logical_and(mask2, mask3))
    mask_to_keep[mask] = False


data_pair9 = data_without_nan_only_pair[mask_to_keep]

# Total dataset = 3x3 dose-response matrices + mono-therapy data
new_data  = pd.concat([data_pair9,data_without_nan_only_mono],ignore_index=True)

new_data.to_csv('NCI-ALMANAC.csv',  index=False)