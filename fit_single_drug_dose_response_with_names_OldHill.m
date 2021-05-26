function [fitresult, gof,xData,yData] = fit_single_drug_dose_response_with_names_OldHill(ExpName,DrugNames,D,g,i, v)
nmax=1000;
%% Find the indexes (exps) where Di~=0 and Dj(j~=i)=0
NotiInd=(1:size(D,2));
NotiInd(i)=[];
DiInd=sum(D(:,NotiInd),2)==0  & ~isnan(g);
%%
[xData, yData] = prepareCurveData(D(DiInd,i) , g(DiInd) );
Nexp=length(xData);
if Nexp<3
    disp(['Error : not enough ('  num2str(Nexp) ') single-drug experiments with drug ' DrugNames{i}]);
    return;
end
if Nexp<5
    disp(['Warning : not enough ('  num2str(Nexp) ') single-drug experiments with drug ' DrugNames{i}] );
    disp('We recommend to measure the single-drug response at least 5 doses');
end
%% Set up fittype and options.
if max(yData)>1
  % t = max(yData);
    t=v;
else
    t = 1;
end

ft = fittype( ' t./(1+(x/x0).^n)','problem','t', 'independent', 'x', 'dependent', 'y' );
opts = fitoptions( 'Method', 'NonlinearLeastSquares' );
opts.Display = 'Off';
opts.Lower = [0 0];
opts.StartPoint = [1 1];
opts.Upper = [nmax max(xData)*10000 ];
% opts.TolFun=1e-16;
% opts.TolX=1e-16;
% opts.MaxFunEvals=1000;
% opts.MaxIter=1000;
% Fit model to data.
[fitresult, gof] = fit( xData, yData, ft, opts, 'problem',t);
%%
f=figure(1000000);clf;hold all;
title(DrugNames{i},'fontweight','normal');
% xData = [0;xData];
% yData = [1;yData];
plot( fitresult, xData, yData ,'o' );
ylim([0 1.3]);
xlim([0 max(xData)*1.1]);
xlabel('Dose');
ylabel('Response');
set(gca,'fontsize',14);
grid on
box on;
hgsave([ExpName '-' DrugNames{i} '-' num2str(v) '.fig']);
saveas(f,[ExpName '-' DrugNames{i} '-' num2str(v) '.pdf'],'pdf')
%print([ExpName '/emf/' DrugNames{i} ],'-dmeta')
%print([ExpName '/png/' DrugNames{i} ],'-dpng','-r0')
%%




