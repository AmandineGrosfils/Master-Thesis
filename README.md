# Master-Thesis

This repository contains all the needed scripts and data files in order to use ComboFM and the Dose model together. The idea is to use ComboFM the predicts the responses of *pairs* of drugs, that are then used as an iput of the Dose model, which predicts responses of *higher order combinations* (triplet of drug in this work). 

In order to do so, 4 scripts must be used : ( **attention changer noms des scripts**)
  1) CV-Dispatch-S*.py : this script allows to make the different folders the cross-validation, as well as the test set that is kept apart from the cross-validation.
  2) ComboFM.py : runs ComboFM and saves the predictions in a *txt* file.
  3) InputDose.py : from the predictions of ComboFM, creates the input *csv* file for the Dose model
  4) mainDose.m :  run the Dose model and saves the predictions in a *csv* file

The * means represents the fact that there are different possible scenarios, each one having one script to divide the dataset. **trouver un truc pour présenter les 11 scénarios**

The data files used are the following : 

  - NCI-ALMANAC.csv : complete dataset used in ComboFM. This file is divided into a test and a traning set. The training set is divided into different cross-validation folds.
  - 
