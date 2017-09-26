# This script counts the stable states and microenvironment combinations that gives each phenotype taking in account different combinations of of RPTP and FAT4 ligands.
# need to provide the name of the file containing the stable states
# presents the percentages of configurations giving stable states of the related phenotypes

import sys 


# Import unperturbed model stable states (the wild-type) 

if (len(sys.argv)<2):
	sys.exit("please provide a file name on the command line")
else: 
	INPUT_file = open(sys.argv[1],'r') 

# Read the file with all computed stable states and generate 1 list with the stable states and 1 string with the node names  


completeSS = []  # All stable states obtained by the model 

for line in INPUT_file:
	if (line[0] == "0" or line[0] == "1" or line[0] == "*" ):
		completeSS.append(line)

	
INPUT_file.close()


 
def SS_count (SS, CC, PT, count):
	#Function for counting the stable states with a given set of conditions
	global remainInputs
	remainInputs=[]
	count=0
	for i in SS:
                mic = "IL6=" + i[0] + "\t" + "ROS="+ i[1] + "\t"+ "ECM="+ i[2]+ "\t"+ "EGF="+ i[3]+ "\t"+ "HGF="+ i[4] + "\t" + "DELTA="+ i[7]
                if i[len(i)-3:len(i)-1] == PT or PT=="**":
                        if (i[5]== CC[0] or i[5] == "*") and (i[6]== CC[1] or i[6] == "*"):
                                if i[0:5].find('*') < 0 and i[7:len(i)-3].find('*') < 0:
                                        count = count + 1
                                        if PT != "**":
                                                remainInputs.append(mic)
                                                print mic
                                else:
                                        R = i[0:6].count('*') + i[8:len(i)-3].count('*')   
                                        count = count + 2**R
                                        if PT != "**":
                                                remainInputs.append(mic)
                                                print mic
 	return count



# function arguments sets
CC_set = ["00", "01","10", "11"]
PT_set = [ "02", "01", "12", "11", "00", "10"]


Conditions = { "00": "Neighbouring cells signals: RPTP-L = 0 + Dshc1 = 0", "10": "Neighbouring cells signals: RPTP-L = 1 + Dshc1 = 0 ", "01": "Neighbouring cells signals: RPTP-L = 0 + Dshc1 = 1 ","11": "Neighbouring cells signals: RPTP-L = 1 + Dshc1 = 1",}

Phenotypes = { "00": "Amoeboid-like cell adhesion","10": "Mesenchymal-like cell adhesion","02": "Epithelial-like cell adhesion","12": "Collective cell migration adhesion", "01": "Hybrid cell adhesion (partial EMT intermediate)","11": "Collective cell migration adhesion"}


#stable state counts
List_SS = []
#microenvironment counts
List_mic = [ ]


# generation of a set of arguments for counting Stable states function.
# Print the number and % of stable states for each set of conditions. 

print "Microenvironments and stable state counts for cell adhesion phenotypes: \n"
for j in CC_set:
        print "=========================================================================="
	Total_counts=0
	PT_totals= "**"
	remainInputs=[]
	Total_SS = SS_count (completeSS, j , PT_totals, Total_counts)
	phen_SS =[]
	phen_mic =[]
	for k in PT_set:
                print j,": ",Conditions[j],"\n" ,k,": ", Phenotypes[k], "\n"
		PT_counts=0
		PT_SS = SS_count (completeSS, j , k , PT_counts)
		sorted(remainInputs)
		remainInputs2=[]
		for l in range(len(remainInputs)):
			if remainInputs[l] not in remainInputs2:
				remainInputs2.append(remainInputs[l])
		config=0
		for l in range(len(remainInputs2)):
			config =config+2**remainInputs2[l].count('*')   			

		Percent_SS= (float(PT_SS)/Total_SS)*100
		Percent_mic = (float(config)/64)*100
		phen_SS.append(PT_SS)
		phen_mic.append(config)
		print "\n", "total stable states =", PT_SS, "out of ", Total_SS, "(", Percent_SS ,"%)", "\n"
		print "===== CONFIG NUMBER:",config, " PERCENTAGE over 64: ", Percent_mic, "%"
		print "=========================================================================="
	List_SS.append(phen_SS)
	List_mic.append(phen_mic)


print "\n=========================Stable State Counts  ===========================\n"

#list of phenotypes for printing tables
p=-1
print "Phenotypes,AP_02,AP_01, AP_12,AP_11,AP_00,AP_10"	
for i in List_SS:
	p=p+1 
	C= "NCS=" + CC_set[p] + ","
	for j in i:
		C = C + str(j)+ ","
	print C
	



print "\n===================== % Microenvironment combinations =======================\n"

t=-1
print "Phenotypes,AP_02,AP_01, AP_12,AP_11,AP_00,AP_10"	
for i in List_mic:
	t=t+1 
	C= "NCS=" + CC_set[t] + ","
	for j in i:
		C =  C + str(j)+ ","
	print C
		
	
print "\n=========================================================================="
