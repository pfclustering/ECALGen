# Script to launch several MC productions - at reco level
# parameters will be:
#  - number of events
#  - parameters to change in the ECAL clustering

# python Evreco_submit.py

import sys
print(sys.version)
import os
import time
import math
import itertools
import subprocess

inputDir = "EcalGen/GEN_SIM_DIGI/doubleElectron/Run3Cond/102X_upgrade2018_realistic_EcalAging_mid2023_400fb_v1/"
productionDir = "EcalGen/PROD_SeedingGathering_v9/"
logsDir = "PROD_SeedingGathering_v9"

params = {}
params["nevts"] =     [50000]
params["gathering"] = [10.0, 5.0, 1.0, 2.0, 0.5] # multiplier
params["seeding"] =   [10.0, 5.0, 1.0, 2.0, 0.5] # multiplier

# Default thresholds for the moment not used
thrs={}
thrs['EB']={}
thrs['EB']['seed']= 0.23 # 230 MeV
thrs['EB']['gather'] = 0.08 # 80 MeV

thrs['EEP']={}
thrs['EEP']['seed']=0.60 # 600 MeV
thrs['EEP']['gather']=0.30 # 300 MeV

thrs['EEM']=thrs['EEP']

##### Create output dir and logsdir
prefix='/pnfs/psi.ch/cms/trivcat/store/user/mratti/'
print 'Going to create output directory ', prefix + productionDir
command = 'xrdfs t3dcachedb03.psi.ch mkdir {p}'.format(p=prefix + productionDir)
if not os.path.isdir(prefix + productionDir):
  subprocess.check_output(command, shell=True)
else: raise RuntimeError('productionDir already present please check')

command = 'mkdir -p {l}'.format(l=logsDir)
if not os.path.isdir(logsDir):
  subprocess.check_output(command, shell=True)
else: raise RuntimeError('logsDir already present please check')

##### Submission
parameters_set = list(itertools.product(params["nevts"],params["gathering"],params["seeding"] ))
for iset in parameters_set:
  inevts = iset[0]
  igathering = iset[1]
  iseeding = iset[2]

  command = "qsub -o {l} -e {l} ecalReco_template.sh {p} {i} {n} {s} {g}".format(p=productionDir, i=inputDir, l=logsDir, n=inevts, s=iseeding, g=igathering)
  print command
  print "Going to submit ecalGen_template.sh for production={p} inDir={i} logsDir={l} nevts={n} seeding={s} gathering={g}".format(p=productionDir, i=inputDir, l=logsDir, n=inevts, s=iseeding, g=igathering)
  os.system(command)
