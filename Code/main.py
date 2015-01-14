from astropy.io import fits
import numpy as np
import glob

import crop as cr
import rotate as rt
import align as al

# data = fits.getdata("../FITS/Inputs/image0.fits")
# cr.crop("../FITS/Inputs/image*.fits")
al.align("image",4)
# fits.writeto('../FITS/output_file.fits', rt.rotate_image(data, 45), clobber=True)