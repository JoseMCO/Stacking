from astropy.io import fits
import numpy as np
import math

def stacking(name,nimages,maxHeight,maxWidth):

	data = []
	header = []
	finalData = np.zeros((maxWidth,maxHeight))


	for i in range(nimages):

		data,header = fits.getdata("../FITS/Outputs/output_"+name + str(i) +"b.fits",header=True)
		
		for x in range(0,header['NAXIS1']):
			for y in range(0,header['NAXIS2']):

				finalData[x][y] += data[x][y]

	for x in range(maxWidth):
		for y in range(maxHeight):

			finalData[x][y] = float(finalData[x][y]/nimages)

	fits.writeto('../FITS/Outputs/final_output.fits', finalData, clobber=True)
