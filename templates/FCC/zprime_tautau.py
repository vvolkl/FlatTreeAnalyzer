import ROOT
import collections

### variable list
variables = {
    "met":{"name":"met_pt","title":"MET [GeV]","bin":50,"xmin":0,"xmax":1000},
    "mzp":{"name":"Mj1j2_pf04","title":"m_{Z'} [TeV]","bin":100,"xmin":2,"xmax":23, "divide":1000},
    "mr":{"name":"mr","title":"m_{Z'}^{razor} [TeV]","bin":100,"xmin":2,"xmax":23, "divide":1000},
    "mr2":{"name":"mr2","title":"m_{Z'}^{razor} [TeV]","bin":100,"xmin":2,"xmax":23, "divide":1000},
    "mr3":{"name":"mr3","title":"m_{Z'}^{razor} [TeV]","bin":100,"xmin":2,"xmax":23, "divide":1000},
    "mt":{"name":"mt","title":"m_{Z'}^{trans} [TeV]","bin":75,"xmin":0,"xmax":15, "divide":1000},
    "dr":{"name":"dr","title":"#DeltaR(#tau_{1},#tau_{2})","bin":50,"xmin":0,"xmax":5},
    "dphi":{"name":"dphi","title":"#DeltaPhi(#tau_{1},#tau_{2})","bin":50,"xmin":-4,"xmax":4},
    "dphi_met":{"name":"dphi_met","title":"#DeltaPhi(Z',met)","bin":50,"xmin":-4,"xmax":4},
    "pttau_1":{"name":"Jet1_pf04_pt","title":"p_{T}^{#tau, max} [TeV]","bin":50,"xmin":0.5,"xmax":10, "divide":1000},
    "pttau_2":{"name":"Jet2_pf04_pt","title":"p_{T}^{#tau, min} [TeV]","bin":50,"xmin":0.5,"xmax":10, "divide":1000},
    "etatau_1":{"name":"Jet1_pf04_eta","title":"#eta^{#tau, max}","bin":35,"xmin":-3.5,"xmax":3.5},
    "etatau_2":{"name":"Jet2_pf04_eta","title":"#eta^{#tau, min}","bin":35,"xmin":-3.5,"xmax":3.5},
}

variables2D = {}


colors = {}
colors['m_{Z} = 2 TeV'] = ROOT.kRed
colors['m_{Z} = 4 TeV'] = ROOT.kRed
colors['m_{Z} = 5 TeV'] = ROOT.kRed
colors['m_{Z} = 6 TeV'] = ROOT.kRed
colors['m_{Z} = 8 TeV'] = ROOT.kRed
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
colors['Drell-Yan'] = ROOT.kGreen+2
colors['QCD'] = ROOT.kBlue+1

signal_groups = collections.OrderedDict()
signal_groups['m_{Z} = 2 TeV'] = ['p8_pp_Zprime_2TeV_ll']
signal_groups['m_{Z} = 4 TeV'] = ['p8_pp_Zprime_4TeV_ll']
signal_groups['m_{Z} = 5 TeV'] = ['p8_pp_Zprime_5TeV_ll']
signal_groups['m_{Z} = 6 TeV'] = ['p8_pp_Zprime_6TeV_ll']
signal_groups['m_{Z} = 8 TeV'] = ['p8_pp_Zprime_8TeV_ll']
signal_groups['m_{Z} = 10 TeV'] = ['p8_pp_Zprime_10TeV_ll']
signal_groups['m_{Z} = 12 TeV'] = ['p8_pp_Zprime_12TeV_ll']
signal_groups['m_{Z} = 14 TeV'] = ['p8_pp_Zprime_14TeV_ll']
signal_groups['m_{Z} = 15 TeV'] = ['p8_pp_Zprime_15TeV_ll']
signal_groups['m_{Z} = 16 TeV'] = ['p8_pp_Zprime_16TeV_ll']
signal_groups['m_{Z} = 18 TeV'] = ['p8_pp_Zprime_18TeV_ll']
signal_groups['m_{Z} = 20 TeV'] = ['p8_pp_Zprime_20TeV_ll']
signal_groups['m_{Z} = 25 TeV'] = ['p8_pp_Zprime_25TeV_ll']
signal_groups['m_{Z} = 30 TeV'] = ['p8_pp_Zprime_30TeV_ll']
signal_groups['m_{Z} = 35 TeV'] = ['p8_pp_Zprime_35TeV_ll']
signal_groups['m_{Z} = 40 TeV'] = ['p8_pp_Zprime_40TeV_ll']

background_groups = collections.OrderedDict()
background_groups['Drell-Yan'] = ['mgp8_pp_tautau_lo','mgp8_pp_tautau_lo_PT_1000_2500']
background_groups['QCD'] = ['mgp8_pp_jj_lo','mgp8_pp_jj_lo_PT_1000_2500']


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
#selbase = 'Jet1_pf04_pt > 1000. && Jet2_pf04_pt > 1000. && ntau>1'

selbase = 'weight_2tagex**Jet1_pf04_pt > 1000. && Jet2_pf04_pt > 1000.'
seleta = ' && abs(Jet1_pf04_eta) < 2.5 && abs(Jet2_pf04_eta) < 2.5'
seldr = ' && abs(dphi)>2.0 && dr>2.5 && dr<4. '
selhighm = '&& met_pt>300.'
sellowm = '&& met_pt>400. && dr<3.8 && abs(dphi)>2.4'

# add mass-dependent list of event selections here if needed...

selections = collections.OrderedDict()
#selections['m_{Z} = 4 TeV'] = []
#selections['m_{Z} = 4 TeV'].append(selbase)

selections['m_{Z} = 5 TeV'] = []
selections['m_{Z} = 5 TeV'].append(selbase+seleta)
selections['m_{Z} = 5 TeV'].append(selbase+seleta+seldr)
selections['m_{Z} = 5 TeV'].append(selbase+seleta+seldr+sellowm)

selections['m_{Z} = 10 TeV'] = []
selections['m_{Z} = 10 TeV'].append(selbase+seleta)
selections['m_{Z} = 10 TeV'].append(selbase+seleta+seldr)
selections['m_{Z} = 10 TeV'].append(selbase+seleta+seldr+selhighm)

selections['m_{Z} = 15 TeV'] = []
selections['m_{Z} = 15 TeV'].append(selbase+seleta)
selections['m_{Z} = 15 TeV'].append(selbase+seleta+seldr)
selections['m_{Z} = 15 TeV'].append(selbase+seleta+seldr+selhighm)

selections['m_{Z} = 20 TeV'] = []
selections['m_{Z} = 20 TeV'].append(selbase+seleta)
selections['m_{Z} = 20 TeV'].append(selbase+seleta+seldr)
selections['m_{Z} = 20 TeV'].append(selbase+seleta+seldr+selhighm)

selections['m_{Z} = 25 TeV'] = []
selections['m_{Z} = 25 TeV'].append(selbase+seleta)
selections['m_{Z} = 25 TeV'].append(selbase+seleta+seldr)
selections['m_{Z} = 25 TeV'].append(selbase+seleta+seldr+selhighm)

selections['m_{Z} = 30 TeV'] = []
selections['m_{Z} = 30 TeV'].append(selbase+seleta)
selections['m_{Z} = 30 TeV'].append(selbase+seleta+seldr)
selections['m_{Z} = 30 TeV'].append(selbase+seleta+seldr+selhighm)

weights = collections.OrderedDict()
