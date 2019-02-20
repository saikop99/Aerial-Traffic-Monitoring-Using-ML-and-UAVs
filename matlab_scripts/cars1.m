% Read video
[filename,pathname] = uigetfile('*.mp4','Select target video');
obj=VideoReader([pathname '/' filename]);
numberOfFrames = get(obj,'NumberOfFrames')
frameRate=get(obj,'FrameRate')
darkCarvalue=50;
darkCar=rgb2gray(read(obj,1000));
figure(1)
title('darkCars');
imshow(darkCar)
noDarkCar=imextendedmax(darkCar,darkCarValue);
figure(2)
title('Removed dark cars')
imshow(darkCar)
%morphological operations
sedisk=strel('disk',2);
noSmallStructures=imopen(noDarkCar,sedisk);
imshow(noSmallStructures)

%for video
for k=1:numberOfFrames
    singleFrame=read(obj,k);
    I=rgb2gray(singleFrame);
    noSmallStructures=imopen(noDarkCars,sedisk);
    noSmallStructures=bwareaopen(noSmallStructures,150);
    taggedCars(:,:,:,:,k) = singleFrame;
   
    stats = regionprops(noSmallStructures, {'Centroid','Area'});
    if ~isempty([stats.Area])
        areaArray = [stats.Area];
        [junk,idx] = max(areaArray);
        c = stats(idx).Centroid;
        c = floor(fliplr(c));
        width = 2;
        row = c(1)-width:c(1)+width;
        col = c(2)-width:c(2)+width;
        taggedCars(row,col,1,k) = 255;
        taggedCars(row,col,2,k) = 0;
        taggedCars(row,col,3,k) = 0;
    end
end
implay(taggedCars,frameRate);