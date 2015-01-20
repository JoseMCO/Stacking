from astropy.io import fits
import numpy as np
import glob

import crop as cr
import rotate as rt
import align as al



data = [0]*4
header =[0]*4
name = "image"
for i in xrange(0,4):

		cr.crop("../FITS/Inputs/"+name+str(i)+".fits", i)


# data = fits.getdata("../FITS/Inputs/image0.fits")
# cr.crop("../FITS/Inputs/image*.fits")
al.align("image",4)

# fits.writeto('../FITS/output_file.fits', rt.rotate_image(data, 45), clobber=True)