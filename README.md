# ECALGen
Bunch of scripts to generate various ecal conditions

### Installation

Use CMSSW_10_0_3 for Run 2 clustering studies
Use CMSSW_10_2_5 for Run 3 clustering studies

Use CMSSW_10_4_0_pre2 for test for UL of 2017
Use CMSSW_9_4_0_patch1 for test of Fall17 of 2017
```
cmsrel CMSSW_10_2_5
cd CMSSW_10_2_5/src/
cmsenv
git cms-addpkg RecoParticleFlow/Configuration
git cms-addpkg Configuration/Generator 
git clone git@github.com:mgratti/ECALGen.git
cp ECALGen/cmssw_changed_files/RecoParticleFlow_EventContent_cff.py RecoParticleFlow/Configuration/python/RecoParticleFlow_EventContent_cff.py
cp ECALGen/cmssw_changed_files/DoublePhoton.py Configuration/Generator/python/DoublePhoton.py
cp ECALGen/cmssw_changed_files/DoubleElectron.py Configuration/Generator/python/DoubleElectron.py
scram b -j8
```

### Workflow for development:
Everytime you log in, remember to pull from central such that Run2 and Run3 things are in sync

```
git pull --rebase
```

Do your modifications, 
```
git add <file1>
git add <file2>
git commit -m "comment"
git push
```
