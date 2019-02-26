clc
clear all
close all
cd ..;
cd ..;
cd ..;
cd ..;
cd home/sai/;
cd Documents/;
cd SIH\ 2019;
cd matlab_scripts/dataset001;
folderData=dir;
s1=['imagedata001' '/' folderData.name];

a=imread('img.jpg');
figure(1)
imshow(a);