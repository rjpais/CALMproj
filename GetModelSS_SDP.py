# This script generates single and double perturbations and retrives the computed stable states for all perturbations
# INSTRUCTIONS TO RUN
# Must have in current directory: a GINsim program; this script; and The model (in GINsim). 
# in command line type: java -jar GINsim-2.9.3-with-deps.jar -s perturbations.py cell_adhesion_model.zginml >> pertubations.txt




g = gs.open(gs.args[0])
perturbations = gs.associated(g, "mutant", True)


# add fixed perturbations for all levels of all components
print "==================================\n MODEL COMPONENTS"
for component in g.getNodeOrder():
	print component
	nodeInfo = component.getNodeInfo()
	for v in xrange(0, nodeInfo.max+1):
		perturbations.addFixedPerturbation(nodeInfo, v)

print g.getNodeOrder()


simple=[]
for p in perturbations:
	simple.append(p)


for i, p in enumerate(simple):
	for p2 in simple[i+1:]:
		s=p.toString()
		s2=p2.toString()
		if (s.split(' ')[0] != s2.split(' ')[0]):
			perturbations.addMultiplePerturbation( (p, p2))

print "==============================================\n PERTURBATIONS AND STABLE STATES"

# Get stable states for all perturbations
model = g.getModel()
ssrv = gs.service("stable")
for p in perturbations:
	print "=============================================="
	m = p.apply(model)
	stable=ssrv.getStableStateSearcher(m)
	stable.run()
	if (stable.getResult() != None):
		paths = stable.getPaths()
		values = paths.getPath()
		for l in paths:
			state = ""
			for v in values:
				if v < 0: state += "*"
				else: state += "%d" % v 
                        print state, "->", p           # I have changed this part!!! to print names after  states 




