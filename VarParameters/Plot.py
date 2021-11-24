import uproot                      # to open rootfiles
import matplotlib.pyplot as plt    # to plot

### This code will plot one histogram for each Branch in the rootfiles. 
### Each histogram will have all the values of a parameter.   


## open desired rootfile

with open('run1_rootfiles.txt') as f:
	rootfiles = f.readlines()
	for rootfile in rootfiles:
		#print("rootfile: ", rootfile)
		#print(" ")
		rootfile_name = rootfile.replace("/uscms_data/d3/snorberg/Geant_Test/CMSSW_11_0_0/src/","").replace("/","_").replace(".root","")
		print(rootfile_name)
		param_val = rootfile_name.strip("run1_sim_").replace('\n','')
		#print(param_val)
		file = uproot.open(str(rootfile).replace('\n',''))
		#print("Trees: ", file.keys())
		print(" ")
## access the TTree
		#Tree = file["T"]
		Tree = file["ECAL_HCAL_Geant_Check"]
		#print("Branches: ", Tree.keys())
		#print(" ")
## access the TBranches and make each an array
# make a list out of the Tree keys (Branches)
		Branches = list(Tree.keys()) 
		for branch in Branches:
			branch_name = branch
			print(branch_name)
			branch_vals = Tree[str(branch)].array()
			continue

	# plot
		bins = 300
		plt.hist(branch_vals, histtype='step', bins=bins)
		plt.title(branch_name)
		plt.xlabel(branch_name)
		plt.ylabel("Events")
		plt.yscale("log")
		plt.legend([param_val])  # how to make it fill automatically?
		#plt.show()
		plt.savefig(param_val+"_"+branch_name+".png")
		#print(param_val+"_"+branch_name+".png")
