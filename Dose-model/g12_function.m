function g12=g12_function(x0,y0,a,b,nx,ny,x,y)
% returns the response (g12) to 2 drugs with doses x and y.
% Each drug characterized by a steepness parameter (Hill coefficient) nx (ny)
% and a halfway point x0 (y0). The drug interaction parmeters are a and b. 
% The function uses a solution to Eq (4) in Ref. 1 that was found by 
% matlab symbolic toolbox and coded into D1eff_fun and D2eff_fun.  
% The solotion is substituted into Eq (3) to give the response g12.
% Ref 1: "Prediction of multidimensional drug dose responses based on measurements
% of drug pairs" published in PNAS 2016
g12=1./(1+(D1eff_fun(x,y,x0,y0,a,b)./x0).^nx).*1./(1+(D2eff_fun(x,y,x0,y0,a,b)./y0).^ny);