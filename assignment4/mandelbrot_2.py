import time
from PIL import Image
from numpy import *
import pylab

fileNam2="mandel_pic_two"
win_fram2=400
xmin=-2.0; xmax=2.0
ymin=-2.0; ymax=2.0
max_N=255

def mandelbrot_two(xmin,xmax,ymin, ymax, fileNam, win_frame):

    begin = time.time()
    
    fileNam2=fileNam
    win_fram2=int(win_frame)

    y,x = ogrid[ xmin:xmax:win_frame*1j, ymin:ymax:win_frame*1j ] # a grid with given values
    c = x+y*1j 
    z = c      # intialize z 
    counting = max_N + zeros(z.shape) #  it will loop til max 255 

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
    draw=mandelbrot_two(xmin,xmax,ymin, ymax, fileNam2, win_fram2)
    
