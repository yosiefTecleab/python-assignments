import sys
import math

#how to run the script with a command line or with out 
#$ python rpn.py "1 2 3 * p"
#$ python rpn.py


# function that checks if a number is float
def is_float(num):
    try: 
        x = float(num) 
        return True
    except ValueError:
        return False

array = []

key = ""  

if len(sys.argv)>1:
   key = sys.argv[1]              

while(True): 
 if key == "":
    key = raw_input("provide an input , to exit type q:  ")    
 for i in key.split(' '): # split the input based on space and process each one by one.
    # different_functions(index)
        if is_float(i):
          array.append(i)     #if is float put it to the array.
        else:  
          # addition of the last two numbers and push the resultant          
          if i == '+':      
            num1=float(array.pop())
            num2=float(array.pop())
            num3=num1 + num2
            array.append(num3) # push num3
          # mutiplication of the last two numbers and push the resultant 
          
          elif i == '*':
            num1=float(array.pop())
            num2=float(array.pop())
            num3=num1 * num2
            array.append(num3) 
          elif i == '/': 
            num1=float(array.pop())
            num2=float(array.pop())
            if(num1 == 0):
                print "error: denominatar must be non zero"
                array.append(num2)
                array.append(num1)
            else:
                array.append(num2/num1)
          
          #calculating the square root of the last input and push the result 
          elif i == 'v': 
            num1=float(array.pop())
            array.append(math.sqrt(num1))
     
          #calculating the sine of the last input and push the result 
          elif i == 'sin': 
            num1=float(array.pop())
            array.append(math.sin(num1))
           
          #calculating the cosine of the last input and push the result  
          elif i == 'cos': 
            num1 = float(array.pop())
            array.append(math.cos(num1))

          # q input to exit 
          elif i == 'q':
             exit()
          # p input prints the last in stack with out poping
          elif i == 'p':
            if len(array) == 0 : 
               print "array is Empty"
            else :                 
                print array[len(array)-1] 
                exit()
          else:
            print "not a float number: " , i

 key = ""

     
