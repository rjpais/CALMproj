# This script compares the existence of phenotypes in perturbations in comparison with reference (Wild-types)
# Retrives the perturbations that cause loss and gains of phenotypes. 



# Import unperturbed model stable states (the wild-type) 
Ref = open("WT_SS.txt",'r') 


# Import single perturbations stable states 
SP = open("SinglePer.txt",'r') 


NODES = []  # node names  
SSper = []  # All stable states of perturbations 
SSref = []  # All stable states of reference


for line in Ref:
	if (line[0] == "0" or line[0] == "1" or line[0] == "*" ):
		SSref.append(line)
	elif line[0] != "0" and line[0] != "1" and line[0] != "*" and line[0] != "=" and line[0] != " ":
		NODES.append(line)
	
Ref.close()


for line in SP:
	if (line[0] == "0" or line[0] == "1" or line[0] == "*" ):
		SSper.append(line)
	
SP.close()





 
def Perturb_analysis (P, SSr, SSp, PT):
	#Function for counting the stable states with a given set of conditions
	Cr=0
	for i in SSr:
               	if i[49:51]== PT:
			Cr = Cr + 1
	Cp=0
	for i in SSp:
                if i.find(P) > -1:
                       	if i[49:51] == PT:
				Cp = Cp + 1
	if Cp > 0 and Cr == 0: 
		S = 1
	elif Cp == 0 and Cr > 0: 
		S = -1
	else:
		S=0 
 
  	return S




# function arguments sets
P_set =[]


# Generation of a node perturbation set 
for j in NODES[0:len(NODES)-3]:
	KO = " " + j[0:len(j)-1] + " KO"
	E1 = " " + j[0:len(j)-1] + " E1"
	P_set.append(KO)  
	P_set.append(E1)
		 


Output_file1 = open("LOSS_GAIN_phenotypes.txt", "w") 

header= "Perturbations that result in loss or gain of phenotypes: \n"

Output_file1.write(header)


E_down=["Loss of Epithelial adhesion (02)"]
M_down = ["Loss of M2 adhession (10) "]


H1_up=["Gain of hybrid adhesion (12)"]
H2_up=["Gain of hybrid adhesion (11)"]


C1_up=["Gain of hybrid adhesion (12) + (02)"]
C2_up=["Gain of hybrid adhesion (11) + (01)"]

I1 = ["Gain of Epithelial and invasive adhesion phenotypes mesenchymal + hybrid forms leaders + followers (02 + 12)"] 
I2 = ["Gain of Epithelial and invasive adhesion phenotypes mesenchymal + hybrid forms leaders + followers (01 + 11) "] 


A_up=["Gain of amoeboid adhesion (00)"]



for P in P_set:
	E1 = Perturb_analysis (P, SSref, SSper, "02")
	E2 = Perturb_analysis (P, SSref, SSper, "01")
	H1 = Perturb_analysis (P, SSref, SSper, "12")
	H2 = Perturb_analysis (P, SSref, SSper, "11")
	A = Perturb_analysis (P, SSref, SSper, "00")
	M = Perturb_analysis (P, SSref, SSper, "10")
	if E1 == -1:
		E_down.append(P)
	if H1 == 1:
		H1_up.append(P)
	if H2 == 1:
		H2_up.append(P)
	if H1 == 1 and E1 == 0 :
		C1_up.append(P)
	if H2 == 1 and E2 == 0 :
		C2_up.append(P)
	if M == -1:
		M_down.append(P)
	if A == 1:
		A_up.append(P)
	if E1 == 0 and H1== 1 and  M==0 :
		I1.append(P)
	if E1 == 0 and E2 ==0 and H2 == 1 and  M == 0 :
		I2.append(P)

SET = [ E_down, M_down, H1_up, H2_up, C1_up, C2_up, I1, I2, A_up]


Output_file1.write("=================================================\n")


for i  in SET:
	for SP in i:
		Output_file1.write("\n")
		Output_file1.write(SP)
	
	Output_file1.write("\n=================================================\n")
 


Output_file1.close()

			

