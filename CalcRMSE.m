function RMSE=CalcRMSE(Exp,Model)
yresid=Exp-Model;
RMSE = sqrt(mean(yresid.^2));
