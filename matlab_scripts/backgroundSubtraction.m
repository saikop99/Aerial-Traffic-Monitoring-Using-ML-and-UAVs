%Background Subtraction suing correct illumination, saturation
 I=imread('testImage1.jpg');
 se = strel('disk',15)
 background = imopen(I,se);
imshow(background)
I2 = I - background;
imshow(I2)
I3 = imadjust(I2);
imshow(I3)
bw = imbinarize(I3);
bw = bwareaopen(bw,50);
imshow(bw)
cc = bwconncomp(bw,4)
cc.NumObjects