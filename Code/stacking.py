from astropy.io import fits
import numpy as np
import math
import glob
from PIL import Image
import pyfits
import numpy as np
import pylab as py
import img_scale

def stacking(outputDir,maxSize):

	data = sorted(glob.glob(outputDir+'/Img_4_*.fits'))
	dir_png = outputDir+'/PNG_Images'	

	newdata = np.zeros((maxSize[0],maxSize[1]))

	for i in xrange(0,len(data)):
		newdata += fits.getdata(data[i])/len(data)

	fits.writeto(outputDir+'/Img_5.fits', newdata, clobber=True)
	j_img = pyfits.getdata(outputDir+'/Img_5.fits')
	img = np.zeros((j_img.shape[0], j_img.shape[1]), dtype=float)
	img[:,:] = img_scale.sqrt(j_img, scale_min=0, scale_max=10000)
	py.clf()
	py.imshow(img, aspect='equal')
	py.title('Stack Img_5')
	py.savefig(dir_png+'/Img_5.png')
	img = Image.open(dir_png+'/Img_5.png')
	img.show()


	print "Stack: Done."	
