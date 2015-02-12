from astropy.io import fits
import numpy as np
import crop as cr
import rotate as rt
import scale as sc
import stacking as st

def align(outputDir):

	data = sorted(glob.glob(outputDir+'/Img_3_*.fits'))
	dataI = [0]*len(data)
	DataWidth = {}
	DataHeight = {}
	DataWH = {}
	mulWH = [0]*len(data)

	for i in xrange(0,len(data)):

		# name = data[i].split('/')[-1].split('.')[0]
		image , header = fits.getdata(data[i],header = True)
		# data[i],header[i] = fits.getdata("../FITS/output_"+name+str(i)+"a.fits", header=True)
		DataWidth[i] = header["NAXIS1"]
		DataHeight[i] = header["NAXIS2"]
		mulWH[i] = header["NAXIS1"]*header["NAXIS2"] # guarda el area de la foto
		DataWH[mulWH[i]]= i

	mulMaxWH = sorted(mulWH) #ordena en forma creciente
	mulMaxWH = mulMaxWH[::-1]#ordena en forma descendente
	# width = sorted(width)#ordena en forma creciente
	# width = width[::-1]#ordena en forma descendente
	# height = sorted(height)#ordena en forma creciente
	# height = height[::-1] #ordena en forma descendente

	maxWidth = DataWidth[DataWH[mulMaxWH[0]]]
	maxHeight = DataHeight[DataWH[mulMaxWH[0]]]

	for i in xrange(0,len(data)):

		# dataBigger[i] = DataWH[i] #guarda la posicion de la foto mas grande en orden descendente
		imageData , header = fits.getdata(data[i],header = True)
		# data,header = fits.getdata("../FITS/output_"+name + str(i) +"a.fits",header=True)
		newData = sc.scale_aux(imageData,header['NAXIS1'],header['NAXIS2'],difsize(maxWidth,header['NAXIS1'],maxHeight,header['NAXIS2']))

		if newData.shape[0] > maxHeight:
			fits.writeto(outputDir+'/Img_4'+str(i)+'.fits', rt.rotate_image(newData, 270),header ,clobber=True)
		else:
			fits.writeto(outputDir+'/Img_4'+str(i)+'.fits', newData,header ,clobber=True)
			
	# st.stacking(len(data),maxHeight,maxWidth,inputDir,outputDir)
	# for i in xrange(0,nimages):
	info = [len(data),maxHeight,maxWidth]
	return info
	# 	fits.writeto("../FITS/output_"+name+str(i)+"b.fits", rt.rotate_image(data[i], 45), clobber=True)

def difsize(maxWidth,width,maxHeight,height,):

	propHeight = float(maxHeight)/float(height)
	propWidth = float(maxWidth)/float(width)
	if propHeight >= propWidth:
		return propHeight
	elif propHeight <= propWidth:
		return propWidth








