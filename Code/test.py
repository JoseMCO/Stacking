from PIL import Image
import pyfits
import numpy as np
import pylab as py
import img_scale
 
j_img = pyfits.getdata('../FITS/Inputs/B/frame-g.fits')
img = np.zeros((j_img.shape[0], j_img.shape[1]), dtype=float)
img[:,:] = img_scale.sqrt(j_img, scale_min=0, scale_max=10000)
py.clf()
py.imshow(img, aspect='equal')
py.title('Blue = J, Green = H, Red = K')
py.savefig('my_rgb_image.png')
img = Image.open('my_rgb_image.png')
img.show()