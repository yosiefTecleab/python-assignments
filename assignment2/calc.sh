#!/bin/bash

if [ $# -eq 0 ]
then
   echo "provide correct command  "
   echo "e.g ./calc.sh S 1 2 3"


elif [ $1 == "S" ]  #sum command
then
total_sum=0      #declare and initialize 

 for i in ${@:2}; do  #skipping the first arguement which is S,P,M,or m
  (( total_sum+=i ))
 done

echo "The sum is $total_sum"


elif [ $1 == "P" ] #product command
then
  total_product=1; #declare and initialize
    for i in ${@:2}; do  
     (( total_product*=i ))
     done 
     echo "The product is $total_product"

elif [ $1 == "M" ]     # max command
then
      max=$2           # initialy assume the first number(which is in second paramer) is the max
      for i in ${@:2} ;
      do
    
      if([ $i -gt $max ]); #max is updated if there is a greater no
      then
           max=$i
      fi      

      done
      echo "the maximum is $max"

elif [ $1 == "m" ]   # min command
then
    min=$2          #assume the first number is the smallest
   for i in ${@:2} ;
   do
      if([ $i -lt $min ]);   #update min if there is smaller no
       then
           min=$i
      fi      
    
    done
   echo "the minumum is $min"


fi




