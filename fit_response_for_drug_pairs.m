function [fitresultij, gofij] = fit_response_for_drug_pairs(ExpName,D,g,DrugNames,i,j,fi)
%% Find the indexes (exps) where Di~=0 & Dj~=0  and Dk(k~=i & k~=j)=0
NotijInd=(1:size(D,2));
NotijInd([i j])=[];
DijInd=sum(D(:,NotijInd),2)==0  & ~isnan(g);
Di=D(DijInd,i);
Dj=D(DijInd,j);
gij=g(DijInd);
%% Fit the data to the model of Eq.(3) and (4) in
%"Prediction of multidimensional drug dose responses based on measurements
% of drug pairs" published in PNAS 2016
[fitresultij,gofij] =  fit2d(ExpName,Di,Dj,gij,DrugNames{i},DrugNames{j},fi{i},fi{j});
Cab=confint(fitresultij);
if  (Cab(1,1)<0 && Cab(2,1)>0) | (Cab(1,2)<0 && Cab(2,2)>0)
    [fitresultija,gofija] =  fit2d_a_or_b_no_disp(Di,Dj,gij,fi{i},fi{j},1);
    [fitresultijb,gofijb] =  fit2d_a_or_b_no_disp(Di,Dj,gij,fi{i},fi{j},2);
    if gofija.rsquare>gofijb.rsquare
%         [fitresultija,gofija] =  fit2d_a_or_b_no_disp(ExpName,Di,Dj,gij,DrugNames{i},DrugNames{j},fi{i},fi{j},1);
        fitresultij=fitresultija;
        gofij=gofija;
    else
%         [fitresultijb,gofijb] =  fit2d_a_or_b_no_disp(ExpName,Di,Dj,gij,DrugNames{i},DrugNames{j},fi{i},fi{j},2);
        fitresultij=fitresultijb;
        gofij=gofijb;
    end;
end;
