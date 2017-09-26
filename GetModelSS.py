

# This script gets all model stable states

g = gs.open(gs.args[0])

print "==================================================================== \n   MODEL COMPONENTS"
# PRINT MODEL COMPONENTS
for component in g.getNodeOrder():
	print component
	nodeInfo = component.getNodeInfo()

print "==================================================================== \n   Wild-type stable states: " 
print "====================================================================" 
# Get stable states 
model = g.getModel()
ssrv = gs.service("stable")
stable=ssrv.getStableStateSearcher(model)
stable.run()

# model states states
if (stable.getResult() != None):
	paths = stable.getPaths()
	values = paths.getPath()
	for lines in paths:
		state = ""
		for value in values:
			if value < 0: 
				state += "*"
			else: 
				state += "%d" % value
		print state


