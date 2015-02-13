from astropy.io import fits
import numpy as np
import glob
import math

def rotate_coords(x, y, theta, ox, oy):
	s, c = np.sin(theta), np.cos(theta)
	x, y = np.asarray(x) - ox, np.asarray(y) - oy
	return x * c - y * s + ox, x * s + y * c + oy

def rotate_image(src, theta, fill=0):
	# theta = -theta*np.pi/180
	oy = len(src)
	ox = len(src[0])

	sh, sw = src.shape

	cx, cy = rotate_coords([0, sw, sw, 0], [0, 0, sh, sh], theta, ox, oy)

	dw, dh = (int(np.ceil(c.max() - c.min())) for c in (cx, cy))

	dx, dy = np.meshgrid(np.arange(dw), np.arange(dh))

	sx, sy = rotate_coords(dx + cx.min(), dy + cy.min(), -theta, ox, oy)

	sx, sy = sx.round().astype(int), sy.round().astype(int)

	mask = (0 <= sx) & (sx < sw) & (0 <= sy) & (sy < sh)

	dest = np.empty(shape=(dh, dw), dtype=src.dtype)

	dest[dy[mask], dx[mask]] = src[sy[mask], sx[mask]]

	dest[dy[~mask], dx[~mask]] = fill

	return dest

def fartestPoints(border):
	dist = []
	for i in xrange(0,len(border)):
		for j in xrange(0,len(border)):
			y1,x1 = border[i]
			y2,x2 = border[j]
			d = (x1-x2)**2 + (y1-y2)**2
			d = math.sqrt(d)
			dist.append((d,border[i],border[j]))
	maxd = 0
	points = 0
	for i in xrange(0,len(dist)):
		if dist[i][0] > maxd:
			points = (dist[i][1],dist[i][2])
			maxd = dist[i][0]

	return points

def theta(points):
	y1,x1 = points[0]
	y2,x2 = points[1]
	theta = (y2-y1+.0)/(x2-x1+.0)
	theta = math.atan(theta)
	return theta

def rotate(outputDir, border):
	maxHeight = 0
	maxWidth = 0
	data = sorted(glob.glob(outputDir+'/Img_1_*.fits'))
	for i in xrange(0,len(data)):
		image = fits.getdata(data[i])
		points = fartestPoints(border[i])
		image = rotate_image(image,theta(points))

		print "Rotate: "+'/Img_1_'+str(i)+'.fits',

		fits.writeto(outputDir+'/Img_2_'+str(i)+'.fits',image, clobber=True)
		
		print "Done."

		h,w = image.shape
		if h > maxHeight:
			maxHeight = h
		if w > maxWidth:
			maxWidth = w

	return (maxHeight,maxWidth)
