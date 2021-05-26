function Dieff=calc_effective_dose(D,fi,aij)
Nd=sum(D>0,2);
Ndrug=size(D,2);
Nexp=size(D,1);
for i=1:Ndrug
    if ~isempty(fi{i})
        D_over_D0(:,i)=D(:,i)./fi{i}.x0;
    end;
end;
Progress=(0:0.01:1);p=1;
options=optimset('TolFun',1e-7,'Tolx',1e-64,'MaxFunEvals',10000,'MaxIter',10000,'Display','off');
for nexp=1:Nexp
    if Nd(nexp)==1
        Dieff_over_D0(nexp,:)=D_over_D0(nexp,:);
    else
%                 nexp
        x0 = D_over_D0(nexp,:)*0;
        Dnow=D_over_D0(nexp,:);
        [Dieff_over_D0(nexp,:),fval,exitflag,output] = fmincon(@(x) effective_dose_function(x,Dnow,aij),x0,[],[],[],[],x0*0,x0+1e6,[],options);
        N=1;
        for nn=-2:0.1:10
            if fval<1.3e-4
                break;
            end;
            N=N+1;
            x0 = D_over_D0(nexp,:)*10^nn;
            [Dieff_over_D0(nexp,:),fval,exitflag,output] = fmincon(@(x) effective_dose_function(x,Dnow,aij),x0,[],[],[],[],x0*0,x0+1e6,[],options);
        end;
%         if fval>1.3e-4
%             for nn=0.1:0.1:7
%                 if fval<1.3e-3
%                     break;
%                 end;
%                 N=N+1;
%                 x0 = rand(size(D_over_D0(nexp,:)))*10^nn;
%                 [Dieff_over_D0(nexp,:),fval,exitflag,output] = fmincon(@(x) effective_dose_function(x,Dnow,aij),x0,[],[],[],[],x0*0,x0+1e6,[],options);
%             end;
%         end;
        if fval>1.3e-3
            output.message
            Dieff_over_D0(nexp,:)=Dieff_over_D0(nexp,:)*nan;
            Nd(nexp)
            fval
        end;
    end;
end;

for i=1:Ndrug
    if ~isempty(fi{i})
        Dieff(:,i)=Dieff_over_D0(:,i).*fi{i}.x0;
    end;
end;

