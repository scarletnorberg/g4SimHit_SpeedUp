cmsrel CMSSW_11_0_0
cd CMSSW_11_0_0/src
cmsenv
git-cms-addpkg SimG4Core #not needed any more
git clone git@github.com:scarletnorberg/g4SimHit_SpeedUp.git
scram b
source Script_RunGeantSettings.sh
root://cmsxrootd.fnal.gov//store/user/snorberg/GEANT/PPD-RunIISummer20UL17GEN-00001.root
