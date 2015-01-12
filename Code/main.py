from astropy.io import fits
import numpy as np
import glob

import crop as cr
import rotate as rt

#cr.crop("../FITS/Inputs/image*.fits")

data = fits.getdata("../FITS/Inputs/image0.fits")
fits.writeto('../FITS/output_file.fits', rt.rotate_image(data, 45), clobber=True)