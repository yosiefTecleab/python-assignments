
from PIL import Image
import time
import numpy as np
 

fileNam1="mandel_pic_one"
win_fram1=400
#scaling=win_fram1/6
xmin=-2; xmax=2
ymin=-2; ymax=2
N=255

def mandelbrot_one(xmin,xmax,ymin, ymax, fileNam, win_frame):
    
    begin = time.time()
    
    fileNam1=fileNam
    win_fram1=int(win_frame) 
    scaling=win_fram1/4
    array = np.zeros((win_fram1,win_fram1)) #intialize array with 0 values
    
    
    for xi in range(0,win_fram1):
        x=( xi /scaling) - ((win_fram1/2)/scaling)  #the scaled y coordinate is computed
        for yi in range(0,win_fram1):
            counting=0    # counting is resetted for every loop
            y=(yi/scaling) - ((win_fram1/2)/scaling) # based on the scaling get the x axis value
            c=complex(x,y)    #get the constant c 

            if x < xmin or x > xmax or y < ymin or y > ymax:
               continue 
            z = complex(0.0,0.0) 

            while counting < N:  
                z=z*z+c
                if abs(z) > 2.0: # condition if it is out of boundry radius 2
                    break
                counting+=1  # counting the number of iterations it took to go out of radius 2 or the max 255
            array[yi][xi]=counting  

    pic=Image.fromarray(array).convert('RGB')
    
    pic.save(fileNam+".png") # picture is saved as fileName.png
    pic.show()   
    
    end = time.time()
    time_ellapsed = (end - begin)
    
    print ("Time ellapsed: ")
    print (time_ellapsed)
        
if __name__ == "__main__":
    mandelbrot_one(xmin,xmax,ymin, ymax, fileNam1, win_fram1)
    
    
