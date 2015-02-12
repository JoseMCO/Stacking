from astropy.io import fits
import numpy as np
import math
import glob

def stacking(maxHeight,maxWidth,outputDir):

	image = sorted(glob.glob(outputDir+'/Img_4_*.fits'))
	length = len(image)
	data = []
	header = []
	finalData = np.zeros((maxWidth,maxHeight))


	for i in range(length):

		data, header = fits.getdata(image[i],header=True)

		if header['NAXIS1'] > maxWidth and header['NAXIS2'] > maxHeight:
		
			for x in range(0,maxWidth):
				for y in range(0,maxHeight):

					finalData[x][y] += data[y][x]

		elif header['NAXIS1'] > maxWidth and header['NAXIS2'] <= maxHeight :

			for x in range(0,maxWidth):
				for y in range(0,header['NAXIS2']):

					finalData[x][y] += data[y][x]

		elif header['NAXIS1'] <= maxWidth and header['NAXIS2'] > maxHeight :

			for x in range(0,header['NAXIS1']):
				for y in range(0,maxHeight):

					finalData[x][y] += data[y][x]
		else:

			for x in range(0,header['NAXIS1']):
				for y in range(0,header['NAXIS2']):

					finalData[x][y] += data[y][x]

	for x in range(maxWidth):
		for y in range(maxHeight):

			finalData[x][y] = float(finalData[x][y])/float(length)

	print "Stack: Done."	
	fits.writeto(outputDir+'/Img_5_final.fits', finalData, clobber=True)
