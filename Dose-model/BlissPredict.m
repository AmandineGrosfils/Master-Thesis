function [BlissPrediction,gi]=BlissPredict(D,fi)
Nexp=size(D,1);
BlissPrediction=ones(Nexp,1);
gi=nan(size(D));
for i=1:length(fi)
    if ~isempty(fi{i})
    BlissPrediction=BlissPrediction.*fi{i}(D(:,i)); 
    Nd=(sum(D'>0))';
    gi(:,i)=fi{i}(D(:,i).*Nd);
    end
end