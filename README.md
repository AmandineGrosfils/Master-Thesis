# Master-Thesis

This repository contains all the needed scripts and data files in order to use ComboFM and the Dose model together. The idea is to use ComboFM the predicts the responses of *pairs* of drugs, that are then used as an iput of the Dose model, which predicts responses of *higher order combinations* (triplet of drugs in this work). 

In order to do so, different scripts must be used : 
  1) makeFile.py : create the NCI-ALMANAC.csv file. It is a subset of the NCI-ALMANAC_full_data.csv file. The NaN values are removed, as well as the dose-response matrices that are not of size 3x3.  
  2) CV-Dispatch-* .py : this script allows to make the different folders for the cross-validation, as well as the test set that is kept apart from the cross-validation.
  3) ComboFM.py : runs ComboFM and saves the predictions in a *txt* file. The script calls the utils.py script.
  The ComboFM codes takes 1 argument : the name of the folder containing the CV folds. 
  5) Input_Dose_ComboFM.py : from the predictions of ComboFM, creates the input *csv* file for the Dose model.
  The Input_Dose_ComboFM takes 2 arguments : the name of the folder containing the result of ComboFM and the name of the file containing the predictions of ComboFM (which should be in the folder specified as the first argument).
  6) mainDose.m :  run the Dose model and saves the predictions in a *csv* file. All the .m files are scripts of the Dose model. Note that the Dose model uses the modified Hill function : <img src="https://render.githubusercontent.com/render/math?math=y(x) = \frac{max(Data)}{1%2B(\frac{x}{a})^b}"> 

The * means represents the fact that there are different possible scenarios of use of ComboFM, each one having one script to divide the dataset. See the image below for a explaination/representation of the different scenarios. The color representation is the following : grey = training set, orange = test set. The names correspond to the * in the CV-Dispatch-*.py scripts.

<img width="622" alt="SCENARIOS" src="https://user-images.githubusercontent.com/62287195/119675819-a8d8e000-be3d-11eb-9ac8-6b76b63f47be.png">

The data files used are the following : 

  - NCI-ALMANAC.csv : complete dataset used in ComboFM. This file is a subset of the NCI-ALMANAC_full_data.csv file. The growth percentages are expressed **without time zero measurements**.
  - NCI-ALMANAC_full_data.csv can be downloaded here : https://zenodo.org/record/4129688#.YK5SaC2FBBY. The growth percentages are expressed **without time zero measurements**.
  - ALMANAC_ALL_INTEREST.csv : subset of the complete NCI-ALMANAC dataset from https://wiki.nci.nih.gov/display/NCIDTPdata/NCI-ALMANAC. This file contains only the data concerning the 3 pairs of drugs of interest, as well as their mono-therapy points. The growth percentages are expressed **with and without time zero measurements**.
  - A549_paper.csv : file containing the responses of the triplet of drugs, from https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1006774/ The growth percentages are expressed **without time zero measurements**..
  - VALIDATION_DOSE.csv : input of the Dose model using only the NCI-ALMANAC dataset (without using the predictions of the Dose model). Use the script Input_Dose_validation.py to make this file. The growth percentages are expressed **without time zero measurements**.
 
The set of files used in ComboFM is obtained using the R scripts : https://zenodo.org/record/4129688#.YK5SaC2FBBY (Preprocessing section). The R scripts must be run on the NCI-ALMANAC.csv file. It gives the following files : 
   
    -  cell_lines__gene_expression.csv
    -  cell_lines__one-hot_encoding.csv
    -  drug1__estate_fingerprints.csv
    -  drug1__one-hot_encoding.csv
    -  drug1_concentration__one-hot_encoding.csv
    -  drug1_drug2_concentration__values.csv
    -  drug2__estate_fingerprints.csv
    -  drug2__one-hot_encoding.csv
    -  drug2_concentration__one-hot_encoding.csv
    -  drug2_drug1_concentration__values.csv
    -  drugs__estate_fingerprints.csv
    -  responses.csv
