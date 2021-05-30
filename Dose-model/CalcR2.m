function R2=CalcR2(Exp,Model)
yresid=Exp-Model;
SSresid = sum(yresid.^2);
SStotal = sum((Exp-mean(Exp)).^2);
R2 = 1 - SSresid/SStotal;
