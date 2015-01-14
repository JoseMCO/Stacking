from astropy.io import fits
import numpy as np
import crop as cr
import rotate as rt

def align(name,nimages):

	data = [0]*nimages
	header =[0]*nimages
	# height[nimages]
	# width[nimages]
	DataWidth = {}
	DataHeight = {}
	DataWH = {}
	mulWH = [0]*nimages

	for i in xrange(0,nimages):

		data[i],header[i] = fits.getdata("../FITS/output_"+name+str(i)+"a.fits", header=True)
		DataWidth[i] = header[i]["NAXIS1"]
		DataHeight[i] = header[i]["NAXIS2"]
		mulWH[i] = header[i]["NAXIS1"]*header[i]["NAXIS2"] #guarda el area de la foto
		DataWH[mulWH[i]]= i
		# width[i] = header[i]["NAXIS1"]
		# height[i] = header[i]["NAXIS2"]

	mulMaxWH = sorted(mulWH)#ordena en forma creciente

	mulMaxWH = mulMaxWH[::-1] #ordena en forma descendente
	print mulMaxWH
	print DataWidth
	print DataHeight
	print DataWH
	# dataBigger[nimages]
	maxWidth = DataWidth[DataWH.values()[0]]
	maxHeight = DataHeight[DataWH.values()[0]]

	for i in xrange(0,nimages):

		# dataBigger[i] = DataWH[i] #guarda la posicion de la foto mas grande en orden descendente
		data[i] = fits.getdata("../FITS/output_"+name + str(DataWH[mulMaxWH[i]]) +"a.fits")

	print DataWH
	for i in xrange(0,nimages):

		fits.writeto("../FITS/output_"+name+str(DataWH[mulMaxWH[i]])+"b.fits", rt.rotate_image(data[i], 45), clobber=True)
