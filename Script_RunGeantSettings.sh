#!/bin/bash

for VAL in 0.015 0.05 0.1 0.15 0.2 0.25 0.3 0.35 0.4 0.45 0.5; do
	LOG=log_${VAL/0./}.txt
	cmsRun varyParam.py $VAL >& $LOG
	echo $VAL $(grep "Total loop" $LOG | tail -n 1 | rev | cut -d' ' -f1 | rev)
done
