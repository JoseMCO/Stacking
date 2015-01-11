from astropy.io import fits
import numpy

originalData, header = fits.getdata("../FITS/frame-i-007907-6-0143.fits", header=True)

width = header["NAXIS1"]
height = header["NAXIS2"]
data = numpy.ndarray(shape=(height,width), dtype=float, order='F')

prom = 0
maxv = -999999999
for i in xrange(0,height):
	for j in xrange(0,width):
		prom += originalData[i,j]/(height*width)
		if originalData[i,j] > maxv:
			maxv = originalData[i,j]

minFilter = prom

for i in xrange(0,height):
	for j in xrange(0,width):
		if originalData[i,j] > minFilter:
			data[i,j] = originalData[i,j]

# se suman al pixel actual los valores de todos los pixeles contiguos
for i in xrange(0,height):
	for j in xrange(0,width):
		tmp = minFilter
		if data[i,j] <= minFilter:
			continue
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
		data[i,j] += tmp

maxx = -1
maxy = -1
maxv = -999999999999

# se busca el pixel con mayor valor
for i in xrange(0,height):
	for j in xrange(0,width):
		if data[i,j] > maxv:
			maxv = data[i,j]
			maxx = j
			maxy = i

print maxv, maxx, maxy

# al grupo que contiene el pixel con el mayor valor, se le setea el mayor valor
for i in xrange(height-1,-1,-1):
	for j in xrange(width-1,-1,-1):
		tmp = minFilter
		if data[i,j] < maxv:
			continue
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

# pixels = []

maxy = maxx = -1
miny = minx = width+height

for i in xrange(0,height):
	for j in xrange(0,width):
		if data[i,j] == maxv:
			if i < miny:
				miny = i
			if i > maxy:
				maxy = i
			if j < minx:
				minx = j
			if j > maxx:
				maxx = j
			# p = (j,i)
			# pixels.append(p)

print minx, maxx, miny, maxy

newHeight = maxy - miny
newWidth = maxx - minx
newdata = numpy.ndarray(shape=(newHeight,newWidth), dtype=float, order='F')

print newHeight, newWidth
for i in xrange(miny,maxy):
	for j in xrange(minx,maxx):
		newdata[i-miny, j-minx] = originalData[i,j]

header["NAXIS1"] = newWidth
header["NAXIS2"] = newHeight

fits.writeto('../FITS/output_file6.fits', newdata, header, clobber=True)
