from astropy.io import fits
import numpy as np
import pylab
import pyfits
import glob

def cropAux (originalData):

	height = len(originalData)
	width = len(originalData[0])
	data = np.ndarray(shape=(height,width), dtype=float)

	prom = originalData.mean(axis=1, dtype=float).mean()
	total = 0
	ntotal = 0

	minFilter = prom
	
	for i in xrange(0,height):
		for j in xrange(0,width):
			if originalData[i,j] > minFilter:
				data[i,j] = originalData[i,j]
				total+=originalData[i,j]
				ntotal+=1
			else:
				data[i,j] = 0

	minFilter = total/ntotal

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

	total = 0
	ntotal = 0
	
	# al grupo que contiene el pixel con el mayor valor, se le setea el mayor valor
	for i in xrange(height-1,-1,-1):
		for j in xrange(width-1,-1,-1):
			if data[i,j] < maxv:
				continue
			
			total+=originalData[i,j]
			ntotal+=1

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

	minFilter = total/ntotal

	maxy = maxx = -1
	miny = minx = width+height

	for i in xrange(0,height):
		for j in xrange(0,width):
			if data[i,j] < maxv or originalData[i,j] < minFilter:
				data[i, j] = 0
			else:
				data[i, j] = originalData[i,j]

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

	border = []
	for i in xrange(miny,maxy+1): 
		line = []
		for j in xrange(minx,maxx+1):
			if data[i,j] <= 0:
				newdata[i-miny, j-minx] = 0
			else:
				newdata[i-miny, j-minx] = originalData[i,j]
				line.append((i-miny, j-minx))

		if len(line) > 0:
			border.append(line[0])
		if len(line) > 1:
			border.append(line[-1])

	return border, newdata

def crop(inputDir, outputDir):
	data = glob.glob(inputDir+'/*.fits')
	borders = []

	for i in xrange(0,len(data)):

		name = data[i].split('/')[-1].split('.')[0]
		image = fits.getdata(data[i])
		if isinstance(image, list):
			image = image[0]

		print "Crop: "+'/Img_0_'+str(i)+'.fits'

		fits.writeto(outputDir+'/Img_0_'+str(i)+'.fits',image, clobber=True)
		border, image = cropAux(image)
		fits.writeto(outputDir+'/Img_1_'+str(i)+'.fits',image, clobber=True)
		borders.append(border)
		print "Done."
	return borders

