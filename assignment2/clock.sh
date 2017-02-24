#!/bin/bash

while true; 
do 
  sleep 1
if [ $# -eq 0 ]; #no command passed from terminal
   then
   now_12h=$(date +"%T")
   echo "$now_12h";
   elif [ $1 == "--AMPM" ]; #--AMPM command Passed
   then
   now_24h=$(date +"%r" )
    echo "$now_24h";  
fi
 done



