# This script search for each perturbation and compares the number of stable states of each phenotype with the reference (Wild_Type) 



# Import unperturbed model stable states (the wild-type) 
Ref = open("WT_SS.txt",'r') 


# Import single perturbations stable states 
SDP = open("SingleDoublePer.txt",'r') 



NODES = []  # node names  

dpSS = []
spSS = []  # All stable states of perturbations 
SSref = []  # All stable states of reference

P12_names =[]

for line in Ref:
	if (line[0] == "0" or line[0] == "1" or line[0] == "*" ):
		SSref.append(line)
	elif line[0] != "0" and line[0] != "1" and line[0] != "*" and line[0] != "=" and line[0] != " ":
		NODES.append(line[0:len(line)-1])
	
Ref.close()

Nodes_exclude = NODES[0:8] + NODES[32:33] + NODES[34:36]+ NODES[len(NODES)-4:len(NODES)] 


print Nodes_exclude



for line in SDP:
	if (line[0] == "0" or line[0] == "1" or line[0] == "*" ) and line.find(", ") > -1:
		dpSS.append(line)
		if line[55:len(line)] not in P12_names: 
			P12_names.append(line[55:len(line)])

	elif (line[0] == "0" or line[0] == "1" or line[0] == "*" ) and line.find(", ") < 0:
		spSS.append(line)

	
SDP.close()


 
def Perturb_analysis (P, SSr, SSp, PT):
	#Function for counting the stable states with a given set of conditions
	Cr=0
	for i in SSr:
               	if i[49:51]== PT:
			Cr = Cr + 1
	Cp=0
	for i in SSp:
                if i.find(P) > -1:
                       	if i[49:51]== PT:
				Cp = Cp + 1
	if Cp > 0 and Cr == 0: 
		S = 1
	elif Cp == 0 and Cr > 0: 
		S = -1
	else:
		S=0 
 
  	return S





# function arguments sets
PT_set = [ "02", "12", "01", "11", "00", "10"]
P_set =[]



Output_file1 = open("Sensitivity_double.txt", "w") 
Output_file2 = open("Sensitivity_double_with_values.txt", "w") 



title= "Critical synergic and counteracting double perturbations that leads to loss and gains of adhesion phenotypes \n"


Output_file1.write(title)		
Output_file2.write(title)		




# List for perturbations with synergic/combinatorial effects on phenotype gains and loss 

H1_gain=[]

H2_gain=[]

E1_loss=[]
E2_loss=[]
M_loss=[]





EXCLUSION= ""
for i in Nodes_exclude:
	EXCLUSION = EXCLUSION + i + " "


Cont=0
for Pij in P12_names:
	DP= Pij.split(",")
	Pi = DP[0]
	Pj = DP[1][1:len(DP[1])]
	N1 =Pi[0:len(Pi)-3]
	N2 =Pj[0:len(Pj)-3]
	Cont=Cont+1
	if EXCLUSION.find(N1) < 0  and EXCLUSION.find(N2) < 0:
		print Pi , "+", Pj, " = ", Pij, "\t perturbation n=", Cont  
		P12=" " + Pij		
		p12E1 = Perturb_analysis (P12, SSref, dpSS, "02")
		p12E2 = Perturb_analysis (P12, SSref, dpSS, "01")
		p12H1 = Perturb_analysis (P12, SSref, dpSS, "12")
		p12H2 = Perturb_analysis (P12, SSref, dpSS, "11")
		p12M = Perturb_analysis (P12, SSref, dpSS, "10") 


		P1=" " + Pi
		P2 = " " + Pj
		p1E1 = Perturb_analysis (P1, SSref, spSS, "02")
		p1E2 = Perturb_analysis (P1, SSref, dpSS, "01")
		p1H1 = Perturb_analysis (P1, SSref, spSS, "12")
		p1H2 = Perturb_analysis (P1, SSref, spSS, "11")
		p1M = Perturb_analysis (P1, SSref, spSS, "10")
		
		p2E1 = Perturb_analysis (P2, SSref, spSS, "02")
		p2E2 = Perturb_analysis (P2, SSref, dpSS, "01")
		p2H1 = Perturb_analysis (P2, SSref, spSS, "12")
		p2H2 = Perturb_analysis (P2, SSref, spSS, "11")
		p2M = Perturb_analysis (P2, SSref, spSS, "10")


		if p12E1 == -1 and p1E1 != -1 and p2E1 !=-1:
			K=(P12, p12E1, p1E1, p2E1)
			E1_loss.append(K)
			print K, "Synergic effect on E1(02) loss!"

		if p12E2 == -1 and p1E2 != -1 and p2E2 !=-1:
			K=(P12, p12E2, p1E2, p2E2)
			E2_loss.append(K)
			print K, "Synergic effect on E2(01) loss!"

		if p12H1 == 1 and p1H1 != 1 and p2H1 !=1:
			K=(P12, p12H1, p1H1, p2H1)
			H1_gain.append(K)
			print K, "Synergic effect on H1(12) gain!"

		if p12H2 == 1 and p1H2 != 1 and p2H2 !=1:
			K=(P12, p12H1, p1H1, p2H1)
			H2_gain.append(K)
			print K, "Synergic effect on H2(11) gain!"

		if p12M == -1 and p1M != -1 and p2M !=-1:
			K=(P12, p12M, p1M, p2M)
			M_loss.append(K)
			print K, "Synergic effect on H2(11) gain!"





SET = [E1_loss , E1_loss , M_loss , H1_gain, H2_gain ]



L = ["synergic double Pertubations allowing epithelial (02) loss", 
	"synergic double Pertubations allowing epithelial (01) loss", 
	"synergic double Pertubations allowing mesenchymal (10) loss",
	"synergic double Pertubations allowing hybrid  (12) gain",
	"synergic double Pertubations allowing hybrid (11) gain" ]


n=-1
for i  in SET:
	n=n+1
	phenotype = L[n] + "\n"
	Output_file1.write("\n=================================================\n") 
	Output_file1.write(phenotype)
	Output_file2.write("\n=================================================\n") 
	Output_file2.write(phenotype)

	for SP in i:
		SynPer = SP[0][0:-1] + "\n"
                SynPerV= "Pi="+str(round(SP[2])) +"\t Pj =" +  str(round(SP[3])) + "\t Pij =" + str(round(SP[1])) + "--> " +SP[0][0:-1] + "\n" 
		Output_file1.write(SynPer)
		Output_file2.write(SynPerV)
	
	Output_file1.write("=================================================\n")
	Output_file2.write("=================================================\n")

Output_file1.close()
Output_file2.close()	
	



			

