import ROOT
import collections

### variable list
variables = {
    #"ptzp":{"name":"zprime_muon_pt","title":"p_{T}^{Zprime} [GeV]","bin":200,"xmin":0,"xmax":20000},
    "njets":{"name":"njets","title":"njets","bin":20,"xmin":0,"xmax":20},
    "nbjets":{"name":"nbjets","title":"nbjets","bin":20,"xmin":0,"xmax":20},
    "nextraleptons":{"name":"nextraleptons","title":"nextraleptons","bin":8,"xmin":0,"xmax":8},
    "higgs_m":{"name":"higgs_m","title":"m_{H} [GeV]","bin":200,"xmin":0,"xmax":1000},
    "ptl_1":{"name":"l1_pt","title":"p_{T}^{l1} [GeV]","bin":250,"xmin":0,"xmax":2500},
    "ptl_2":{"name":"l2_pt","title":"p_{T}^{l2} [GeV]","bin":250,"xmin":0,"xmax":2500},
    "ptl_3":{"name":"l3_pt","title":"p_{T}^{l3} [GeV]","bin":250,"xmin":0,"xmax":2500},
    "ptl_4":{"name":"l4_pt","title":"p_{T}^{l4} [GeV]","bin":250,"xmin":0,"xmax":2500},
    "met_pt":{"name":"met_pt","title":"E_{T}^{miss}","bin":50,"xmin":0,"xmax":100},
}


colors = {}
colors['pp_tth01j_5f_hllll'] = ROOT.kRed
colors['background'] = ROOT.kGreen+2
#colors['pp_tt4l_4f'] = ROOT.kGreen+2
#colors['pp_ttv01j_5f'] = ROOT.kGreen+3
#colors['pp_h012j_5f_hllll'] = ROOT.kGreen+4
#colors['pp_vbf_h01j_5f_hllll'] = ROOT.kGreen+5
#colors['pp_vh012j_5f_hllll'] = ROOT.kGreen+6
#colors['pp_vv012j_5f'] = ROOT.kGreen+7
#colors['pp_vvv01j_5f'] = ROOT.kGreen+8

signal_groups = collections.OrderedDict()
signal_groups['pp_tth01j_5f_hllll'] = ['pp_tth01j_5f_hllll']

background_groups = collections.OrderedDict()
background_groups['background'] = ['pp_tt4l_4f',
  'pp_ttv01j_5f',
  'pp_h012j_5f_hllll',
  'pp_vbf_h01j_5f_hllll',
  'pp_vh012j_5f_hllll',
  'pp_vv012j_5f',
  'pp_vvv01j_5f',
  ]

#background_groups['pp_ttv01j_5f'] = ['pp_ttv01j_5f']
#background_groups['pp_h012j_5f_hllll'] = ['pp_h012j_5f_hllll']
#background_groups['pp_vbf_h01j_5f_hllll'] = ['pp_vbf_h01j_5f_hllll']
#background_groups['pp_vh012j_5f_hllll'] = ['pp_vh012j_5f_hllll']
#background_groups['pp_vv012j_5f'] = ['pp_vv012j_5f']
#background_groups['pp_vvv01j_5f'] = ['pp_vvv01j_5f']

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
selbase = 'higgs_m > 0'

# add mass-dependent list of event selections here if needed...

selections = collections.OrderedDict()
selections['pp_tth01j_5f_hllll'] = []
selections['pp_tth01j_5f_hllll'].append(selbase)
