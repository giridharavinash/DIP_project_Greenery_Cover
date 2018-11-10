import numpy as np
from skimage import io, transform, exposure
from matplotlib import pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
def read_band(n):
    if n in range(1, 12):
        tif_list = get_ipython().getoutput('ls *.TIF')
        band_name = 'B' + str(n) + '.TIF'
        img_idx = [idx for idx, band_string in enumerate(tif_list) if band_name in band_string]
        img = io.imread(tif_list[img_idx[0]])
        return img
    else:
        print('Band number has to be in the range 1-11!')

b4 = read_band(4) 
b3 = read_band(3) 
b2 = read_band(2) 
b8 = read_band(8)


img432_roi = np.dstack((b4, b3, b2))[4400:5200, 3500:4100, :]


b4 = b4/b4.max()
b3 = b3/b3.max()
b2 = b2/b2.max()
b8 = b8/b8.max()


b4 = b4[4400:5200, 3500:4100]
b3 = b3[4400:5200, 3500:4100]
b2 = b2[4400:5200, 3500:4100]
b8 = b8[8800:10400, 7000:8200]



img432 = np.dstack((b4, b3, b2))
img432_2x = transform.rescale(img432, 2)


m = np.sum(img432_2x, axis=2)
ps4 = b8*img432_2x[:, :, 0]/m
ps3 = b8*img432_2x[:, :, 1]/m
ps2 = b8*img432_2x[:, :, 2]/m
img432_ps = np.dstack((ps4, ps3, ps2))


fig = plt.figure(figsize=(12, 9))
fig.set_facecolor('white')

ax1 = fig.add_subplot(121)
ax1.imshow(img432_ps)
plt.title('Pansharpened image')
plt.axis('off')

ax2 = fig.add_subplot(122)
ax2.imshow(img432_roi/65535)
plt.title('Raw image')
plt.axis('off')

plt.show()


fig = plt.figure(figsize=(10, 7))
fig.set_facecolor('white')

for color, channel in zip('rgb', np.rollaxis(img432_ps, axis=-1)):
    counts, centers = exposure.histogram(channel)
    plt.plot(centers[1::], counts[1::], color=color)

plt.show()


fig = plt.figure(figsize=(10, 7))
fig.set_facecolor('white')

for color, channel in zip('rgb', np.rollaxis(img432_roi, axis=-1)):
    counts, centers = exposure.histogram(channel)
    plt.plot(centers[1::], counts[1::], color=color)

plt.show()


img1 = np.empty(img432_ps.shape, dtype='float64')
lims = [(0.088,0.17), (0.108, 0.19), (0.130,0.20)]
for lim, channel in zip(lims, range(3)):
    img1[:, :, channel] = exposure.rescale_intensity(img432_ps[:, :, channel], lim)


img2 = np.empty(img432_roi.shape, dtype='float64')
lims = [(7100,14500), (8200, 14000), (9200,13500)]
for lim, channel in zip(lims, range(3)):
    img2[:, :, channel] = exposure.rescale_intensity(img432_roi[:, :, channel], lim)


fig = plt.figure(figsize=(12, 9))
fig.set_facecolor('white')

ax1 = fig.add_subplot(121)
ax1.imshow(img1)
plt.title('Pansharpened image')
plt.axis('off')

ax2 = fig.add_subplot(122)
ax2.imshow(img2/65535)
plt.title('Raw image')
plt.axis('off')

plt.show()


fig = plt.figure(figsize=(9, 12))
fig.set_facecolor('white')

ax1 = fig.add_subplot(121)
ax1.imshow(img1[750:1050, 880:1040, :])
plt.title('Pansharpened image - zoomed')
plt.axis('off')

ax2 = fig.add_subplot(122)
ax2.imshow(img2[375:525, 440:520, :]/65535)
plt.title('Raw image - zoomed')
plt.axis('off')

plt.show()

