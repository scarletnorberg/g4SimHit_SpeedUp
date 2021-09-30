### imports ###
import os       # to use operating-system-dependent functionalities
import re       # to use regular expressions matching operations

### Values ###

#ProductionCuts = [0.5, 1.0, 2.0, 5.0, 10.0, 12.0, 14.0, 18.0, 20.0]
#Mag_vals = [0.01, 0.015, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35]
RusRo_vals = [0.1, 0.01]
Energy_vals = [200, 250]

### Parameters dictionary ###

parameters = dict()  # initialization the dictionary

## adding key-value pairs 
parameters['RusRoGammaEnergyLimit']=Energy_vals
parameters['RusRoElectronEnergyLimit']=Energy_vals

parameters['RusRoEcalGamma']=RusRo_vals
parameters['RusRoEcalNeutron']=RusRo_vals


### loop ###
for PARAM, VALUES in parameters.items():       # loops key-value pairs 
	for VAL in VALUES:		       # loops the values 
		print(PARAM,VAL)               # prints the current parameter and value in the loop
		

		INPUT = str('paramNames=%s paramValues=%s'%(PARAM,VAL))
                LOG = "log_"+PARAM+"_"+str(VAL)
		os.system("cmsRun PPD_RunIISummer20UL17SIM_0_cfg.py "+INPUT+" >& "+LOG+".txt")                                 # cmsRun of config into LOG
		#os.system("python PPD_RunIISummer20UL17SIM_0_cfg.py "+INPUT+" >& log_"+PARAM+"_"+str(VAL)+".txt dump=1")      # config dump into LOG
		
		## run-time print

		log = open("log_"+PARAM+"_"+str(VAL)+".txt","r")   # open to read the log file
		run_time = "Total loop"                            # string to search in th elog

		for line in log:                         # loop through the all the lines in the log
			if re.search(run_time, line):    
				print(line)              # print the line in the log that contains the specified string
