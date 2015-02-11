import numpy as np

def compare(img1, img2):
	newdata = np.absolute(np.subtract(img1, img2))
	return newdata.mean(axis=1, dtype=float).mean()

