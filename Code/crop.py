from astropy.io import fits
import numpy as np
import glob

def cropAux (originalData):

	height = len(originalData)
	width = len(originalData[0])
	data = np.ndarray(shape=(height,width), dtype=float)

	prom = originalData.mean(axis=1, dtype=float).mean()

	minFilter = prom
	
	for i in xrange(0,height):
		for j in xrange(0,width):
			if originalData[i,j] > minFilter:
				data[i,j] = originalData[i,j]
			else:
				data[i,j] = -1

	maxv = -999999999999
	# se suman al pixel actual los valores de todos los pixeles contiguos y se guarda el maximo valor
	for i in xrange(0,height):
		for j in xrange(0,width):
			if data[i,j] <= minFilter:
				continue
			tmp = minFilter
			if i > 0 and data[i-1,j] > minFilter: #abajo
				tmp += data[i-1,j]
			if i < height-1 and data[i+1,j] > minFilter: #arriba
				tmp += data[i+1,j]
			if j > 0 and data[i,j-1] > minFilter: #izquierda
				tmp += data[i,j-1]
			if j < width-1 and data[i,j+1] > minFilter: #derecha
				tmp += data[i,j+1]
			if i > 0 and j > 0 and data[i-1,j-1] > minFilter: #abajo-izquierda
				tmp += data[i-1,j-1]
			if i < height-1 and j > 0 and data[i+1,j-1] > minFilter: #arriba-izquierda
				tmp += data[i+1,j-1]
			if i > 0 and j < width-1 and data[i-1,j+1] > minFilter: #abajo-derecha
				tmp += data[i-1,j+1]
			if i < height-1 and j < width-1 and data[i+1,j+1] > minFilter: #arriba-derecha
				tmp += data[i+1,j+1]
			data[i,j] = tmp #+= tmp
			if data[i,j] > maxv:
				maxv = data[i,j]

	maxy = maxx = -1
	miny = minx = width+height
	# al grupo que contiene el pixel con el mayor valor, se le setea el mayor valor
	for i in xrange(height-1,-1,-1):
		for j in xrange(width-1,-1,-1):
			if data[i,j] < maxv:
				continue
			tmp = minFilter
			if i > 0 and data[i-1,j] > minFilter: #abajo
				data[i-1,j] = maxv
			if i < height-1 and data[i+1,j] > minFilter: #arriba
				data[i+1,j] = maxv
			if j > 0 and data[i,j-1] > minFilter: #izquierda
				data[i,j-1] = maxv
			if j < width-1 and data[i,j+1] > minFilter: #derecha
				data[i,j+1] = maxv
			if i > 0 and j > 0 and data[i-1,j-1] > minFilter: #abajo-izquierda
				data[i-1,j-1] = maxv
			if i < height-1 and j > 0 and data[i+1,j-1] > minFilter: #arriba-izquierda
				data[i+1,j-1] = maxv
			if i > 0 and j < width-1 and data[i-1,j+1] > minFilter: #abajo-derecha
				data[i-1,j+1] = maxv
			if i < height-1 and j < width-1 and data[i+1,j+1] > minFilter: #arriba-derecha
				data[i+1,j+1] = maxv
			if i < miny:
				miny = i
			if i > maxy:
				maxy = i
			if j < minx:
				minx = j
			if j > maxx:
				maxx = j

	newHeight = maxy - miny
	newWidth = maxx - minx

	newdata = np.ndarray(shape=(newHeight+1,newWidth+1), dtype=float)

	for i in xrange(miny,maxy+1): 
		for j in xrange(minx,maxx+1):
			if originalData[i,j] < minFilter:
				newdata[i-miny, j-minx] = 0
			else:
				newdata[i-miny, j-minx] = originalData[i,j]

	return newdata

def crop(dir,numimage):
	data = glob.glob(dir)
	print data
	for i in xrange(0,len(data)):
		name = data[i].split('/')[-1].split('.')[0]
		print i, name, data[i]
		data[i] = cropAux(fits.getdata(data[i]))
		fits.writeto('../FITS/Outputs/output_'+str(name)+'.fits', data[i], clobber=True)


	# data = glob.glob("../FITS/I/*.fits")

	# for i in xrange(0,len(data)):
	# 	print data[i], i
	# 	data[i] = fits.getdata(data[i])

	# height = width = -1
	# maxs = []
	# for x in xrange(0,len(data)):
	# 	h = len(data[x])
	# 	w = len(data[x][0])
	# 	xmax = ymax = vmax = -1;
	# 	for i in xrange(0,h):
	# 		for j in xrange(0,w):
	# 			if data[x][i,j] > vmax:
	# 				ymax = i
	# 				xmax = j
	# 				vmax = data[x][i,j]
	# 	maxs.append([ymax, xmax])
	# 	h = ymax*2+1 if ( abs(ymax-h) < ymax ) else abs(ymax-h)*2+1
	# 	w = xmax*2+1 if ( abs(xmax-h) < xmax ) else abs(xmax-h)*2+1
	# 	if height < h:
	# 		height = h
	# 	if width < w:
	# 		width = w

	# newdata = np.ndarray(shape=(height,width), dtype=float)

	# h = (height-1)/2
	# w = (width-1)/2
	# for x in xrange(0,len(data)):
	# 	for i in xrange(0,len(data[x])):
	# 		for j in xrange(0,len(data[x][0])):
	# 			newdata[i+(h-maxs[x][0])/2,j+(w-maxs[x][1])/2] += data[x][i,j] 

	# fits.writeto('../FITS/output_file.fits', newdata, clobber=True)
