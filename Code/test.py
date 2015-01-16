from astropy.io import fits
import numpy
import Image

data, header = fits.getdata("../FITS/f1.fits", header=True)

width = header["NAXIS1"]
height = header["NAXIS2"]
# top,down = [0,0] , [width/2,0]
# left,right = [height/2,0] , [0,0]

# for i in xrange(0,height):
# 	for j in xrange(0,width):
# 		if data[i,j] < 1:
# 			data[i,j] = 0.5
# 		if data[i,j] > 0 and j > top[0]:
# 			top = j,i
# 		if data[i,j] > 0 and j < down[0]:
# 			down = j,i
# 		if data[i,j] > 0 and i > right[0]:
# 			right = j,i
# 		if data[i,j] > 0 and i < left[0]:
# 			left = j,i

# data2 = data[left[0]:right[0],down[0]:top[0]]
#top = right, down = left 
# print top
# print down
# print left
# print right
#solo sirve para f1.fits no se sacar el cuerpo mas grande.

 
img = Image.open("../FITS/f1.fits") # create a new black image
img.show() # create the pixel map
 
# for i in range(img.size[0]):    # for every pixel:
#     for j in range(img.size[1]):
#         pixels[i,j] = data[i,j] # set the colour accordingly
 
# img.show()
# fits.writeto('../FITS/output_file.fits', data2, header, clobber=True)
