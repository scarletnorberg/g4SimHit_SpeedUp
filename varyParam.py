import FWCore.ParameterSet.Config as cms
import sys
from PPD_RunIISummer20UL17SIM_0_cfg import process

process.g4SimHits.MagneticField.ConfGlobalMFM.OCMS.StepperParam.EnergyThSimple = cms.double(float(sys.argv[2]))
