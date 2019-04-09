# Team 17 : Given a satellite image, estimate the amount of green cover
Avinash Nunna 20161176
Nikhilendra Atheti 20161054

This project presents a technique to estimate the amount of green cover and urban cover when a satellite image is given. 
The proposed method is based on preprocessing the satellite image for image enhancement and use NDVI values along with the 
conventional RGB channels to get a segmentation technique which is able to classify green cover, urban cover and water 
cover. Using the two classified outputs collected in the classification step, a much better and accurate classification 
is obtained. The implementation is fully unsupervised and is used to generate the classification of the LANDSAT-8 
satellite image.

1)color_image_processing.py outputs the enhanced image.
2)the above run to pan_sharp.py to get the pansharped image.
3)ndvi_calculation.py outputs the landsat ndvi
4)the folder src has segmnetation codes which output the Final result.

link to input images- https://drive.google.com/open?id=11FNj5cPnBAitDH_ZhIn-KNcLoE-VJAJA
link to output images - https://drive.google.com/open?id=1J_mu81S2pHK_1QYQRCchCliCwaputiVC
