#!/bin/bash

## Sources a secondary script which contains a list of parameters and a lists of values.
## This script then loops over each parameter and value, to run a config file,
## prints out the time to run over all events, and logs the run of each iteration.

source RunEverything.sh
source Parameters_two.sh $varnames

#the if statement allows the user to establish whether he wants to work with all the parameters or only with one of them
if [ $# -eq 0 ]; then
        for par in "${!parameters[@]}"; do                 # parameter loop
                for VAL in "${!parameters[$par]}"; do      # current parameter's values loop
                        LOG=log_${par}_${VAL}.txt          # initialize log for the current parameter and value 
                        PRU=changes_${par}.txt             # initialize register for current run time and value
                        echo $par $VAL
                        cmsRun PPD_RunIISummer20UL17SIM_0_cfg.py paramNames=$par paramValues=$VAL >& $LOG             # logs the cmsRun, parsing the current parameter and value
                        echo $VAL $(grep "Total loop" $LOG | tail -n 1 | rev | cut -d' ' -f1 | rev) | tee -a $PRU     # prints the current value and Total loop time of the cmsRun and save the results in a .txt file
                done
        done
else
        for VAL in "${!parameters[$varnames]}"; do         # current parameter's values loop
                LOG=log_${varnames}_${VAL}.txt             # initialize log for the current parameter and value
                PRU1=changes_${varnames}.txt               # initialize register for current run time and value
                echo $varnames $VAL
                cmsRun PPD_RunIISummer20UL17SIM_0_cfg.py paramNames=$varnames paramValues=$VAL >& $LOG               # logs the cmsRun, parsing the current parameter and value
                echo $VAL $(grep "Total loop" $LOG | tail -n 1 | rev | cut -d' ' -f1 | rev) | tee -a $PRU1           # prints the current value and Total loop time of the cmsRun and save the results in a .txt file
        done
fi
