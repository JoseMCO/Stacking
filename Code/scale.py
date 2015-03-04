import numpy as np
import math
import info_imagen
from astropy.io import fits
import glob
from PIL import Image
import pyfits
import numpy as np
import pylab as py
import img_scale

def scale_aux(image, maxSize):

    h, w = image.shape
    r = float(maxSize[1])/float(w)     

    if (r == 1):
        return h, w, image

    else:

        image_final = np.zeros((round(r*h),round(r*w)))

        for i in range(0,h):
            for j in range(0,w):

                image_final[round(r*i)][round(r*j)] = image[i][j]
    
    return round(r*h), round(r*w), image_final

def scale(outputDir, maxSize):
    data = sorted(glob.glob(outputDir+'/Img_2_*.fits'))
    nmh = 0
    nmw = 0
    dir_png = outputDir+'/PNG_Images' 

    for i in xrange(0,len(data)):
        image = fits.getdata(data[i])
        h,w = image.shape
        
        print "Scale: "+'/Img_2_'+str(i)+'.fits',

        h,w,image = scale_aux(image,maxSize)
        fits.writeto(outputDir+'/Img_3_'+str(i)+'.fits',image, clobber=True)
        
        j_img = pyfits.getdata(outputDir+'/Img_3_'+str(i)+'.fits')
        img = np.zeros((j_img.shape[0], j_img.shape[1]), dtype=float)
        img[:,:] = img_scale.sqrt(j_img, scale_min=0, scale_max=10000)
        py.clf()
        py.imshow(img, aspect='equal')
        py.title('Scale Img_3_'+str(i))
        py.savefig(dir_png+'/Img_3_'+str(i)+'.png')
        img = Image.open(dir_png+'/Img_3_'+str(i)+'.png')
        img.show()
        print "Done."

        if h > nmh:
            nmh = h
        if w > nmw:
            nmw = w

    return (nmh,nmw)


