import sys
import re
   
def readFile(syntaxFile, themeFile, sourceFile):
        
		#read syntax file
		fopen_syntax = open(syntaxFile, "r")
		
		#creat dictionery for syntax
		syntax=dict()			
		str = fopen_syntax.read().splitlines()
				
		# add to syntax dictionery
		for xx in str:
			# index of starting and end for the key syntax
			str_value=xx.index('"') + 1
			end_value=xx.index('":')	
			
			#index of start and end for the value syntax
			str_key=xx.index(': ')+2
			end_key=len(xx)
			#end_key=str[i].index('\n')

			#dict with key=comment, and value=NNNN.*(?:$|\n)"
			syntax_key=xx[str_key:end_key]
			syntax_value=xx[str_value:end_value]
			
			#key-value is added to syntax dict
			syntax[syntax_key]=syntax_value			
				
				
		#read color theme file and defining dictionery for it
		fopen_theme = open(themeFile, "r")
		theme=dict()
		str2 = fopen_theme.read().splitlines()
		
		for yy in str2:
			#comment: 0;32
			# index of starting is 0 and end for the key theme is
			end2_key=yy.index(':')	
			theme_key=yy[0:end2_key]
			
			#index of start and end for the value syntax
			str2_value=yy.index(':') + 2
			end2_value=len(yy)
			
			theme_value=yy[str2_value:end2_value]
			#adding key-value to theme dictionery
			theme[theme_key]=theme_value	
			     
		#read the source file 
		fopen_source = open(sourceFile, "r")
		str3 = fopen_source.read()		
		
		# every word read is checked in syntax dict
		for i in syntax:		    
			for found in re.findall(syntax[i], str3):
				
				#i is the corresonding key in theme dict
				code = theme[i][2:]
				
				start_code = "\033[{}m".format(code)
				end_code = "\033[0m"
				
				text = syntax[i]
				clour_print = start_code + found + end_code
			
				str3 = str3.replace(found, clour_print)
		
		sys.stdout.write(str3)
		sys.stdout.flush()
		
				
		fopen_syntax.close()
		fopen_theme.close()
		fopen_source.close()
		
if(len(sys.argv) == 4):	
	syntaxFile =sys.argv[1]
	themeFile =sys.argv[2]
	sourceFile_to_colour =sys.argv[3]

	readFile(syntaxFile, themeFile, sourceFile_to_colour)	
else:
	sys.stdout.write("provide correct file inputs:" + '\n')
	sys.stdout.write("python3 highlighter.py syntaxfile themefile sourcefile_to_colour")
	







