import ROOT
import collections

### variable list
variables = {
    "ptzp":{"name":"zprime_muon_pt","title":"p_{T}^{Z'} [GeV]","bin":50,"xmin":0,"xmax":5000},
    "mzp":{"name":"zprime_muon_m","title":"m_{Z'} [TeV]","bin":100,"xmin":0,"xmax":20, "divide":1000},
    "ptmu_1":{"name":"lep1_pt","title":"p_{T}^{#mu, max} [TeV]","bin":50,"xmin":0,"xmax":10, "divide":1000},
    "ptmu_2":{"name":"lep2_pt","title":"p_{T}^{#mu, min} [TeV]","bin":50,"xmin":0,"xmax":10, "divide":1000},
    #"yzp":{"name":"zprime_y","title":"y_{Z'}","bin":80,"xmin":-4,"xmax":4},
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

colors['m_{Z ETA} = 6 TeV'] = ROOT.kRed
colors['m_{Z CHI} = 6 TeV'] = ROOT.kRed
colors['m_{Z PSI} = 6 TeV'] = ROOT.kRed
colors['m_{Z LRM} = 6 TeV'] = ROOT.kRed
colors['m_{Z I} = 6 TeV'] = ROOT.kRed


signal_groups = collections.OrderedDict()
signal_groups['m_{Z} = 2 TeV'] = ['p8_pp_ZprimeSSM_2TeV_ll']
signal_groups['m_{Z} = 4 TeV'] = ['p8_pp_ZprimeSSM_4TeV_ll']
signal_groups['m_{Z} = 6 TeV'] = ['p8_pp_ZprimeSSM_6TeV_ll']
signal_groups['m_{Z} = 8 TeV'] = ['p8_pp_ZprimeSSM_8TeV_ll']
signal_groups['m_{Z} = 10 TeV'] = ['p8_pp_ZprimeSSM_10TeV_ll']
signal_groups['m_{Z} = 12 TeV'] = ['p8_pp_ZprimeSSM_12TeV_ll']
signal_groups['m_{Z} = 14 TeV'] = ['p8_pp_ZprimeSSM_14TeV_ll']

signal_groups['m_{Z ETA} = 6 TeV'] = ['p8_pp_ZprimeETA_6TeV_ll']
signal_groups['m_{Z CHI} = 6 TeV'] = ['p8_pp_ZprimeCHI_6TeV_ll']
signal_groups['m_{Z PSI} = 6 TeV'] = ['p8_pp_ZprimePSI_6TeV_ll']
signal_groups['m_{Z LRM} = 6 TeV'] = ['p8_pp_ZprimeLRM_6TeV_ll']
signal_groups['m_{Z I} = 6 TeV'] = ['p8_pp_ZprimeI_6TeV_ll']

background_groups = collections.OrderedDict()
background_groups['Drell-Yan'] = ['mgp8_pp_mumu_5f_HT_500_1000',
                                  'mgp8_pp_mumu_5f_HT_1000_2000',
                                  'mgp8_pp_mumu_5f_HT_2000_5000',
                                  'mgp8_pp_mumu_5f_HT_5000_10000',
                                  'mgp8_pp_mumu_5f_HT_10000_27000']

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
selbase = 'lep1_pt > 500. && lep2_pt > 500. && abs(lep1_eta) < 4 && abs(lep2_eta) < 4 && zprime_muon_m>1000'

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

#selections['m_{Z ETA} = 6 TeV'] = []
#selections['m_{Z ETA} = 6 TeV'].append(selbase)
#selections['m_{Z CHI} = 6 TeV'] = []
#selections['m_{Z CHI} = 6 TeV'].append(selbase)
#selections['m_{Z PSI} = 6 TeV'] = []
#selections['m_{Z PSI} = 6 TeV'].append(selbase)
#selections['m_{Z LRM} = 6 TeV'] = []
#selections['m_{Z LRM} = 6 TeV'].append(selbase)
#selections['m_{Z I} = 6 TeV'] = []
#selections['m_{Z I} = 6 TeV'].append(selbase)
