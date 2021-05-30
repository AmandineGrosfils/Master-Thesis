function create_folders_for_figs(ExpName)
mkdir(ExpName);
mkdir([ExpName '/fig/']);
mkdir([ExpName '/pdf/']);
%mkdir([ExpName '/emf/']);
mkdir([ExpName '/png/']);