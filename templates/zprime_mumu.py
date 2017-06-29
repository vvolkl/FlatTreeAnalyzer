import ROOT
import collections

### variable list
variables = {
    "ptzp":{"name":"zprime_muon_pt","title":"p_{T}^{Zprime} [GeV]","bin":200,"xmin":0,"xmax":20000},
    "mzp":{"name":"zprime_muon_m","title":"m_{Zprime} [GeV]","bin":500,"xmin":0,"xmax":50000},
    "ptmu_1":{"name":"lep1_pt","title":"p_{T}^{#mu, max} [GeV]","bin":200,"xmin":0,"xmax":20000},
    "ptmu_2":{"name":"lep2_pt","title":"p_{T}^{#mu, min} [GeV]","bin":200,"xmin":0,"xmax":20000},
    "met":{"name":"met_pt","title":"E_{T}^{miss}","bin":50,"xmin":0,"xmax":100},
}


colors = {}
colors['m_{Z} = 5 TeV'] = ROOT.kRed
colors['m_{Z} = 10 TeV'] = ROOT.kRed
colors['m_{Z} = 15 TeV'] = ROOT.kRed
colors['m_{Z} = 20 TeV'] = ROOT.kRed
colors['m_{Z} = 25 TeV'] = ROOT.kRed
colors['m_{Z} = 30 TeV'] = ROOT.kRed
colors['m_{Z} = 35 TeV'] = ROOT.kRed
colors['m_{Z} = 40 TeV'] = ROOT.kRed
colors['Drell-Yann'] = ROOT.kGreen+2

signal_groups = collections.OrderedDict()
signal_groups['m_{Z} = 5 TeV'] = ['pp_Zprime_5TeV_ll']
signal_groups['m_{Z} = 10 TeV'] = ['pp_Zprime_10TeV_ll']
signal_groups['m_{Z} = 15 TeV'] = ['pp_Zprime_15TeV_ll']
signal_groups['m_{Z} = 20 TeV'] = ['pp_Zprime_20TeV_ll']
signal_groups['m_{Z} = 25 TeV'] = ['pp_Zprime_25TeV_ll']
signal_groups['m_{Z} = 30 TeV'] = ['pp_Zprime_30TeV_ll']
signal_groups['m_{Z} = 35 TeV'] = ['pp_Zprime_35TeV_ll']
signal_groups['m_{Z} = 40 TeV'] = ['pp_Zprime_40TeV_ll']

background_groups = collections.OrderedDict()
background_groups['Drell-Yann'] = ['pp_ll012j_5f_HT_0_200', 'pp_ll012j_5f_HT_200_700','pp_ll012j_5f_HT_700_1500','pp_ll012j_5f_HT_1500_2700',
                'pp_ll012j_5f_HT_2700_4200','pp_ll012j_5f_HT_4200_8000', 'pp_ll012j_5f_HT_8000_15000', 'pp_ll012j_5f_HT_15000_25000', 
                'pp_ll012j_5f_HT_25000_35000', 'pp_ll012j_5f_HT_35000_100000']

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
selbase = 'lep1_pt > 200. && lep2_pt > 200. && abs(lep1_eta) < 4 && abs(lep2_eta) < 4 && zprime_muon_m>2000'

# add mass-dependent list of event selections here if needed...

selections = collections.OrderedDict()
selections['m_{Z} = 5 TeV'] = []
selections['m_{Z} = 5 TeV'].append(selbase)
selections['m_{Z} = 10 TeV'] = []
selections['m_{Z} = 10 TeV'].append(selbase)
selections['m_{Z} = 15 TeV'] = []
selections['m_{Z} = 15 TeV'].append(selbase)
selections['m_{Z} = 20 TeV'] = []
selections['m_{Z} = 20 TeV'].append(selbase)
selections['m_{Z} = 25 TeV'] = []
selections['m_{Z} = 25 TeV'].append(selbase)
selections['m_{Z} = 30 TeV'] = []
selections['m_{Z} = 30 TeV'].append(selbase)
selections['m_{Z} = 35 TeV'] = []
selections['m_{Z} = 35 TeV'].append(selbase)
selections['m_{Z} = 40 TeV'] = []
selections['m_{Z} = 40 TeV'].append(selbase)
