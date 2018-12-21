import ROOT
import collections

ana_tex = "Z\' #rightarrow #mu^{+}#mu^{-} (1710.06363)"

### variable list
variables = {
#    "ptzp":{"name":"zprime_muon_pt","title":"p_{T}^{Z'} [GeV]","bin":200,"xmin":0,"xmax":20000},
    "mzp":{"name":"zprime_muon_m","title":"m_{Z'} [TeV]","bin":200,"xmin":0,"xmax":50, "divide":1000},
#    "ptmu_1":{"name":"lep1_pt","title":"p_{T}^{#mu, max} [TeV]","bin":100,"xmin":0,"xmax":20, "divide":1000},
#    "ptmu_2":{"name":"lep2_pt","title":"p_{T}^{#mu, min} [TeV]","bin":100,"xmin":0,"xmax":20, "divide":1000},
}

variables2D = {}


colors = {}
colors['m_{Z} = 4 TeV']  = ROOT.kRed
colors['m_{Z} = 6 TeV']  = ROOT.kRed
colors['m_{Z} = 8 TeV']  = ROOT.kRed
colors['m_{Z} = 10 TeV'] = ROOT.kRed
colors['m_{Z} = 12 TeV'] = ROOT.kRed
colors['m_{Z} = 14 TeV'] = ROOT.kRed
colors['m_{Z} = 15 TeV'] = ROOT.kRed
colors['m_{Z} = 16 TeV'] = ROOT.kRed
colors['m_{Z} = 18 TeV'] = ROOT.kRed
colors['m_{Z} = 20 TeV'] = ROOT.kRed
colors['m_{Z} = 25 TeV'] = ROOT.kRed
colors['m_{Z} = 30 TeV'] = ROOT.kRed
colors['m_{Z} = 35 TeV'] = ROOT.kRed
colors['m_{Z} = 40 TeV'] = ROOT.kRed
colors['m_{Z} = 45 TeV'] = ROOT.kRed
colors['Drell-Yan'] = ROOT.kGreen+2

signal_groups = collections.OrderedDict()
signal_groups['m_{Z} = 4 TeV']  = ['mgp8_pp_Zprime_mumu_5f_Mzp_4TeV' ]
signal_groups['m_{Z} = 6 TeV']  = ['mgp8_pp_Zprime_mumu_5f_Mzp_6TeV' ]
signal_groups['m_{Z} = 8 TeV']  = ['mgp8_pp_Zprime_mumu_5f_Mzp_8TeV' ]
signal_groups['m_{Z} = 10 TeV'] = ['mgp8_pp_Zprime_mumu_5f_Mzp_10TeV']
signal_groups['m_{Z} = 12 TeV'] = ['mgp8_pp_Zprime_mumu_5f_Mzp_12TeV']
signal_groups['m_{Z} = 14 TeV'] = ['mgp8_pp_Zprime_mumu_5f_Mzp_14TeV']
signal_groups['m_{Z} = 15 TeV'] = ['mgp8_pp_Zprime_mumu_5f_Mzp_15TeV']
signal_groups['m_{Z} = 16 TeV'] = ['mgp8_pp_Zprime_mumu_5f_Mzp_16TeV']
signal_groups['m_{Z} = 18 TeV'] = ['mgp8_pp_Zprime_mumu_5f_Mzp_18TeV']
signal_groups['m_{Z} = 20 TeV'] = ['mgp8_pp_Zprime_mumu_5f_Mzp_20TeV']
signal_groups['m_{Z} = 25 TeV'] = ['mgp8_pp_Zprime_mumu_5f_Mzp_25TeV']
signal_groups['m_{Z} = 30 TeV'] = ['mgp8_pp_Zprime_mumu_5f_Mzp_30TeV']
signal_groups['m_{Z} = 35 TeV'] = ['mgp8_pp_Zprime_mumu_5f_Mzp_35TeV']
signal_groups['m_{Z} = 40 TeV'] = ['mgp8_pp_Zprime_mumu_5f_Mzp_40TeV']
signal_groups['m_{Z} = 45 TeV'] = ['mgp8_pp_Zprime_mumu_5f_Mzp_45TeV']

background_groups = collections.OrderedDict()
background_groups['Drell-Yan'] = ['mgp8_pp_mumu_5f_HT_500_1000','mgp8_pp_mumu_5f_HT_1000_2000','mgp8_pp_mumu_5f_HT_2000_5000','mgp8_pp_mumu_5f_HT_5000_10000','mgp8_pp_mumu_5f_HT_10000_27000','mgp8_pp_mumu_5f_HT_27000_100000']

# global parameters
intLumi = 3.0e+07
delphesVersion = '3.4.2'

uncertainties = []
uncertainties.append([0., 0.])
uncertainties.append([0.02, 0.0])
uncertainties.append([0.02, 0.02])
uncertainties.append([0.02, 0.10])

# the first time needs to be set to True
runFull = False

# base pre-selections
selbase = 'lep1_pt > 1200. && lep2_pt > 1200. && abs(lep1_eta) < 4 && abs(lep2_eta) < 4 && zprime_muon_m > 2500.'

# add mass-dependent list of event selections here if needed...

selections = collections.OrderedDict()
#selections['m_{Z} = 4 TeV'] = []
#selections['m_{Z} = 4 TeV'].append(selbase)
#selections['m_{Z} = 6 TeV'] = []
#selections['m_{Z} = 6 TeV'].append(selbase)
#selections['m_{Z} = 8 TeV'] = []
#selections['m_{Z} = 8 TeV'].append(selbase)
#selections['m_{Z} = 10 TeV'] = []
#selections['m_{Z} = 10 TeV'].append(selbase)
#selections['m_{Z} = 12 TeV'] = []
#selections['m_{Z} = 12 TeV'].append(selbase)
#selections['m_{Z} = 14 TeV'] = []
#selections['m_{Z} = 14 TeV'].append(selbase)
#selections['m_{Z} = 15 TeV'] = []
#selections['m_{Z} = 15 TeV'].append(selbase)
#selections['m_{Z} = 16 TeV'] = []
#selections['m_{Z} = 16 TeV'].append(selbase)
#selections['m_{Z} = 18 TeV'] = []
#selections['m_{Z} = 18 TeV'].append(selbase)
#selections['m_{Z} = 20 TeV'] = []
#selections['m_{Z} = 20 TeV'].append(selbase)
#selections['m_{Z} = 25 TeV'] = []
#selections['m_{Z} = 25 TeV'].append(selbase)
selections['m_{Z} = 30 TeV'] = []
selections['m_{Z} = 30 TeV'].append(selbase)
#selections['m_{Z} = 35 TeV'] = []
#selections['m_{Z} = 35 TeV'].append(selbase)
#selections['m_{Z} = 40 TeV'] = []
#selections['m_{Z} = 40 TeV'].append(selbase)
#selections['m_{Z} = 45 TeV'] = []
#selections['m_{Z} = 45 TeV'].append(selbase)
