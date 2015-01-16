from astropy.io import fits
import numpy as np
import crop as cr
import rotate as rt
import escalar as es

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
		# mulWH[i] = header[i]["NAXIS1"]*header[i]["NAXIS2"] # guarda el area de la foto
		DataWH[mulWH[i]]= i
		width[i] = header[i]["NAXIS1"]
		height[i] = header[i]["NAXIS2"]

	mulMaxWH = sorted(mulWH) #ordena en forma creciente
	mulMaxWH = mulMaxWH[::-1]#ordena en forma descendente
	width = sorted(width)#ordena en forma creciente
	width = width[::-1]#ordena en forma descendente
	height = sorted(height)#ordena en forma creciente
	height = height[::-1] #ordena en forma descendente

	maxWidth = DataWidth[DataWH[mulMaxWH[0]]]
	maxHeight = DataHeight[DataWH[mulMaxWH[0]]]

	for i in xrange(0,nimages):

		# dataBigger[i] = DataWH[i] #guarda la posicion de la foto mas grande en orden descendente
		data[i] = fits.getdata("../FITS/output_"+name + str(i) +"a.fits")
		newData = es.escalar(data[i],header[i]['NAXIS1'],header[i]['NAXIS2'],1.5)
		#newData = resize(data[i],maxWidth,maxHeight,header[i]['NAXIS1'],header[i]['NAXIS2'])
		# print newData
		# header[i]['NAXIS1'] = maxWidth
		# header[i]['NAXIS2'] = maxHeight
		fits.writeto("../FITS/output_"+name+str(i)+"b.fits", newData,header[i] ,clobber=True)

	# for i in xrange(0,nimages):

	# 	fits.writeto("../FITS/output_"+name+str(i)+"b.fits", rt.rotate_image(data[i], 45), clobber=True)

# def resize(data,maxWidth,maxHeight,width,height):

# 	difWidth = abs(maxWidth-width)
# 	difHeight = abs(maxHeight-height)
# 	newData = np.zeros((maxWidth,maxHeight))
# 	repeat = 0

# 	if (difWidth*difHeight)%2 == 0:
# 		repeat = 2

# 	else:
# 		repeat = 3
# 	aux = 1

# 	for x in xrange(0,width-1):

# 		for y in xrange(0,height-1):

# 			print data[x][y]
# 			if (aux <= 2 and repeat == 2) or (aux <= 3 and repeat == 3):

# 				newData[x][y] = data[x][y]
# 				newData[x+1][y+1] = data[x][y]
# 				aux += aux

# 			elif (aux == 3 and repeat == 2) or (aux == 4 and repeat == 3):

# 				newData[x][y] = data[x][y]
# 				newData[x+1][y+1] = data[x][y]
# 				newData[x+2][y+2] = data[x][y]
# 				if aux == 3:
# 					aux = 2
# 				else:
# 					aux = 3

# 	return newData







