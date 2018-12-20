import ROOT
import collections

ana_tex = "Z\' #rightarrow #mu^{+}#mu^{-} (1710.06363)"

### variable list
variables = {
    "ptzp":{"name":"zprime_muon_pt","title":"p_{T}^{Z'} [GeV]","bin":200,"xmin":0,"xmax":6000},
    "mzp":{"name":"zprime_muon_m","title":"m_{Z'} [TeV]","bin":200,"xmin":0,"xmax":20, "divide":1000},
    "ptmu_1":{"name":"lep1_pt","title":"p_{T}^{#mu, max} [TeV]","bin":100,"xmin":0,"xmax":10, "divide":1000},
    "ptmu_2":{"name":"lep2_pt","title":"p_{T}^{#mu, min} [TeV]","bin":100,"xmin":0,"xmax":10, "divide":1000},
}

variables2D = {}


colors = {}
colors['m_{Z} = 2 TeV']  = ROOT.kRed
colors['m_{Z} = 4 TeV']  = ROOT.kRed
colors['m_{Z} = 6 TeV']  = ROOT.kRed
colors['m_{Z} = 8 TeV']  = ROOT.kRed
colors['m_{Z} = 10 TeV'] = ROOT.kRed
colors['m_{Z} = 12 TeV'] = ROOT.kRed
colors['m_{Z} = 14 TeV'] = ROOT.kRed
colors['Drell-Yan'] = ROOT.kGreen+2

signal_groups = collections.OrderedDict()
signal_groups['m_{Z} = 2 TeV']  = ['mgp8_pp_Zprime_mumu_5f_Mzp_2TeV' ]
signal_groups['m_{Z} = 4 TeV']  = ['mgp8_pp_Zprime_mumu_5f_Mzp_4TeV' ]
signal_groups['m_{Z} = 6 TeV']  = ['mgp8_pp_Zprime_mumu_5f_Mzp_6TeV' ]
signal_groups['m_{Z} = 8 TeV']  = ['mgp8_pp_Zprime_mumu_5f_Mzp_8TeV' ]
signal_groups['m_{Z} = 10 TeV'] = ['mgp8_pp_Zprime_mumu_5f_Mzp_10TeV']
signal_groups['m_{Z} = 12 TeV'] = ['mgp8_pp_Zprime_mumu_5f_Mzp_12TeV']
signal_groups['m_{Z} = 14 TeV'] = ['mgp8_pp_Zprime_mumu_5f_Mzp_14TeV']

background_groups = collections.OrderedDict()
background_groups['Drell-Yan'] = ['mgp8_pp_mumu_5f_HT_500_1000','mgp8_pp_mumu_5f_HT_1000_2000','mgp8_pp_mumu_5f_HT_2000_5000','mgp8_pp_mumu_5f_HT_5000_10000','mgp8_pp_mumu_5f_HT_10000_27000']

# global parameters
intLumi = 1.5e+07
delphesVersion = '3.4.2'

uncertainties = []
uncertainties.append([0., 0.])
uncertainties.append([0.02, 0.0])
uncertainties.append([0.02, 0.02])
uncertainties.append([0.02, 0.10])

# the first time needs to be set to True
runFull = True
HELHC=True

# base pre-selections
selbase = 'lep1_pt > 750. && lep2_pt > 750. && abs(lep1_eta) < 4 && abs(lep2_eta) < 4 && zprime_muon_m > 1500.'

# add mass-dependent list of event selections here if needed...

selections = collections.OrderedDict()
selections['m_{Z} = 2 TeV'] = []
selections['m_{Z} = 2 TeV'].append(selbase)
selections['m_{Z} = 4 TeV'] = []
selections['m_{Z} = 4 TeV'].append(selbase)
selections['m_{Z} = 6 TeV'] = []
selections['m_{Z} = 6 TeV'].append(selbase)
selections['m_{Z} = 8 TeV'] = []
selections['m_{Z} = 8 TeV'].append(selbase)
selections['m_{Z} = 10 TeV'] = []
selections['m_{Z} = 10 TeV'].append(selbase)
selections['m_{Z} = 12 TeV'] = []
selections['m_{Z} = 12 TeV'].append(selbase)
selections['m_{Z} = 14 TeV'] = []
selections['m_{Z} = 14 TeV'].append(selbase)
