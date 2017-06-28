import ROOT
import collections

### variable list
variables = {
    "tau32_1":{"name":"tau1_32","title":"#tau_{3,2}","bin":50,"xmin":0.0,"xmax":1.0},
#jet1pt,jet2pt,jet1eta,jet2eta...
# softdrop etc ...
}

colors = {}
colors['m_{Z} = 10 TeV'] = ROOT.kBlue
colors['m_{Z} = 20 TeV'] = ROOT.kBlue
colors['QCD'] = ROOT.kYellow
colors['tt'] = ROOT.kRed

signal_groups = collections.OrderedDict()
signal_groups['m_{Z} = 10 TeV'] = ['pp_Zprime_10TeV_ttbar']
signal_groups['m_{Z} = 20 TeV'] = ['pp_Zprime_20TeV_ttbar']

background_groups = collections.OrderedDict()
background_groups['QCD'] = ['pp_Zprime_20TeV_ttbar']
#background_groups['QCD'] = ['pp_jj']
#background_groups['tt'] = ['pp_tt012j_5f']

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
selbase = 'Jet1_pt > 500. && Jet2_pt > 300. && abs(Jet1_eta) < 2.5 && abs(Jet2_eta) < 2.5'

# add mass-dependent list of event selections here if needed...

selections = collections.OrderedDict()
selections['m_{Z} = 10 TeV'] = []
selections['m_{Z} = 10 TeV'].append(selbase)
selections['m_{Z} = 10 TeV'].append(selbase + '&& tau1_32 < 0.60')

selections['m_{Z} = 20 TeV'] = []
selections['m_{Z} = 20 TeV'].append(selbase)
selections['m_{Z} = 20 TeV'].append(selbase + '&& tau1_32 < 0.70')
