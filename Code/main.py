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
	maxSize = sc.scale(outputDir, maxSize)
	al.align(outputDir, maxSize)
	st.stacking(outputDir, maxSize)

def aux(inputDir,outputDir):
	data = glob.glob(inputDir+'/*.fits')
	print data
	print "1", data[0].split('/')[-1].split('.')[0]
	image1 = fits.getdata(data[0])
	print "2", data[1].split('/')[-1].split('.')[0]
	image2 = fits.getdata(data[1])
	cm.compare(image1, image2)
	
