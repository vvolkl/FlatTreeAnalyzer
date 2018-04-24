import ROOT
import collections

### variable list
variables = {
    "ptzp":{"name":"zprime_muon_pt","title":"p_{T}^{Z'} [GeV]","bin":200,"xmin":0,"xmax":20000},
    "mzp":{"name":"zprime_muon_m","title":"m_{Z'} [TeV]","bin":200,"xmin":10,"xmax":50, "divide":1000},
    "ptmu_1":{"name":"lep1_pt","title":"p_{T}^{#mu, max} [TeV]","bin":100,"xmin":5,"xmax":20, "divide":1000},
    "ptmu_2":{"name":"lep2_pt","title":"p_{T}^{#mu, min} [TeV]","bin":100,"xmin":5,"xmax":20, "divide":1000},
}

variables2D = {}


colors = {}
colors['m_{Z} = 15 TeV'] = ROOT.kRed
colors['m_{Z} = 20 TeV'] = ROOT.kRed
colors['m_{Z} = 25 TeV'] = ROOT.kRed
colors['m_{Z} = 30 TeV'] = ROOT.kRed
colors['m_{Z} = 35 TeV'] = ROOT.kRed
colors['m_{Z} = 40 TeV'] = ROOT.kRed
colors['m_{Z} = 45 TeV'] = ROOT.kRed
colors['m_{Z} = 50 TeV'] = ROOT.kRed
colors['Drell-Yann'] = ROOT.kGreen+2

signal_groups = collections.OrderedDict()
signal_groups['m_{Z} = 15 TeV'] = ['p8_pp_Zprime_15TeV_ll']
signal_groups['m_{Z} = 20 TeV'] = ['p8_pp_Zprime_20TeV_ll']
signal_groups['m_{Z} = 25 TeV'] = ['p8_pp_Zprime_25TeV_ll']
signal_groups['m_{Z} = 30 TeV'] = ['p8_pp_Zprime_30TeV_ll']
signal_groups['m_{Z} = 35 TeV'] = ['p8_pp_Zprime_35TeV_ll']
signal_groups['m_{Z} = 40 TeV'] = ['p8_pp_Zprime_40TeV_ll']
signal_groups['m_{Z} = 45 TeV'] = ['p8_pp_Zprime_45TeV_ll']
signal_groups['m_{Z} = 50 TeV'] = ['p8_pp_Zprime_50TeV_ll']

background_groups = collections.OrderedDict()
background_groups['Drell-Yann'] = ['mgp8_pp_mumu_lo']

# global parameters
intLumi = 3.0e+07
delphesVersion = '3.4.2'

uncertainties = []
uncertainties.append([0., 0.])
uncertainties.append([0.02, 0.0])
uncertainties.append([0.02, 0.02])
uncertainties.append([0.02, 0.10])

# the first time needs to be set to True
runFull = True

# base pre-selections
selbase = 'lep1_pt > 6000. && lep2_pt > 6000. && abs(lep1_eta) < 4 && abs(lep2_eta) < 4 && zprime_muon_m>12000'

# add mass-dependent list of event selections here if needed...

selections = collections.OrderedDict()
#selections['m_{Z} = 15 TeV'] = []
#selections['m_{Z} = 15 TeV'].append(selbase)
#selections['m_{Z} = 20 TeV'] = []
#selections['m_{Z} = 20 TeV'].append(selbase)
#selections['m_{Z} = 25 TeV'] = []
#selections['m_{Z} = 25 TeV'].append(selbase)
selections['m_{Z} = 30 TeV'] = []
selections['m_{Z} = 30 TeV'].append(selbase)
#selections['m_{Z} = 35 TeV'] = []
#selections['m_{Z} = 35 TeV'].append(selbase)
selections['m_{Z} = 40 TeV'] = []
selections['m_{Z} = 40 TeV'].append(selbase)
#selections['m_{Z} = 45 TeV'] = []
#selections['m_{Z} = 45 TeV'].append(selbase)
#selections['m_{Z} = 50 TeV'] = []
#selections['m_{Z} = 50 TeV'].append(selbase)

