import ROOT
import collections

### variable list
variables = {
    "h_m":{"name":"softDropped_higgsjet_m","title":"m_{SD}(H) [GeV]","bin":15,"xmin":0.0,"xmax":300.0},
    "h_mbb":{"name":"higgsjet_mbs","title":"m_{bb}(H) [GeV]","bin":15,"xmin":0.0,"xmax":300.0},
    "h_m_l":{"name":"softDropped_higgsjet_m","title":"m_{SD}(H) [GeV]","bin":30,"xmin":0.0,"xmax":300.0},
    "h_mbb_l":{"name":"higgsjet_mbs","title":"m_{bb}(H) [GeV]","bin":30,"xmin":0.0,"xmax":300.0},
    "h_tau21":{"name":"higgsjet_tau21","title":"#tau_{2,1}(H)","bin":50,"xmin":0.0,"xmax":1.0},
    "h_tau32":{"name":"higgsjet_tau32","title":"#tau_{3,2}(H)","bin":50,"xmin":0.0,"xmax":1.0},
    "h_nbs":{"name":"higgsjet_nbs","title":"N_{b}(H)","bin":6,"xmin":-0.5,"xmax":5.5},
    "h_bdt":{"name":"higgsjet_bdt_th","title":"BDT(H)","bin":50,"xmin":-1.0,"xmax":1.0},
    "top_m":{"name":"softDropped_topjet_m","title":"m_{SD}(t) [GeV]","bin":50,"xmin":0.0,"xmax":300.0},
    "top_tau21":{"name":"topjet_tau21","title":"#tau_{2,1}(t)","bin":50,"xmin":0.0,"xmax":1.0},
    "top_tau32":{"name":"topjet_tau32","title":"#tau_{3,2}(t)","bin":50,"xmin":0.0,"xmax":1.0},
    "top_bdt":{"name":"topjet_bdt_th","title":"BDT(t)","bin":50,"xmin":-1.0,"xmax":1.0},
    "top_nbs":{"name":"topjet_nbs","title":"N_{b}(t)","bin":6,"xmin":-0.5,"xmax":5.5},
    "l_pt":{"name":"l_pt","title":"p_{T}^{l} [GeV]","bin":50,"xmin":0.0,"xmax":500.0},
    "met":{"name":"met_pt","title":"E_{T}^{miss} [GeV]","bin":50,"xmin":0.0,"xmax":1000.0},
    "nbjets":{"name":"nbjets","title":"N_{b}","bin":6,"xmin":-0.5,"xmax":5.5},

}

variables2D = {
}


colors = {}

colors['ttH'] = ROOT.kRed
colors['tt+jets'] = ROOT.kGreen+1
colors['tt+bb'] = ROOT.kAzure
colors['ttZ'] = ROOT.kMagenta



signal_groups = collections.OrderedDict()

signal_groups['ttH'] = ['mgp8_pp_tth01j_5f_hbb']

background_groups = collections.OrderedDict()



background_groups['tt+jets'] = [
                            'mgp8_pp_ttj_4f',
                           ]

background_groups['tt+bb'] = [
                            'mgp8_pp_ttbb_4f',
                           ]
                          
background_groups['ttZ'] = [
                            'mgp8_pp_ttz_5f_zbb',
                           ]
                           

# global parameters
intLumi = 30000000

delphesVersion = '3.4.2'

uncertainties = []
uncertainties.append([0., 0.])
uncertainties.append([0.01, 0.00])
uncertainties.append([0.01, 0.001])

# the first time needs to be set to True
runFull = True
#runFull = False

# base pre-selections

selbase  = 'l_pt > 25. && higgsjet_pt > 250. && topjet_pt > 250.'
selbase  = 'abs(l_eta) > 3.0 && abs(higgsjet_eta) < 3.0 && abs(topjet_eta) < 3.0'

# loose top selection, right now only for consistency, but will be needed when add W+jets
sel_top = selbase + ' && softDropped_topjet_m > 120. && softDropped_topjet_m < 250. && topjet_tau32 < 0.8'

# do not apply mSD cut, because we will fit on that variable later
sel_higgs = sel_top + ' && higgsjet_tau21 < 0.6'


# tight btag selection
sel_bs = sel_higgs + ' && nbjets > 3 && higgsjet_nbs > 1'

# just to know s/b
sel_mass = sel_bs +' && higgsjet_mbs > 100. && higgsjet_mbs < 135.'

selections = collections.OrderedDict()

selections['ttH'] = []
selections['ttH'].append(selbase)
selections['ttH'].append(sel_top)
selections['ttH'].append(sel_higgs)
selections['ttH'].append(sel_bs)
selections['ttH'].append(sel_mass)
