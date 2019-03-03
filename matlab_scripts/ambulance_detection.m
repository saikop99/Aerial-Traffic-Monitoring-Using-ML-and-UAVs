clear all
close all
clc
[y1 Fs1] = audioread('ambulance.wav');
[y2 Fs2] = audioread('city_ambulance.wav');
figure
q=fft(y1)
plot(q)
figure
plot(y1)
title('Ambulance Sound');
figure
plot(y2)
title('city_ambulance sound');