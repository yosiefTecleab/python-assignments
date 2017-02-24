from mandelbrot_1 import *
from mandelbrot_2 import *
from mandelbrot_3 import *

import sys

if len(sys.argv)!=1:
    input_terminal=sys.argv[1]
    
    
    if input_terminal=='-python' or input_terminal=='-numpy' or input_terminal=='-cython':
              
        xmin=float(input("give Xmin: "))
        xmax=float(input("give Xmax: "))
        ymin=float(input("give Ymin: "))
        ymax=float(input("give Ymax: "))
        fileNam=input("give file name:  ")
        win=float(input("choose resolution 100, 400, 600:  "))
        
        if input_terminal=='-python' :
            mandelbrot_one(xmin,xmax,ymin,ymax,fileNam,win)

        elif input_terminal=='-numpy':
            mandelbrot_two(xmin,xmax,ymin,ymax,fileNam,win)

        elif input_terminal=="cython" :          
            mandelbrot_3.mandelbrot_three(xmin,xmax,ymin,ymax,fileNam,win)

    elif input_terminal=='--help':
        print("3 different mandelbrot implementations, type:")
        print("mandelbrotInterface.py -python for python  implementation ")
        print("mandelbrotInterface.py -numpy  for numpy   implementation ")
        print("mandelbrotInterface.py -cython for cython  implementation ")
        
              
else:   
     print ("incorrect command line arguments. provide")
     print(" mandelbrotInterface.py --help ")
     print ("to choose options")








