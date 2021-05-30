% PReDict toobox 
% ---------------------------------------------------------------------------
% Provides predicted response to multi-drug cocktails using the effective dose model.
% See more details about the model in :
% "Prediction of multidimensional drug dose responses based on measurements
% of drug pairs" published in PNAS (2016)
% ---------------------------------------------------------------------------
% Input : File with the doses of the cocktail and the measured response.
% The input file should be in csv, text (tab delimited) or xls format
% The data structure is:
% Drug1 ,Drug2,Drug3, ... Response
% 0,   ,0    ,0     , ... 1
% 1,   ,0    ,0     , ... 0.5
% 0.5, ,3    ,5     , ... 0.1 
% ... ...    ...      ... 
% The code can give predictions for any number of drugs.
% ---------------------------------------------------------------------------
% Output : 
% 1. Output File (ExpName-predictions) in the same format. The predicted response is in the last column.
% 2. Figures (in fig,pdf,png,emf format) compares the predicted and measured response. 
%    The figures are located in the folder "ExpName" that the code creates
% ---------------------------------------------------------------------------    
% Two examples are provided:
% Three drugs example - Cm-Ofl-Sal
% Four drugs example - Linc-Cm-Ofl-Tmp

%%

%dir = '/Users/mcadamsjr/Documents/Master_2_Inge/TFE/PReDictToolBox/DIAGONAL_SENS2/';
ExpName= sprintf('VALIDATION_DOSE'); % Try also the four drugs example -'Linc-Cm-Ofl-Tmp'
DataInputFileName=ExpName;
DataOutputFileName=[ExpName '-predictions'];
%% Create folders for the figs
%create_folders_for_figs(ExpName);

%% Read the data that is located in "DataInputFileName" 
[D,g,DrugNames]=load_data(DataInputFileName);
% D(D(:,2)>0,2)=log(D(D(:,2)>0,2))+2.56;
% g=min(g,1);
%% Find D0,n from the single drug dose response
Ndrugs=size(D,2);
for i=1:Ndrugs
    [fi{i}]=fit_single_drug_dose_response_with_names(ExpName,DrugNames,D,g,i);
end
n=1;
BlissModelPrediction=BlissPredict(D,fi);
%% Find aij from the drug pairs dose response
for i=1:Ndrugs
    for j=i+1:Ndrugs
        [fij{n}]=fit_response_for_drug_pairs(ExpName,D,g,DrugNames,i,j,fi);
        aij(i,j)=fij{n}.a;
        aij(j,i)=fij{n}.b;
        n=n+1;
    end;
end
%save([ExpName '_Params'],'fi','aij')
%% Predict the response of the multi-drug cocktails
%PairModelPrediction=PairPredict(D,fi);
DoseModelPrediction=DoseModelPredict(D,fi,aij);
%% Write the reults into the output file
for i=1:Ndrugs
    Dout{i}=D(:,i);
end
OutputTable=table(Dout{:},g,DoseModelPrediction);
OutputTable.Properties.VariableNames(1:Ndrugs)=DrugNames;
writetable(OutputTable,[DataOutputFileName '.csv']);
%% Plot the measured vs predicted response for all data
savename_extra='';
is_display=1;
%[blissR2,blissRMSE,DoseR2,DoseRMSE]=plotExpVsModel(ExpName,g,BlissModelPrediction,DoseModelPrediction,savename_extra);


[blissR2,blissRMSE,DoseR2,DoseRMSE]=plotExpVsModel(ExpName,g(43:end),BlissModelPrediction(43:end),DoseModelPrediction(43:end),savename_extra);
%CalcR2(Var5(43:end),  DoseModelPrediction(43:end))
%CalcRMSE(Var5(43:end),  DoseModelPrediction(43:end))




