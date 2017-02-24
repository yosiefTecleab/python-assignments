#!/bin/bash
 

# real time departure from forskningsparken(source rute.no) 

file=$(curl -s "http://mon.ruter.no/SisMonitor/Refresh?stopid=3010370&computerid=acba4167-b79f-4f8f-98a6-55340b1cddb3&isOnLeftSide=true&blocks=&rows=&test=&stopPoint=" | grep -E "<td>|center\">" | cut -d">" -f 2 | cut -d"<" -f 1)
i=0;


if [ $# -eq 0 ]; then # with no flag, no arguement
    echo "The East and West bounds departuring from Forskiningsparken are: "
    echo "$file"
   

elif [ "$1" == "--E" ]; then # with eastbound flag
     # if condition :platform 2
   echo "The Eastbound departuring from Forskiningsparken are:"
   echo "$file"



elif [ "$1" == "--W" ] ; then # with westbound flag
    # if condition :platform 1
   echo "The Westbound departuring from Forskiningsparken are:"
   echo "$file"
  
      
fi








