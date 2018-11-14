 h = imread('output3.png');
 hg = rgb2hsv(h);
 [m, n, e] = size(hg);
 mask = 0;
 disp(hg(1:5,1:5,1));
 
 for i=1:m
     for j=1:n
            if(hg(i,j,1)> && hg(i,j,1)<0.6 && hg(i,j,2)>0.5 && hg(i,j,3)>0.5)
                mask=mask+1;
            end
     end
 end

green_pixel_percent = (mask/(m*n))*100;
disp('Green Pixel Percent: ');
disp(green_pixel_percent);