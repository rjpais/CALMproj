# This script generates all internal stable states given the combination of phenotypes


import sys 


# Import file with stable states (wild-type or perturbed cases) 

if (len(sys.argv)<2):
	sys.exit("please provide a file name on the command line")
else: 
	INPUT_file = open(sys.argv[1],'r') 

# Read the file with all computed stable states and generate 1 list with the stable states and 1 string with the node names  


modelSS = []  # All stable states obtained by the model 
Nodes = ""
for line in INPUT_file:	
	if (line[0] == "0" or line[0] == "1" or line[0] == "*" and Counter > 10):
		modelSS.append(line)
	elif (line[0] != "0" and line[0] != "1" and line[0] != "*" and line[0] != "=" and line[0] != " "):
		Nodes= Nodes + line[0:-1] + " "
	
INPUT_file.close()



def SS_phenotypes (SS, PT):
	#Function to identify distinct internal stable states for a given phenotype
	Internal_SS = []
	PHENOTYPE = "no"
	for state in SS: 
		if state[-3:-1] == PT:
			PHENOTYPE = "yes"
			if state[8:-3] not in Internal_SS:
				Internal_SS.append(state[8:-3])
	for state in Internal_SS:
			SSpt = state
			print SSpt
	if PHENOTYPE == "no":
		print "not a stable phenotype" 
	return



def SSpattern (SS, PT):
	#Function for identifying conservative activity sates on the stable states that correspond to a given adhesion phenotype
	SS_internal = []
	multivalues = [40]  # position of the multivalued node
	PHENOTYPE="no"
	for state in SS: 
		if state[-3:-1] == PT:
			PHENOTYPE="yes"
			SS_internal.append(state[8:len(state)-1])
	if len(SS_internal) > 0 and PHENOTYPE=="yes":	
		match = SS_internal[0]
		SSpt = ""	
		for i in range(0,len(state)-9):
			SSP=""
			value = 0
			M1 = 0
			M0 = 0
			M2 = 0
			for l in SS_internal:
				if l[i]== match[i] and value != "-":
					value = match[i]
					if (i in multivalues) and l[i]== "2":
						M2 = M2 + 1
 					elif (i in multivalues) and l[i]== "1": 
						M1 = M1 + 1  
 					elif (i in multivalues) and l[i]== "0":
						M0= M0 + 1
				elif l[i]!= match[i]:
					value = "-"
					if (i in multivalues) and l[i]== "2":
						M2 = M2 + 1
 					elif (i in multivalues) and l[i]== "1": 
						M1 = M1 + 1  
 					elif (i in multivalues) and l[i]== "0":
						M0= M0 + 1 
			if i in multivalues:
				if M0 == 0 and M1 != 0 and M2 != 0:
					value = "a" 
				if M0 != 0 and M1 == 0 and M2 != 0:
					value = "b"
				if M0 != 0 and M1 != 0 and M2 == 0:
					value = "c"
			SSpt = SSpt + str(value)
		print SSpt[0:len(SSpt)-2]



print "Internal stable states of phenotypes patterns \n", Nodes 

# function arguments sets
PT_set = [ "02", "01", "12", "11", "00", "10"]
PT_names=[ "Epithelial adhesion phenotype (F = 0 & C = 2)", "Hybrid-like adhesion phenotype 1 (F = 0 & C = 1)" , "Hybrid-like adhesion phenotype 2 (F = 1 & C = 2)", "Hybrid-like adhesion phenotype 3 (F = 1 & C = 1)", "Hybrid-like adhesion phenotype 4 (F = 0 & C = 0)", "Mesenchymal-like adhesion phnenotype (F = 1 & C = 0)", ""] 

n=0
for phenotype in PT_set:
	print PT_names[n]
	SS_phenotypes (modelSS, phenotype)
	SSpattern (modelSS, phenotype)
	print "\n"
	n=n+1

print " - means that all activity degrees are possible \n", " a means that only basal activity degree is not possible (value 0) \n", " b means that only intermediate activity degree is not possible (value 1) \n", " c means that only high activity degree is not possible (value 2) \n" 
 
