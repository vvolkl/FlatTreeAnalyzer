import ROOT
import collections

ana_tex = "ttV"

### variable list
variables = {
    "z_pt":{"name":"z_pt","title":"p_{T}^{Z} [GeV]","bin":200,"xmin":0,"xmax":1000},
    "z_m":{"name":"z_m","title":"m_{Z} [GeV]","bin":50,"xmin":0,"xmax":500},
    "l1_pt":{"name":"l1_pt","title":"p_{T}^{l, 1} [GeV]","bin":250,"xmin":0,"xmax":1000},
    "l2_pt":{"name":"l2_pt","title":"p_{T}^{l, 2} [GeV]","bin":250,"xmin":0,"xmax":1000},
    "met":{"name":"met_pt","title":"E_{T}^{miss}","bin":100,"xmin":0,"xmax":500},
    "nljets":{"name":"nljets","title":"N_{light}","bin":10,"xmin":0,"xmax":10},
    "nbjets":{"name":"nbjets","title":"N_{b-jets}","bin":10,"xmin":0,"xmax":10},
    "njets":{"name":"njets","title":"N_{jets}","bin":10,"xmin":0,"xmax":10},

}


colors = {}
colors['ttV'] = ROOT.kRed
colors['V+jets'] = ROOT.kGreen+2

signal_groups = collections.OrderedDict()
signal_groups['ttV'] = ['pp_ttv01j_5f']


background_groups = collections.OrderedDict()
background_groups['V+jets'] = ['pp_v0123j_5f']

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
selbase = 'l1_pt > 20. && l2_pt > 20.'

# add mass-dependent list of event selections here if needed...

selections = collections.OrderedDict()
selections['ttV'] = []
selections['ttV'].append(selbase)
selections['ttV'].append(selbase + '&& njets>3')
selections['ttV'].append(selbase + '&& nbjets>0 && njets>3')
