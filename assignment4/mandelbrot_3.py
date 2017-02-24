
import mandelbrot_3

xmin=-2.0; xmax=2.0
ymin=-2.0; ymax=2.0
fileNam2="mandel_pic_three"
win_fram2=400

print("time ellapsed for cython mandelbrot:")

#mandelbrot_3.mandelbrot_three(-2,2,-2,2,"mandel_pic_three",400)

if __name__ == "__main__":
   mandelbrot_3.mandelbrot_three(xmin,xmax,ymin, ymax, fileNam2, win_fram2)

