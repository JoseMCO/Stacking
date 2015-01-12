from astropy.io import fits
import numpy as np
import glob

def rotate_coords(x, y, theta, ox, oy):
	s, c = np.sin(theta), np.cos(theta)
	x, y = np.asarray(x) - ox, np.asarray(y) - oy
	return x * c - y * s + ox, x * s + y * c + oy

def rotate_image(src, theta, fill=255):
	theta = -theta*np.pi/180
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
