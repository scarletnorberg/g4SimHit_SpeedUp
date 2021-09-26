### imports ###
#import FWCore.ParameterSet.Config as cms

#from Configuration.Eras.Era_Run2_2017_cff import Run2_2017
#from g4SimHit_SpeedUp.VarParameters.optGenSim import options

#import PPD_RunIISummer20UL17SIM_0_cfg.py

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
		
		## opening and writing the log without the with-statement
		#log = 'log_'+PARAM+'_'+str(VAL)+'.txt'
		#print(log)
		#print(" ")
		#LOG = open(log,'w')
		#LOG.write('testing')
		#LOG.close()

		## opening and writing the LOG with the with-statement
		with open('log_'+PARAM+'_'+str(VAL)+'.txt','w') as LOG:
			## writing into the LOG test
			#LOG.write('testing '+PARAM+' with value '+str(VAL))
			#LOG.close()
			
			LOG.write(str(execfile("PPD_RunIISummer20UL17SIM_0_cfg.py")))
			#LOG.write(run)
			LOG.close()


			#cmsRun PPD_RunIISummer20UL17SIM_0_cfg.py paramNames=PAR paramValues=VAL >& $LOG     # logs the cmsRun, parsing the current paramter and value
        		#run = execfile("python PPD_RunIISummer20UL17SIM_0_cfg.py paramNames="+PARAM+" paramValues="+str(VAL))   # running the config file ...
			# for-loop to write the output of running the config into the LOG file 
			#for output in execfile('PPD_RunIISummer20UL17SIM_0_cfg.py'):
				#LOG.write(output)
				#LOG.close()
				#print(VAL, grep("Total loop", LOG | tail -n 1 | rev | cut -d' ' -f1 | rev))
