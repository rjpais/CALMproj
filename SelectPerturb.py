# This script generates a file with the Stable states for a given perturbation selected by user  
 
# Import model perturbations stable states

FILE_NAME = raw_input("Type the name of file .txt")
mutants_SS = open(FILE_NAME,'r') 
 

# Select a perturbation


mut= raw_input("type the perturbation name") 
M = 52  #number of model components is on first line 

# Read the file with all computed stable states and generate list with all the stable states and a string with the node names  


Nodes = "" # string with node names separated by space  
mut_SS = ""  # model pertubation stable states

for line in mutants_SS:
	if (line[0] == "0" or line[0] == "1" or line[0] == "*" ):
		if line.find (mut) > -1:
			if mut.find (",") < 0 and line.find (",") < 0:
				mut_SS = mut_SS + line[0:M]+ "\n"
			elif  mut.find (",") > -1 and line.find (",") > -1:
				mut_SS = mut_SS + line[0:M] + "\n"
	elif (line[0] != "0" and line[0] != "1" and line[0] != "*" and line[0]!=" " and line[0]!= "=" ) and line[0]!= "5" :
		Nodes = Nodes + line 


mutants_SS.close()

# printing 
if len(mut_SS) > 0:
	F=raw_input("type the output file name (name.txt) \n")
	title = mut + " perturbation Stable States \n" 
	File1=open(F, 'w') # stable states for unhealthy tissue (inflammation or hypoxia or ECM-stiffness on). 
	File1.write("==================================================================== \n\tMODEL COMPONENTS \n")
	File1.write(Nodes + "\n")
	File1.write("==================================================================== \n")
	File1.write(title)
	File1.write("==================================================================== \n")	
	File1.write(mut_SS)
	File1.close()

if len(mut_SS) == 0 :
	print "There is no perturbation name in the list!!!"
	print "Please run again the script and insert a new perturbation name."

