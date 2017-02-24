import sys

def diff_implementation(original_version, modified_version):
    
		'''
			two input files are read simultonously and their comparison line 
			by line is printed to terminal as required.moreover, the it is saved in the out
			put file diff_output.txt
		'''
		with open(original_version, "r") as f1:
			original = f1.readlines()

		with open(modified_version, "r") as f2:
			modified = f2.readlines()
			
		f3 = open('diff_output.txt','w') 
		
		i=0
		j=0	
		while i < len(original) and j < len(modified): # we check only until we reach the end of file of either 
			#when each corresonding line are not the same																						  
			if original[i] != modified[j]:
					# initial set lines are added
					check=False
					tmp=[]
					k=j
					while k < len(modified) and not check: 
						# plus sign is added as prefixes
						ln="+"+modified[k] 
						tmp.append(ln)
						k=k+1
						if k < len(modified):
							#if so the new lines are added
							if modified[k] == original[i]: 
								j=k
								for z in tmp:
									sys.stdout.write(z)
									f3.write(z)
								check=True
							
					# lines are removed, if they are not added in original and - sign is added in the prefixes
					if not check: 
						ln="-"+original[i] 
						sys.stdout.write(ln )
						f3.write(ln)
						i=i+1 
			#the lines are the same sign o is the prefixs
			elif original[i] == modified[j]: #the lines are the same sign o is the prefixs
				sys.stdout.write("0"+original[i])
				f3.write("0"+original[i])
				i=i+1
				j=j+1
				
		f3.close()

if( len(sys.argv) == 3):	

	original_version =sys.argv[1]
	modified_version =sys.argv[2]
    
	diff_implementation(original_version, modified_version)      	
else:
	sys.stdout.write("provide correct file inputs:" + '\n')
	sys.stdout.write("python my_diff.py origina_file modified_file")
	




