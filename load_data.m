function [D,g,DrugNames]=load_data(DataFileName)
filename=[DataFileName '.csv'];
Input=dlmread(filename,',',1,0);
%% Read drug names
f=fopen(filename);
line=fgetl(f);
fclose(f);
Ind=[0 regexp(line,',')];
for i=1:length(Ind)-1
    DrugNames{i}=line(Ind(i)+1:Ind(i+1)-1);
end;    
%% D - The doses of drug 1..n in the cocktail
D=Input(:,1:end-1);
%% g - the messured response for drug 1..n in the doses D
g=Input(:,end);
%%

