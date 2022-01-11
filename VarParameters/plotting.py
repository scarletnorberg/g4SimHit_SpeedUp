import uproot			# to access rootfiles
import matplotlib.pyplot as plt	# to plot the histograms
import re			# to match strings

## Branch dictionaries 
Dict_EcalHitsEBenergyEM = dict()
Dict_EcalHitsEBenergy = dict()
Dict_EcalHitsEBenergyHad = dict()
Dict_EcalHitsEEenergyEM = dict()
Dict_EcalHitsEEenergy = dict()
Dict_EcalHitsEEenergyHad = dict()
Dict_HcalHitsenergy = dict()
Dict_HcalHitsenergyEM = dict()
Dict_HcalHitsenergyHad = dict()

## Branch dictionaries list
Dict_list = [Dict_EcalHitsEBenergyEM, Dict_EcalHitsEBenergy, Dict_EcalHitsEBenergyHad, Dict_EcalHitsEEenergyEM, Dict_EcalHitsEEenergy, Dict_EcalHitsEEenergyHad, Dict_HcalHitsenergy, Dict_HcalHitsenergyEM, Dict_HcalHitsenergyHad]

## list for the parameters and their respective value (this will be used for plotting)
param_val_list = [] 

with open('run1_rootfiles.txt') as f:    # read desired text file with rootfiles' path; change when needed
	rootfiles = f.readlines()
	for rootfile in rootfiles:       # loops the rootfiles in .txt file
		rootfile = rootfile.replace('\n','')  # eliminates 'new line' 
		rootfile_name = rootfile.replace("/uscms_data/d3/snorberg/Geant_Test/CMSSW_11_0_0/src/","").replace("/","_").replace(".root","").replace('\n','')
		param_val = rootfile_name.replace("run1_sim_","").replace('\n','')
		param_val_list.append(param_val)

		print(rootfile)
		#print(param_val)
		print(" ")

		with uproot.open(rootfile) as file:
			#print(file.classnames())
			Tree = file["ECAL_HCAL_Geant_Check"]	# accessing the TTree
			#print(Tree.show())
			Branches = list(Tree.keys())		# accessing and listing the Tree's TBranches
			#print(" ")
			#print(Branches)

			for branch in Branches:
				branch = branch.decode('utf8').strip()			# decode the utf8 byte from the string
				param_val_branch = str(branch) + str("_") + param_val	# Branch's parameter_value (to be used as Dict key) 
				branch_vals = Tree[str(branch)].array()			# Branch's array-value (to be used as Dict value)	
				branch_pattern = re.compile(str(branch))		# set the Branch string as a pattern for matching

				#print(param_val_branch)
				#print(" ")
				#print(branch_pattern)
				#print(" ")
				
				## Match the branh_pattern to add the current Branch's parameter and value as key
				## and the Branch's array-value as value to the appropriate dictionary

				if re.fullmatch(branch_pattern, "EcalHitsEBenergyEM"):
					Dict_EcalHitsEBenergyEM[str(param_val_branch)] = branch_vals
					continue
				elif re.fullmatch(branch_pattern, "EcalHitsEBenergy"):
					Dict_EcalHitsEBenergy[str(param_val_branch)] = branch_vals
					continue 
				elif re.fullmatch(branch_pattern, "EcalHitsEBenergyHad"):
					Dict_EcalHitsEBenergyHad[str(param_val_branch)] = branch_vals
					continue
				elif re.fullmatch(branch_pattern, "EcalHitsEEenergyEM"):
					Dict_EcalHitsEEenergyEM[str(param_val_branch)] = branch_vals
					continue
				elif re.fullmatch(branch_pattern, "EcalHitsEEenergy"):
					Dict_EcalHitsEEenergy[str(param_val_branch)] = branch_vals
					continue
				elif re.fullmatch(branch_pattern, "EcalHitsEEenergyHad"):
					Dict_EcalHitsEEenergyHad[str(param_val_branch)] = branch_vals
					continue
				elif re.fullmatch(branch_pattern, "HcalHitsenergy"):
					Dict_HcalHitsenergy[str(param_val_branch)] = branch_vals
					continue
				elif re.fullmatch(branch_pattern, "HcalHitsenergyEM"):
					Dict_HcalHitsenergyEM[str(param_val_branch)] = branch_vals
					continue
				elif re.fullmatch(branch_pattern, "HcalHitsenergyHad"):
					Dict_HcalHitsenergyHad[str(param_val_branch)] = branch_vals
					continue
				else:
					continue


## Lists to add respective Branch's values from all the rootfiles
EcalHitsEBenergyEM_data = []
EcalHitsEBenergy_data = []
EcalHitsEBenergyHad_data = []
EcalHitsEEenergyEM_data = []
EcalHitsEEenergy_data = []
EcalHitsEEenergyHad_data = []
HcalHitsenergy_data = []
HcalHitsenergyEM_data = []
HcalHitsenergyHad_data = []


for D in Dict_list:	# loop Branches dictionaries list
	for b,v in D.items():	# goes through items of the current dictionary
		#print(b)
		#print(" ")
		#print(v)
		#print(" ")

		## remove the parameter and value from the string, and set the branch_name as pattern for matching
		branch_name = b.replace("RusRoMuonIronNeutron","").strip("__0.123456789")	# change the first string when needed
		pattern = re.compile(str(branch_name))
		
		if re.fullmatch(pattern, "EcalHitsEBenergyEM"):
			EcalHitsEBenergyEM_data.append(v)
			continue

		elif re.fullmatch(pattern, "EcalHitsEBenergy"):
			EcalHitsEBenergy_data.append(v)
			continue

		elif re.fullmatch(pattern, "EcalHitsEBenergyHad"):
			EcalHitsEBenergyHad_data.append(v)
			continue

		elif re.fullmatch(pattern, "EcalHitsEEenergyEM"):
			EcalHitsEEenergyEM_data.append(v)
			continue

		elif re.fullmatch(pattern, "EcalHitsEEenergy"):
			EcalHitsEEenergy_data.append(v)
			continue

		elif re.fullmatch(pattern, "EcalHitsEEenergyHad"):
			EcalHitsEEenergyHad_data.append(v)
			continue

		elif re.fullmatch(pattern, "HcalHitsenergy"):
			HcalHitsenergy_data.append(v)
			continue

		elif re.fullmatch(pattern, "HcalHitsenergyEM"):
			HcalHitsenergyEM_data.append(v)
			continue

		elif re.fullmatch(pattern, "HcalHitsenergyHad"):
			HcalHitsenergyHad_data.append(v)
			continue

		else:
			continue


bins = 100
print("plotting!")

## change plt.title() and plt.savefig() strings when needed

# 1
plt.hist(EcalHitsEBenergyEM_data, bins=bins, histtype='step', stacked=True, label=param_val_list)
plt.title("RusRoMuonIronNeutron_EcalHitsEBenergyEM")
plt.xlabel("EcalHitsEBenergyEM")
plt.ylabel("Events")
plt.yscale("log")
plt.legend(loc='upper right')
plt.savefig("RusRoMuonIronNeutron_EcalHitsEBenergyEM.png")
plt.close()

# 2
plt.hist(EcalHitsEBenergy_data, bins=bins, histtype='step', stacked=True, label=param_val_list)
plt.title("RusRoMuonIronNeutron_EcalHitsEBenergy")
plt.xlabel("EcalHitsEBenergy")
plt.ylabel("Events")
plt.yscale("log")
plt.legend(loc='upper right')
plt.savefig("RusRoMuonIronNeutron_EcalHitsEBenergy.png")
plt.close()

# 3
plt.hist(EcalHitsEBenergyHad_data, bins=bins, histtype='step', stacked=True, label=param_val_list)
plt.title("RusRoMuonIronNeutron_EcalHitsEBenergyHad")
plt.xlabel("EcalHitsEBenergyHad")
plt.ylabel("Events")
plt.yscale("log")
plt.legend(loc='upper right')
plt.savefig("RusRoMuonIronNeutron_EcalHitsEBenergyHad.png")
plt.close()

# 4
plt.hist(EcalHitsEEenergyEM_data, bins=bins, histtype='step', stacked=True, label=param_val_list)
plt.title("RusRoMuonIronNeutron_EcalHitsEEenergyEM")
plt.xlabel("EcalHitsEEenergyEM")
plt.ylabel("Events")
plt.yscale("log")
plt.legend(loc='upper right')
plt.savefig("RusRoMuonIronNeutron_EcalHitsEEenergyEM.png")
plt.close()

# 5
plt.hist(EcalHitsEEenergy_data, bins=bins, histtype='step', stacked=True, label=param_val_list)
plt.title("RusRoMuonIronNeutron_EcalHitsEEenergy")
plt.xlabel("EcalHitsEEenergy")
plt.ylabel("Events")
plt.yscale("log")
plt.legend(loc='upper right')
plt.savefig("RusRoMuonIronNeutron_EcalHitsEEenergy.png")
plt.close()

# 6
plt.hist(EcalHitsEEenergyHad_data, bins=bins, histtype='step', stacked=True, label=param_val_list)
plt.title("RusRoHcalMuonIronNeutron_EcalHitsEEenergyHad")
plt.xlabel("EcalHitsEEenergyHad")
plt.ylabel("Events")
plt.yscale("log")
plt.legend(loc='upper right')
plt.savefig("RusRoMuonIronNeutron_EcalHitsEEenergyHad.png")
plt.close()

# 7
plt.hist(HcalHitsenergy_data, bins=bins, histtype='step', stacked=True, label=param_val_list)
plt.title("RusRoMuonIronNeutron_HcalHitsenergy")
plt.xlabel("HcalHitsenergy")
plt.ylabel("Events")
plt.yscale("log")
plt.legend(loc='upper right')
plt.savefig("RusRoMuonIronNeutron_HcalHitsenergy.png")
plt.close()

# 8
plt.hist(HcalHitsenergyEM_data, bins=bins, histtype='step', stacked=True, label=param_val_list)
plt.title("RusRoMuonIronNeutron_HcalHitsenergyEM")
plt.xlabel("HcalHitsenergyEM")
plt.ylabel("Events")
plt.yscale("log")
plt.legend(loc='upper right')
plt.savefig("RusRoMuonIronNeutron_HcalHitsenergyEM.png")
plt.close()

# 9
plt.hist(HcalHitsenergyHad_data, bins=bins, histtype='step', stacked=True, label=param_val_list)
plt.title("RusRoMuonIronNeutron_HcalHitsenergyHad")
plt.xlabel("HcalHitsenergyHad")
plt.ylabel("Events")
plt.yscale("log")
plt.legend(loc='upper right')
plt.savefig("RusRoMuonIronNeutron_HcalHitsenergyHad.png")
plt.close()

print("The End!")

