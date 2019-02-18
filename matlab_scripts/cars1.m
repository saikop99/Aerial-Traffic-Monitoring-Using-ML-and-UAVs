% Read video
[filename,pathname] = uigetfile('*.mp4','Select target video');
obj=VideoReader([pathname '/' filename]);
NumberOfFrames = obj.NumberOfFrames;
%
close all
figure(1);
% Read background
background=read(obj,1);
% Square
s1=[208 195];
s2=[300 195];%[300 195];
s3=[100 282];
s4=[227 282]; %[227 282]
r1=[320 195];
r2=[417 195];
r3=[252 282];
r4=[393 282];
lim_fd=[184 282];%lim_fd=[184 282];
lim_cd=[300 370];
lim_fi=[184 282];
lim_ci=[100 200];
auto1=0;
auto2=0;
ind_ant1=0;
ind_ant2=0;
% 
for cnt = 1:3:900 %NumberOfFrames or 81 or 904 (change!)
    the_image=read(obj,cnt);
    imagesc(the_image);
    hold on    
    %horizontal lines
    line([s1(1),s2(1)],[s1(2),s2(2)],'LineWidth',3,'Color','r')
    line([s3(1),s4(1)],[s3(2),s4(2)],'LineWidth',3,'Color','r')
    %vertical lines
    line([s1(1),s3(1)],[s1(2),s3(2)],'LineWidth',3,'Color','r')
    line([s2(1),s4(1)],[s2(2),s3(2)],'LineWidth',3,'Color','r')    
    %horizontal lines
    line([r1(1),r2(1)],[r1(2),r2(2)],'LineWidth',3,'Color','g')
    line([r3(1),r4(1)],[r3(2),r4(2)],'LineWidth',3,'Color','g')
    %vertical lines
    line([r1(1),r3(1)],[r1(2),r3(2)],'LineWidth',3,'Color','g')
    line([r2(1),r4(1)],[r2(2),r3(2)],'LineWidth',3,'Color','g')
    %     axis image off
    % LEFT COMPARATION
    ind1=counter_vhcl(double(the_image),double(background),19,lim_fi,lim_ci);
    % Counting routine          
    if ind_ant1==0 && ind1==1
        auto1=auto1+1;           
    end
    ind_ant1=ind1;
    % RIGHT COMPARATION 
    ind2=counter_vhcl(double(the_image),double(background),19,lim_fd,lim_cd);
    % Counting routine
    if ind_ant2==0 && ind2==1
        auto2=auto2+1;
    end
    ind_ant2=ind2;
    
    title(['Vehicle L: ',num2str(auto1),' Vehicles R: ',num2str(auto2)],'FontSize',15)
    drawnow;
    hold off
end
function [flag]=counter_vhcl(im_ent,back_ground,threshold,lim_row,lim_col)
diferencia=zeros(size(back_ground,1),size(back_ground,2));
for f=lim_row(1):lim_row(2)%izq=184:282 -- izq=184:282
    for c=lim_col(1):lim_col(2)%izq=100:220 -- der=300:370
        diferencia(f,c) = (abs(im_ent(f,c,1)-back_ground(f,c,1)) > threshold) | (abs(im_ent(f,c,2) - back_ground(f,c,2)) > threshold) ...
            | (abs(im_ent(f,c,3) - back_ground(f,c,3)) > threshold);
    end
end
diferencia =bwareaopen(diferencia ,150);
%     imshow(diferencia)
%
[i j]=find(diferencia==1);
fc=[i j];%<--Points to plot
%
% 
if  isempty(fc)
    flag=0;
    return
end
flag=1;
% Rectangulars borders
MinF=min(fc(1:end,1));
MaxF=max(fc(1:end,1));
MinC=min(fc(1:end,2));
MaxC=max(fc(1:end,2));
%Plot rectangle
Xi=MinC;
Yi=MinF;
ancho=abs(MaxC-MinC)+1;
alto    =abs(MaxF-MinF)+1;
end