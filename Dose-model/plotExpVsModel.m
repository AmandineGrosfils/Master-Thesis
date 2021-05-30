function [blissR2,blissRMSE,DoseR2,DoseRMSE]=plotExpVsModel(ExpName,g,BlissModelPrediction,DoseModelPrediction,savename_extra)
BlissModelPrediction=BlissModelPrediction(:);
DoseModelPrediction=DoseModelPrediction(:);
g=g(:);
blissR2=CalcR2(g,BlissModelPrediction);
blissRMSE=CalcRMSE(g,BlissModelPrediction);
DoseR2=CalcR2(g,DoseModelPrediction);
DoseRMSE=CalcRMSE(g,DoseModelPrediction);
f=figure;clf;hold all;
plot(g,BlissModelPrediction,'or','markersize',4, ...
    'displayname',['Bliss, R^2 = ' num2str(max(blissR2,0),2),...
    ',RMSE = ' num2str(blissRMSE,2) ]);
plot(g,DoseModelPrediction,'xb','markersize',6,'linewidth',1, ...
    'displayname',['Dose Model, R^2 = ' num2str(max(DoseR2,0),2),...
    ',RMSE = ' num2str(DoseRMSE,2) ]);
plot([0 1],[0 1],'-k','linewidth',1,'displayname','y=x');
legend show;
legend('Location','northwest');
xlim([0 1]);
ylim([0 1]);
xlabel('Experiment');ylabel('Model');
set(gca,'fontsize',12);grid on; box on;
title([ savename_extra],'fontweight','normal');
%%
%savename= [ExpName ' Exp Vs Model' savename_extra];
%hgsave([ExpName '/fig/' savename '.fig']);
%saveas(f,[ExpName '/pdf/' savename '.pdf'],'pdf')
%saveas(f,[ExpName '/png/' savename '.png'],'png')
%print([ExpName '\emf\' savename ],'-dmeta')
%print([ExpName '/png/' savename],'-dpng','-r0');
%saveas(f,[ExpName '-results.pdf'],'pdf')
