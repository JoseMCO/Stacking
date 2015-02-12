from astropy.io import fits
import numpy as np
import glob
import os

import crop as cr
import rotate as rt
import scale as sc
import align as al
import stacking as st
import compare as cm


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
	border = cr.crop(inputDir, outputDir)
	maxSize = rt.rotate(outputDir, border)
	sc.scale(outputDir, maxSize)
	# info = al.align(outputDir)
	# st.stacking(info[0],info[1],outputDir)

def aux(inputDir,outputDir):
	data = glob.glob(inputDir+'/*.fits')
	print data
	print "1", data[0].split('/')[-1].split('.')[0]
	image1 = fits.getdata(data[0])
	print "2", data[1].split('/')[-1].split('.')[0]
	image2 = fits.getdata(data[1])
	cm.compare(image1, image2)
	
# data = [0]*4
# header =[0]*4
# name = "image"
# for i in xrange(0,4):

# 		cr.crop("../FITS/Inputs/"+name+str(i)+".fits", i)


# data = fits.getdata("../FITS/Inputs/image0.fits")
# al.align("image",4)

# fits.writeto('../FITS/output_file.fits', rt.rotate_image(data, 45), clobber=True)

stack("/home/jose/Documents/LIRAE/Practica/stacking/FITS/Inputs/B","/home/jose/Documents/LIRAE/Practica/stacking/FITS/Outputs")
