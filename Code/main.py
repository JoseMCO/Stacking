from astropy.io import fits
import numpy as np
import glob
import os

import crop as cr
import rotate as rt
import align as al


def stack(inputDir,outputDir):
	print 'Input Directory:', inputDir
	print 'Output Directory:', outputDir
	for the_file in os.listdir(outputDir):
		file_path = os.path.join(outputDir, the_file)
		try:
			if os.path.isfile(file_path):
				os.unlink(file_path)
		except Exception, e:
			print e
	cr.crop(inputDir, outputDir)
	
# data = [0]*4
# header =[0]*4
# name = "image"
# for i in xrange(0,4):

# 		cr.crop("../FITS/Inputs/"+name+str(i)+".fits", i)


# data = fits.getdata("../FITS/Inputs/image0.fits")
# al.align("image",4)

# fits.writeto('../FITS/output_file.fits', rt.rotate_image(data, 45), clobber=True)