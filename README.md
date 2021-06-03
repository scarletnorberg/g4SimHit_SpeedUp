# Setup

```bash
cmsrel CMSSW_11_0_0
cd CMSSW_11_0_0/src
cmsenv
git cms-init
git clone git@github.com:scarletnorberg/g4SimHit_SpeedUp.git
scram b
cd g4SimHit_SpeedUp
xrdcp root://cmseos.fnal.gov//store/user/snorberg/GEANT/PPD-RunIISummer20UL17GEN-00001.root .
./Script_RunGeantSettings.sh
```
