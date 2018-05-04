import ROOT
import collections

### variable list
variables = {
    "ptzp":{"name":"zprime_ele_pt","title":"p_{T}^{Z'} [GeV]","bin":200,"xmin":0,"xmax":6000},
    "mzp":{"name":"zprime_ele_m","title":"m_{Z'} [TeV]","bin":200,"xmin":0,"xmax":16, "divide":1000},
    "ptel_1":{"name":"lep1_pt","title":"p_{T}^{e, max} [TeV]","bin":100,"xmin":0,"xmax":16, "divide":1000},
    "ptel_2":{"name":"lep2_pt","title":"p_{T}^{e, min} [TeV]","bin":100,"xmin":0,"xmax":16, "divide":1000},
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
signal_groups['m_{Z} = 2 TeV']  = ['p8_pp_ZprimeSSM_2TeV_ll']
signal_groups['m_{Z} = 4 TeV']  = ['p8_pp_ZprimeSSM_4TeV_ll']
signal_groups['m_{Z} = 6 TeV']  = ['p8_pp_ZprimeSSM_6TeV_ll']
signal_groups['m_{Z} = 8 TeV']  = ['p8_pp_ZprimeSSM_8TeV_ll']
signal_groups['m_{Z} = 10 TeV'] = ['p8_pp_ZprimeSSM_10TeV_ll']
signal_groups['m_{Z} = 12 TeV'] = ['p8_pp_ZprimeSSM_12TeV_ll']
signal_groups['m_{Z} = 14 TeV'] = ['p8_pp_ZprimeSSM_14TeV_ll']

background_groups = collections.OrderedDict()
background_groups['Drell-Yan'] = ['mgp8_pp_ee_5f_HT_500_1000','mgp8_pp_ee_5f_HT_1000_2000','mgp8_pp_ee_5f_HT_2000_5000','mgp8_pp_ee_5f_HT_5000_10000','mgp8_pp_ee_5f_HT_10000_27000']

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
selbase = 'lep1_pt > 500. && lep2_pt > 500. && abs(lep1_eta) < 4 && abs(lep2_eta) < 4 && zprime_ele_m>1000'

# add mass-dependent list of event selections here if needed...

selections = collections.OrderedDict()
selections['m_{Z} = 2 TeV' ] = []
selections['m_{Z} = 2 TeV' ].append(selbase)
selections['m_{Z} = 4 TeV' ] = []
selections['m_{Z} = 4 TeV' ].append(selbase)
selections['m_{Z} = 6 TeV' ] = []
selections['m_{Z} = 6 TeV' ].append(selbase)
selections['m_{Z} = 8 TeV' ] = []
selections['m_{Z} = 8 TeV' ].append(selbase)
selections['m_{Z} = 10 TeV'] = []
selections['m_{Z} = 10 TeV'].append(selbase)
selections['m_{Z} = 12 TeV'] = []
selections['m_{Z} = 12 TeV'].append(selbase)
selections['m_{Z} = 14 TeV'] = []
selections['m_{Z} = 14 TeV'].append(selbase)
