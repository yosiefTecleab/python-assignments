

from PIL import Image
import time
import numpy as np
#from numpy import * 
from numpy cimport *
#cimport numpy as np
import pylab

fileNam2="mandel_pic_three"
win_fram2=400
xxmin=-2; xxmax=2
yymin=-2; yymax=2
max_N=255

def mandelbrot_three( double xmin1,double xmax1,double ymin1,double ymax1,fileNam,double win_fram ):
    
    cdef double begin = time.time()

    fileNam2=fileNam
    cdef double win_fram2=int(win_fram)  
    cdef double xmin=xmin1
    cdef double xmax=xmax1
    cdef double ymin=ymin1
    cdef double ymax=ymax1

    y,x = np.ogrid[ xmin:xmax:win_fram2*1j, ymin:ymax:win_fram2*1j ] # a grid with given values
    c = x+y*1j 
    z = c      # intialize z 
    counting = max_N + np.zeros(z.shape) #  it will loop til max 255 
    
    cdef int i # to iterate faster with c type
    for i in range(max_N):
        z  = z**2 + c 
        out_of_radius2 = abs(z) > 2  # those out of boundry radius 2
        temp = out_of_radius2 & (counting==max_N)  #  out of boundry radius 2 , 255 is assigned 
        counting[temp] = 0                 
        z[out_of_radius2] = 2       # in order to avoid overflow set to 2 for those out of boundry 2
      
    pic=Image.fromarray(counting).convert('RGB')
   
    pic.save(fileNam+".png") 
    pic.show() 

    end = time.time()
    time_ellapsed = (end - begin)
    
    print ("Time ellapsed: ")
    print (time_ellapsed)
    

if __name__ == "__main__":    
    draw=mandelbrot_three(xxmin,xxmax,yymin, yymax, fileNam2, win_fram2)
