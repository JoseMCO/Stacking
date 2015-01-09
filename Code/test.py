from astropy.io import fits

data, header = fits.getdata("../FITS/frame-g-007907-6-0143.fits", header=True)

width = header["NAXIS1"]
height = header["NAXIS2"]

for i in xrange(0,height):
	for j in xrange(0,width):
		if data[i,j] < .5:
			data[i,j] = .5

fits.writeto('../FITS/output_file.fits', data, header, clobber=True)