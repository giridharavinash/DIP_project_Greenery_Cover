
import re
import numpy as np
from skimage import io, exposure
from matplotlib import pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')


def read_band(n):
    """
    Load Landsat 8 band
    Input:
    n - integer in the range 1-11
    Output:
    img - 2D array of uint16 type
    """
    if n in range(1, 12):
        tif_list = get_ipython().getoutput('ls *.TIF')
        band_name = 'B' + str(n) + '.TIF'
        img_idx = [idx for idx, band_string in enumerate(tif_list) if band_name in band_string]
        img = io.imread(tif_list[img_idx[0]])
        return img
    else:
        print('Band number has to be in the range 1-11!')

def image_show(img, color_map, title):
    """
    Show image
    Input:
    img - 2D array of uint16 type
    color_map - string
    title - string
    """
    fig = plt.figure(figsize=(10, 10))
    fig.set_facecolor('white')
    plt.imshow(img, cmap=color_map)
    plt.title(title)
    plt.show()


def image_histogram(img):
    """
    Plot image histogram
    Input:
    img - 2D array of uint16 type
    """
    co, ce = exposure.histogram(img)
    
    fig = plt.figure(figsize=(10, 7))
    fig.set_facecolor('white')
    plt.plot(ce[1::], co[1::])
    plt.show()

def image_adjust_brightness(img, limit_left, limit_right, color_map, title):
    """
    Adjust image brightness and plot the image
    Input:
    img - 2D array of uint16 type
    limit_left - integer
    limit_right - integer
    color_map - string
    title - string
    """
    img_ha = exposure.rescale_intensity(img, (limit_left, limit_right))
    
    fig = plt.figure(figsize=(10, 10))
    fig.set_facecolor('white')
    plt.imshow(img_ha, cmap=color_map)
    plt.title(title)
    plt.show()
    
    return img_ha


def get_gain_bias_angle(n):
    """
    Get band reflectance gain, bias, 
    and Sun elevation angle
    Input:
    n - integer in the range 1-11
    Output:
    gain - float
    bias - float
    """
    if n in range(1, 10):
        n_str = str(n)
        s_g = 'REFLECTANCE_MULT_BAND_' + n_str + ' = '
        s_b = 'REFLECTANCE_ADD_BAND_' + n_str + ' = '
    
        fn = get_ipython().getoutput('ls *_MTL.txt')
    
        f = open(fn[0], 'r+')
    
        search_str_g = '(?<=' + s_g + ').*'
        search_str_b = '(?<=' + s_b + ').*'
        search_str_a = '(?<=' + 'SUN_ELEVATION = ' + ').*'
    
        for line in f:
            s0 = re.search(search_str_a, line)
            s1 = re.search(search_str_g, line)
            s2 = re.search(search_str_b, line)
            if s0:
                angle = float(s0.group(0))
            elif s1:
                gain = float(s1.group(0))
            elif s2:
                bias = float(s2.group(0))
    
        f.close()
    
        return gain, bias, angle
    else:
        print('Band number has to be in the range 1-9!')


cd /Users/kronos/gis/l8/kansas_aug/



b4 = read_band(4)
b5 = read_band(5)


b4_gain, b4_bias, angle = get_gain_bias_angle(4)
b5_gain, b5_bias, angle = get_gain_bias_angle(5)

b4_lambda_refl  = (b4_gain * b4 + b4_bias) / np.sin(angle)
b5_lambda_refl  = (b5_gain * b5 + b5_bias) / np.sin(angle)



ndvi = (b5_lambda_refl - b4_lambda_refl) / (b5_lambda_refl + b4_lambda_refl)



img_ha = image_adjust_brightness(ndvi, -0.7695, 1.459, 'OrRd', 'NDVI')



image_show(ndvi[3440:3600, 3060:3200], 'OrRd', 'NDVI - zoomed')

