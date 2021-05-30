function [fitresult, gof] = fit2d_a_or_b_no_disp(d1,d2,g12,f1,f2,a_or_b)
%% Fit the function coded in g12_function (see documentation) to the two-drug data experiment named "Expname".
% d1,d2 - the doses of the two drugs
% g12 - the measured response 
% name1,name2 - the drug names
% f1,f2 - the single-drug functions
%% Initilize the single-drug parameters (n,D0)
%  we allow n and D0(x0) to change within their uncertainty estimated from the single-drug measurements. 
x0=f1.x0;
nx=f1.n;
y0=f2.x0;
ny=f2.n;
conf1=confint(f1);
conf2=confint(f2);
dnx=diff(conf1(:,1))/20000;
dny=diff(conf2(:,1))/20000;
dx0=diff(conf1(:,2))/20000;
dy0=diff(conf2(:,2))/20000;

%%
[xData, yData, zData] = prepareSurfaceData( d1, d2, g12 );
if a_or_b==1
    a_low=-0.9999;
    b_low=0;
    a_high=inf;
    b_high=1e-6;
    dx0i=dx0;
else
    b_low=-0.9999;
    a_low=0;
    b_high=inf;
    a_high=1e-6;
    dy0i=dy0;
end;
    

ft = fittype( 'g12_function(x0,y0,a,b,nx,ny,x,y)', 'independent', {'x', 'y'}, 'dependent', 'z' );
opts = fitoptions( 'Method', 'NonlinearLeastSquares' );
opts.Lower = [a_low b_low  max(nx-dnx,0) max(ny-dny,0) max(x0-dx0,0)  max(y0-dy0,0) ];
opts.Upper = [a_high  b_high nx+dnx ny+dny x0+dx0 y0+dy0 ];
opts.StartPoint = [0 0 nx ny x0 y0 ];
[fitresult, gof] = fit( [xData, yData], zData, ft, opts );
% %%
% f=figure(1111);
% h=plot( fitresult, [xData, yData], zData );
% alpha(.7)
% title(ExpName);
% grid on;
% box on;
% colormap jet;
% view( 73.5, 16.0 );
% xlabel(name1);
% ylabel(name2);
% zlabel('Response');
% set(gca,'fontsize',14);
% zlim([0 1]);
% title([name1 '-' name2 ': Response'],'fontweight','normal');
% %%
% savename=[name1 '-' name2 ' Response'];
% hgsave([ExpName '\fig\' savename '.fig']);
% saveas(f,[ExpName '\pdf\' savename '.pdf'],'pdf')
% print([ExpName '\emf\' savename],'-dmeta')
% print([ExpName '\png\' savename],'-dpng','-r0');
% 
% %%
% f=figure(2222);
% h=plot( fitresult, [xData, yData], zData, 'Style', 'Residual' );
% grid on
% view( 73.5, 16.0 );
% alpha(.2)
% grid on
% view( 60.5, 14.0 );
% xlabel(name1);
% ylabel(name2);
% zlabel('Residual');
% set(gca,'fontsize',14);
% grid on
% title([name1 '-' name2 ': Residuals'],'fontweight','normal');
% %%
% savename=[name1 '-' name2 ' Residual'];
% hgsave([ExpName '\fig\' savename '.fig']);
% saveas(f,[ExpName '\pdf\' savename '.pdf'],'pdf')
% print([ExpName '\emf\' savename ],'-dmeta')
% print([ExpName '\png\' savename],'-dpng','-r0');
% %%
% f=figure(3333);clf;hold all;
% I=d1>0 & d2 >0;
% g=zData(I);
% DoseModelPrediction=fitresult([xData(I), yData(I)]);
% BlissModelPrediction=f1(d1(I)).*f2(d2(I));
% plot(g,BlissModelPrediction,'or','markersize',4, ...
%     'displayname',['Bliss, R^2 = ' num2str(CalcR2(g,BlissModelPrediction),2),...
%     ',RMSE = ' num2str(CalcRMSE(g,BlissModelPrediction),2) ]);
% plot(g,DoseModelPrediction,'xb','markersize',6,'linewidth',1, ...
%     'displayname',['Dose Model, R^2 = ' num2str(CalcR2(g,DoseModelPrediction),2),...
%     ',RMSE = ' num2str(CalcRMSE(g,DoseModelPrediction),2) ]);
% plot([0 1],[0 1],'-k','linewidth',1,'displayname','y=x');
% legend show;
% legend('Location','northwest');
% xlim([0 1]);
% ylim([0 1]);
% xlabel('Experiment');ylabel('Model');
% set(gca,'fontsize',12);grid on; box on;
% title(ExpName,'fontweight','normal');
% title([ name1 '-' name2 ': Exp Vs Model'],'fontsize',12,'fontweight','normal');
% %%
% savename=[ name1 '-' name2 ' ExpVsModel'];
% hgsave([ExpName '\fig\' savename '.fig']);
% saveas(f,[ExpName '\pdf\' savename '.pdf'],'pdf')
% print([ExpName '\emf\' savename ],'-dmeta')
% print([ExpName '\png\' savename],'-dpng','-r0');
% 
% 
% 
% 
