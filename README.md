# Master-Thesis

This repository contains all the needed scripts and data files in order to use ComboFM and the Dose model together. The idea is to use ComboFM the predicts the responses of *pairs* of drugs, that are then used as an iput of the Dose model, which predicts responses of *higher order combinations* (triplet of drug in this work). 

In order to do so, 4 scripts must be used : 
  1) CV-Dispatch-*.py : this script allows to make the different folders the cross-validation, as well as the test set that is kept apart from the cross-validation.
  2) ComboFM.py : runs ComboFM and saves the predictions in a *txt* file. The script calls the utils.py script.
  The ComboFM codes takes 1 argument : the name of the folder containing the CV folds. 
  4) Input_Dose_ComboFM.py : from the predictions of ComboFM, creates the input *csv* file for the Dose model.
  The Input_Dose_ComboFM takes 2 arguments : the name of the folder containing the result of ComboFM and the nmale of the file containing the predictions of ComboFM (which should be in the folder specified as the first argument).
  6) mainDose.m :  run the Dose model and saves the predictions in a *csv* file. All the .m files are scripts of the Dose model.

The * means represents the fact that there are different possible scenarios, each one having one script to divide the dataset. See the image below for a explaination/representation of the different scenarios. The color representation is the following : grey = training set, orange = test set. The names correspond to the * in the CV-Dispatch-*.py scripts.
<img width="622" alt="SCENARIOS" src="https://user-images.githubusercontent.com/62287195/119675819-a8d8e000-be3d-11eb-9ac8-6b76b63f47be.png">


The data files used are the following : 

  - NCI-ALMANAC.csv : complete dataset used in ComboFM. This file is divided into a test and a training set. The training set is divided into different cross-validation folds. **JE SAIS PAS UPLOAD LE FICHIER : TROP LOURD**
  - ALMANAC_ALL_INTEREST.csv : subset of the complete NCI-ALMANAC dataset from https://wiki.nci.nih.gov/display/NCIDTPdata/NCI-ALMANAC. This file contains only the data concerning the 3 pairs of drugs of interest, as well as their mono-therapy points.
  - A549_paper.csv : file containing the responses of the triplet of drugs, from https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1006774/
  - VALIDATION_DOSE.csv : input of the Dose model using only the NCI-ALMANAC dataset (without using the predictions of the Dose model). Use the script Input_Dose_validation.py to make this file.
 
The set of files used in ComboFM is obtained using the R scripts : https://zenodo.org/record/4129688#.YK5SaC2FBBY (Preprocessing section). The R scripts must be run on the NCI-ALMANAC.csv file. It gives the following files (too heavy to put on GitHub) : 
   
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
