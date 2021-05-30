function [ModelPrediction,Dieff]=DoseModelPredict(D,fi,aij)
%%
%% Calculate the effetive dose
Dieff=calc_effective_dose(D,fi,aij);
%% Calculate the predicted response
ModelPrediction=BlissPredict(Dieff,fi);
