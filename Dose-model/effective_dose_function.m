function F = effective_dose_function(Deff,D,aij)
for i=1:size(D,2)
    Diter=D(i);
    for j=1:size(D,2)
        Diter=Diter./(1+aij(i,j)*Deff(j)/(1+Deff(j)));
    end
    Fi(i)=Deff(i)-Diter;
end
F=sqrt(sum(Fi.^2));