clc
clear all
close all
cd ..;
cd ..;
cd ..;
cd ..;
cd /home/sai/;
cd Documents/;
cd SIH_2019;
cd aerial_traffic_monitoring_sih2019;
cd matlab_scripts/imagedata001;
folderData=dir;
for i = 3:134
    s1=['imagedataset001' '/' folderData(i).name];
    sample1{1,i}=s1;
end

cd ..;
cd framedata001;
folderData=dir;
for i=3:134
    s2=['framedata001' '/' folderData(i).name];
    fileID=fopen(folderData(i).name,'r');
    tempData=fscanf(fileID,'%d');
end
