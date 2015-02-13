from astropy.io import fits
import numpy as np
import math
import glob

def stacking(outputDir,maxSize):
	data = sorted(glob.glob(outputDir+'/Img_4_*.fits'))

	newdata = np.zeros((maxSize[0],maxSize[1]))

	for i in xrange(0,len(data)):
		newdata += fits.getdata(data[i])/len(data)

	fits.writeto(outputDir+'/Img_5.fits', newdata, clobber=True)
	print "Stack: Done."	
