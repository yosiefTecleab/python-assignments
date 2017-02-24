import sys

size = len(sys.argv)

# for '*' or '*.py' ,no of arguements is greater than 2
if size > 2: 
        word_count=0  # initialize count
        for filename in sys.argv[1:]: # loop through all avoiding the filename which is index 0
           fil=open(filename)
   	   x=fil.read()
           no_of_words = len(x.split(' ')) # count words in a line
           fil.close() 
	   word_count= word_count + no_of_words 
        
        print "Total number of words are:" , word_count 
          
  
elif size==2:

            file_name=sys.argv[1] #first arguement in the command is file name 
            fil = open(file_name)
            x = fil.read()
            fil.close()    
            no_of_lines = sum(i.count(b'\n') for i in x) # count lines 
            no_of_words = len(x.split(' ')) # count the words
            no_of_characters = len(x) #count characters
           
            print  no_of_lines , " ", no_of_words," ", no_of_characters, " ", file_name

elif size!=2:

        print "incorrect command input, it should be:"
        print "python wc.py filename"
        print "python wc.py *"



