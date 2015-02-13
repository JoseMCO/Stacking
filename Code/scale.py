import numpy as np
import math
import info_imagen
from astropy.io import fits
import glob

def scale_aux(image, maxSize):

    h, w = image.shape
    r = float(maxSize[1])/float(w) # NO SE COMO SE CALCULA :C
    
    # ------- S I  R A Z O N  E S   1  N O   S E   E S C A L A --------
    if (r == 1):
        return h, w, image

    else:
        # ----------- A G R A N D A R   I M A G E N ------------
        image_final = np.zeros((round(r*h),round(r*w)))
        # print image_final.shape

        for i in range(0,h):
            for j in range(0,w):
                # print r, i, j, r*i, r*j
                image_final[round(r*i)][round(r*j)] = image[i][j]

    # x = y = 0
    # razon = int(round(razon))

    # # ------- I N T E R P O L A C I O N    P R O P I A M E N T E   T A L -----------
    # # 1 Calculamos los porcentajes los cuales son constantes, el calculo se realiza desde (0,0) a (razon, razon)
    
    # porcentajes = []
    # for i in range(razon+1):
    #     for j in range(razon+1):
    #         if i == 0 and j == 0 or i == 0 and j == razon or i == razon and j == 0 or i == razon and j == razon:
    #             continue
    #         else:
    #             suma_distancias = info_imagen.distancia(i,j,0,0) + info_imagen.distancia(i,j,razon,0) + info_imagen.distancia(i,j,0,razon) + info_imagen.distancia(i,j,razon,razon)
    #             porcentajes.append(info_imagen.distancia(i,j,razon,razon)/suma_distancias)
    #             porcentajes.append(info_imagen.distancia(i,j,razon,0)/suma_distancias)
    #             porcentajes.append(info_imagen.distancia(i,j,0,razon)/suma_distancias)
    #             porcentajes.append(info_imagen.distancia(i,j,0,0)/suma_distancias)

    # posicion_vector = 0

    # while x < (NAXIS1-1)*razon:
    #     while y < (NAXIS2-1)*razon:

    #         pos = [x,y,x+razon,y,x,y+razon,x+razon,y+razon]
                                   
    #         for i in range(x,x+razon+1):
    #             for j in range(y,y+razon+1):

    #                 if( i == pos[0] and j == pos[1] or i == pos[2] and j == pos[3] or i == pos[4] and j == pos[5] or i == pos[6] and j == pos[7]):
    #                     continue


    #                 if posicion_vector < 20:
    #                 	matriz_final[i][j] = matriz[x][y] * porcentajes[posicion_vector] + matriz[x][y+razon-1] * porcentajes[posicion_vector+1] + matriz[x+razon-1][y] * porcentajes[posicion_vector+2] + matriz[x+razon-1][y+razon-1] * porcentajes[posicion_vector+3]
    #                 	posicion_vector +=4
                                   
    #         y = y + razon
    #     y = 0
    #     x = x + razon
    
    return round(r*h), round(r*w), image_final

def scale(outputDir, maxSize):
    data = sorted(glob.glob(outputDir+'/Img_2_*.fits'))
    nmh = 0
    nmw = 0
    for i in xrange(0,len(data)):
        image = fits.getdata(data[i])
        h,w = image.shape

        # propHeight = float(maxSize[0])/float(h)
        # propWidth = float(maxSize[1])/float(w)
        # r = 0
        # if propHeight >= propWidth:
        #     r = propHeight
        # elif propHeight <= propWidth:
        #     r = propWidth
        
        print "Scale: "+'/Img_2_'+str(i)+'.fits',

        h,w,image = scale_aux(image,maxSize)
        fits.writeto(outputDir+'/Img_3_'+str(i)+'.fits',image, clobber=True)
        
        print "Done."

        if h > nmh:
            nmh = h
        if w > nmw:
            nmw = w

    return (nmh,nmw)


# import numpy as np
# import math
# import imageInfo

# def scale(data, NAXIS1, NAXIS2, reason):
    
#     # ------- S I  R A Z O N  E S   1  N O   S E   E S C A L A --------
#     if (reason == 1):
#         return data

    
#     if ( reason < 1):
#         # ----------- E N C O G E R     I M A G E N ------------
#         finalData = np.zeros((round((NAXIS1-1)*reason+1),round((NAXIS2-1)*reason+1)))
#         print finalData.shape
#         print data.shape
#         for x in range(NAXIS1):
#             for y in range(NAXIS2):
#                 finalData[round(x*reason)][round(y*reason)] = data[x][y]
#         return finalData
#     else:
#     	# ----------- A G R A N D A R   I M A G E N ------------
#         finalData = np.zeros(((NAXIS1-1)*round(reason)+1,(NAXIS2-1)*round(reason)+1))

#         for x in range(NAXIS1):
#             for y in range(NAXIS2):
#                 finalData[x*round(reason)][y*round(reason)] = data[y][x]


#     x = y = 0
#     reason = int(round(reason))

#     # ------- I N T E R P O L A C I O N    P R O P I A M E N T E   T A L -----------
#     # 1 Calculamos los percentages los cuales son constantes, el calculo se realiza desde (0,0) a (reason, reason)
    
#     percentages = []
#     for i in range(reason+1):
#         for j in range(reason+1):
#             if i == 0 and j == 0 or i == 0 and j == reason or i == reason and j == 0 or i == reason and j == reason:
#                 continue
#             else:
#                 sum_distance = distance(i,j,0,0) + distance(i,j,reason,0) + distance(i,j,0,reason) + distance(i,j,reason,reason)
#                 percentages.append(distance(i,j,reason,reason)/sum_distance)
#                 percentages.append(distance(i,j,reason,0)/sum_distance)
#                 percentages.append(distance(i,j,0,reason)/sum_distance)
#                 percentages.append(distance(i,j,0,0)/sum_distance)

#     position_vector = 0
#     while x < (NAXIS1-1)*reason:
#         while y < (NAXIS2-1)*reason:

#             pos = [x,y,x+reason,y,x,y+reason,x+reason,y+reason]
#             print pos              
#             for i in range(x,x+reason+1):
#                 for j in range(y,y+reason+1):

#                     if( i == pos[0] and j == pos[1] or i == pos[2] and j == pos[3] or i == pos[4] and j == pos[5] or i == pos[6] and j == pos[7]):
#                         continue
                                   
#                     finalData[i][j] = data[x][y] * percentages[position_vector] + data[x][y+reason-1] * percentages[position_vector+1] + data[x+reason-1][y] * percentages[position_vector+2] + data[x+reason-1][y+reason-1] * percentages[position_vector+3]
#                     position_vector +=4
                                   
#             y = y + reason
#         y = 0
#         x = x + reason
    
#     return finalData
