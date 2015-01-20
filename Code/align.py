from astropy.io import fits
import numpy as np
import crop as cr
import rotate as rt
import escalar as es
import stacking as st

def align(name,nimages):

	data = [0]*nimages
	header =[0]*nimages
	height = [0]*nimages
	width = [0]*nimages
	DataWidth = {}
	DataHeight = {}
	DataWH = {}
	mulWH = [0]*nimages

	for i in xrange(0,nimages):

		data[i],header[i] = fits.getdata("../FITS/output_"+name+str(i)+"a.fits", header=True)
		DataWidth[i] = header[i]["NAXIS1"]
		DataHeight[i] = header[i]["NAXIS2"]
		mulWH[i] = header[i]["NAXIS1"]*header[i]["NAXIS2"] # guarda el area de la foto
		DataWH[mulWH[i]]= i
		width[i] = header[i]["NAXIS1"]
		height[i] = header[i]["NAXIS2"]

	mulMaxWH = sorted(mulWH) #ordena en forma creciente
	mulMaxWH = mulMaxWH[::-1]#ordena en forma descendente
	width = sorted(width)#ordena en forma creciente
	width = width[::-1]#ordena en forma descendente
	height = sorted(height)#ordena en forma creciente
	height = height[::-1] #ordena en forma descendente

	maxWidth = DataWidth[0]
	maxHeight = DataHeight[DataWH[mulWH[0]]]

	for i in xrange(0,nimages):

		# dataBigger[i] = DataWH[i] #guarda la posicion de la foto mas grande en orden descendente
		data[i],header[i] = fits.getdata("../FITS/output_"+name + str(i) +"a.fits",header=True)
		newData = es.escalar(data[i],header[i]['NAXIS1'],header[i]['NAXIS2'],difsize(maxHeight,header[i]['NAXIS2']))

		print maxHeight
		print header[i]['NAXIS2']
		print difsize(maxHeight,header[i]['NAXIS2'])
		# #newData = resize(data[i],maxWidth,maxHeight,header[i]['NAXIS1'],header[i]['NAXIS2'])
		# # print newData
		# # header[i]['NAXIS1'] = maxWidth
		# # header[i]['NAXIS2'] = maxHeight
		fits.writeto("../FITS/Outputs/output_"+name+str(i)+"b.fits", newData,header[i] ,clobber=True)

	st.stacking(name,nimages,maxHeight,maxWidth)
	# for i in xrange(0,nimages):

	# 	fits.writeto("../FITS/output_"+name+str(i)+"b.fits", rt.rotate_image(data[i], 45), clobber=True)

def difsize(maxHeight,height):

	propHeight = float(maxHeight)/float(height)
	
	return propHeight







