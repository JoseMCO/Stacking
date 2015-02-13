from astropy.io import fits
import numpy as np
import glob

def align_aux(image,maxSize):
	h,w = image.shape
	hdiff = (maxSize[0]-h)/2

	newdata = np.zeros((maxSize[0],maxSize[1]))

	for i in xrange(0,h): 
		for j in xrange(0,w):
			newdata[i+hdiff, j] = image[i,j]

	return newdata

def align(outputDir, maxSize):
	data = sorted(glob.glob(outputDir+'/Img_3_*.fits'))
	borders = []
	for i in xrange(0,len(data)):
		image = fits.getdata(data[i])

		print "Align: "+'/Img_3_'+str(i)+'.fits',

		image = align_aux(image, maxSize)
		fits.writeto(outputDir+'/Img_4_'+str(i)+'.fits',image, clobber=True)

		print "Done."
