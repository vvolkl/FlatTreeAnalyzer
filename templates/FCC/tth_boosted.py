import ROOT
import collections

ana_tex = "tth_boosted"

### variable list
variables = {
    "h_m":{"name":"softDropped_higgsjet_m","title":"m_{SD}(H) [GeV]","bin":15,"xmin":0.0,"xmax":300.0},
    "h_mjj":{"name":"higgsjet_mjs","title":"m_{jj}(H) [GeV]","bin":15,"xmin":0.0,"xmax":300.0},
    "h_m2j":{"name":"higgsjet_mjj","title":"m_{jj}(H) [GeV]","bin":15,"xmin":0.0,"xmax":300.0},
    "h_mbb":{"name":"higgsjet_mbs","title":"m_{bb}(H) [GeV]","bin":15,"xmin":0.0,"xmax":300.0},
    "t_mjj":{"name":"topjet_mjs","title":"m_{jj}(top) [GeV]","bin":15,"xmin":0.0,"xmax":300.0},
    "t_mbb":{"name":"topjet_mbs","title":"m_{bb}(top) [GeV]","bin":15,"xmin":0.0,"xmax":300.0},
    "h_m_l":{"name":"softDropped_higgsjet_m","title":"m_{SD}(H) [GeV]","bin":30,"xmin":0.0,"xmax":300.0},
    "h_mjj_l":{"name":"higgsjet_mjs","title":"m_{jj}(H) [GeV]","bin":30,"xmin":0.0,"xmax":300.0},
    "h_m2j_l":{"name":"higgsjet_mjj","title":"m_{jj}(H) [GeV]","bin":30,"xmin":0.0,"xmax":300.0},
    #"h_mbb_l":{"name":"higgsjet_mbs","title":"m_{bb}(H) [GeV]","bin":30,"xmin":0.0,"xmax":300.0},
    "h_mjj_l60":{"name":"higgsjet_mjs","title":"m_{jj}(H) [GeV]","bin":60,"xmin":0.0,"xmax":300.0},
    #"h_mbb_l60":{"name":"higgsjet_mbs","title":"m_{bb}(H) [GeV]","bin":60,"xmin":0.0,"xmax":300.0},
    "h_mjj_l90":{"name":"higgsjet_mjs","title":"m_{jj}(H) [GeV]","bin":90,"xmin":0.0,"xmax":300.0},
    "h_m2j_l90":{"name":"higgsjet_mjj","title":"m_{jj}(H) [GeV]","bin":90,"xmin":0.0,"xmax":300.0},
    #"h_mbb_l90":{"name":"higgsjet_mbs","title":"m_{bb}(H) [GeV]","bin":90,"xmin":0.0,"xmax":300.0},
    "h_mjj_l120":{"name":"higgsjet_mjs","title":"m_{jj}(H) [GeV]","bin":120,"xmin":0.0,"xmax":300.0},
    "h_m2j_l120":{"name":"higgsjet_mjj","title":"m_{jj}(H) [GeV]","bin":120,"xmin":0.0,"xmax":300.0},
    #"h_mbb_l120":{"name":"higgsjet_mbs","title":"m_{bb}(H) [GeV]","bin":120,"xmin":0.0,"xmax":300.0},
    "h_mjj_l150":{"name":"higgsjet_mjs","title":"m_{jj}(H) [GeV]","bin":150,"xmin":0.0,"xmax":300.0},
    "h_m2j_l150":{"name":"higgsjet_mjj","title":"m_{jj}(H) [GeV]","bin":150,"xmin":0.0,"xmax":300.0},
    "h_mbb_l150":{"name":"higgsjet_mbs","title":"m_{bb}(H) [GeV]","bin":150,"xmin":0.0,"xmax":300.0},
    "h_dRjj":{"name":"higgsjet_dRjj","title":"#Delta R(jj) (H)","bin":100,"xmin":0.0,"xmax":4.0},
####
    "h_m1j_l10":{"name":"higgsjet_mj","title":"m_{j}(H) [GeV]","bin":10,"xmin":0.0,"xmax":100.0},
    "h_m1j_l20":{"name":"higgsjet_mj","title":"m_{j}(H) [GeV]","bin":20,"xmin":0.0,"xmax":100.0},
    "h_m1j_l50":{"name":"higgsjet_mj","title":"m_{j}(H) [GeV]","bin":50,"xmin":0.0,"xmax":100.0},
    "h_m1j_l100":{"name":"higgsjet_mj","title":"m_{j}(H) [GeV]","bin":100,"xmin":0.0,"xmax":100.0},
####
    "h_mSD":{"name":"softDropped_higgsjet_m","title":"m_{SD}(H) [GeV]","bin":15,"xmin":0.0,"xmax":300.0},
    "h_mSD_l":{"name":"softDropped_higgsjet_m","title":"m_{SD}(H) [GeV]","bin":30,"xmin":0.0,"xmax":300.0},
    "h_mSD_l60":{"name":"softDropped_higgsjet_m","title":"m_{SD}(H) [GeV]","bin":60,"xmin":0.0,"xmax":300.0},
    "h_mSD_l90":{"name":"softDropped_higgsjet_m","title":"m_{SD}(H) [GeV]","bin":90,"xmin":0.0,"xmax":300.0},
    "h_mSD_l120":{"name":"softDropped_higgsjet_m","title":"m_{SD}(H) [GeV]","bin":120,"xmin":0.0,"xmax":300.0},
    "h_mSD_l150":{"name":"softDropped_higgsjet_m","title":"m_{SD}(H) [GeV]","bin":150,"xmin":0.0,"xmax":300.0},
####
    "h_tau21":{"name":"higgsjet_tau21","title":"#tau_{2,1}(H)","bin":50,"xmin":0.0,"xmax":1.0},
    "h_tau32":{"name":"higgsjet_tau32","title":"#tau_{3,2}(H)","bin":50,"xmin":0.0,"xmax":1.0},
    "h_njs":{"name":"higgsjet_njs","title":"N_{j}(H)","bin":6,"xmin":-0.5,"xmax":5.5},
    "h_nbs":{"name":"higgsjet_nbs","title":"N_{b}(H)","bin":6,"xmin":-0.5,"xmax":5.5},
    "h_ncs":{"name":"higgsjet_ncs","title":"N_{c}(H)","bin":6,"xmin":-0.5,"xmax":5.5},
    "h_nls":{"name":"higgsjet_nls","title":"N_{l}(H)","bin":6,"xmin":-0.5,"xmax":5.5},
    #"h_bdt":{"name":"higgsjet_bdt_th","title":"BDT(H)","bin":50,"xmin":-1.0,"xmax":1.0},
    "top_m":{"name":"softDropped_topjet_m","title":"m_{SD}(t) [GeV]","bin":50,"xmin":0.0,"xmax":300.0},
    "top_tau21":{"name":"topjet_tau21","title":"#tau_{2,1}(t)","bin":50,"xmin":0.0,"xmax":1.0},
    "top_tau32":{"name":"topjet_tau32","title":"#tau_{3,2}(t)","bin":50,"xmin":0.0,"xmax":1.0},
    #"top_bdt":{"name":"topjet_bdt_th","title":"BDT(t)","bin":50,"xmin":-1.0,"xmax":1.0},
    "top_njs":{"name":"topjet_njs","title":"N_{j}(t)","bin":6,"xmin":-0.5,"xmax":5.5},
    "top_nbs":{"name":"topjet_nbs","title":"N_{b}(t)","bin":6,"xmin":-0.5,"xmax":5.5},
    "top_ncs":{"name":"topjet_ncs","title":"N_{c}(t)","bin":6,"xmin":-0.5,"xmax":5.5},
    "top_nls":{"name":"topjet_nls","title":"N_{l}(t)","bin":6,"xmin":-0.5,"xmax":5.5},
    "l_pt":{"name":"l_pt","title":"p_{T}^{l} [GeV]","bin":50,"xmin":0.0,"xmax":500.0},
    "met":{"name":"met_pt","title":"E_{T}^{miss} [GeV]","bin":50,"xmin":0.0,"xmax":1000.0},
    "nbjets":{"name":"nbjets","title":"N_{b}","bin":6,"xmin":-0.5,"xmax":5.5},
    #"weight_0tagex":{"name":"weight_0tagex","title":"TRF 0 btag excl","bin":50,"xmin":0.,"xmax":1.},
    #"weight_1tagex":{"name":"weight_1tagex","title":"TRF 1 btag excl","bin":50,"xmin":0.,"xmax":1.},
    #"weight_2tagex":{"name":"weight_2tagex","title":"TRF 2 btag excl","bin":50,"xmin":0.,"xmax":1.},
    #"weight_3tagex":{"name":"weight_3tagex","title":"TRF 3 btag excl","bin":50,"xmin":0.,"xmax":1.},
    #"weight_4tagex":{"name":"weight_4tagex","title":"TRF 4 btag excl","bin":50,"xmin":0.,"xmax":1.},
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

# base pre-selections
selbase  = 'l_pt > 25. && higgsjet_pt > 200. && topjet_pt > 200.'
selbase  += ' && abs(l_eta) > 3.0 && abs(higgsjet_eta) < 3.0 && abs(topjet_eta) < 3.0'
selbase  += ' && higgsjet_njs >= 2 && topjet_njs >= 2'

# loose top selection, right now only for consistency, but will be needed when add W+jets
sel_top = selbase + ' && softDropped_topjet_m > 120. && softDropped_topjet_m < 250. && topjet_tau32 < 0.8'

# do not apply mSD cut, because we will fit on that variable later
sel_higgs = sel_top + ' && higgsjet_tau21 < 0.6'

## tight btag selection
#######################
## init -> sel_bs = sel_higgs + ' && nbjets > 3 && higgsjet_nbs > 1'
#######################
## SR
sel_bs = sel_higgs + ' && nbjets >= 4'
sel_bsTRF = 'weight_4tagin**' + sel_higgs

# just to know SR s/b
sel_mass = sel_bs +' && higgsjet_mjj > 100. && higgsjet_mjj < 135.'
sel_massTRF = sel_bsTRF +' && higgsjet_mjj > 100. && higgsjet_mjj < 135.'

## ttj CR
sel_bsless = sel_higgs + ' && nbjets < 4'
sel_bslessTRF = 'weight_4tagless**' + sel_higgs
sel_bslessTRF2 = 'weight_3tagless**' + sel_higgs

## ttbb CR tests
sel_antitop = selbase + ' && (softDropped_topjet_m < 120. || softDropped_topjet_m > 250.) && topjet_tau32 > 0.8'
sel_antihiggs = sel_antitop + ' && higgsjet_tau21 < 0.6'
sel_antibsTRF = 'weight_4tagin**' + sel_antihiggs
#
sel_anti2top = selbase + ' && (softDropped_topjet_m < 120. || softDropped_topjet_m > 250.) && topjet_tau32 > 0.8'
sel_anti2higgs = sel_anti2top + ' && higgsjet_tau21 > 0.6'
sel_anti2bsTRF = 'weight_4tagin**' + sel_anti2higgs
#
sel_anti3top = selbase + ' && softDropped_topjet_m > 120. && softDropped_topjet_m < 250. && topjet_tau32 < 0.8'
sel_anti3higgs = sel_anti3top + ' && higgsjet_tau21 > 0.6'
sel_anti3bsTRF = 'weight_4tagin**' + sel_anti3higgs

# 2D cuts tests
sel_full = sel_bsTRF
sel2D_loose = ' && (topjet_mjj/higgsjet_mjj)>1.-(topjet_dRjj/higgsjet_dRjj) '
sel2D_tight = ' && (topjet_mjj/higgsjet_mjj)>1.5-(topjet_dRjj/higgsjet_dRjj) '
seltHmjj_tight = ' && (topjet_mjj/higgsjet_mjj)>0.9 '
seltHmjs_tight = ' && (topjet_mjs/higgsjet_mjs)>1.6 '
sel250 = ' && higgsjet_pt > 250. && topjet_pt > 250. '
#
sel200_no2D    = sel_full
sel200_2Dloose = sel_full + sel2D_loose
sel200_2Dtight = sel_full + sel2D_tight
sel250_no2D    = sel_full + sel250
sel250_2Dloose = sel_full + sel250 + sel2D_loose
sel250_2Dtight = sel_full + sel250 + sel2D_tight
#
sel200_tHmjjtight = sel_full + seltHmjj_tight
sel250_tHmjjtight = sel_full + sel250 + seltHmjj_tight
sel200_tHmjstight = sel_full + seltHmjs_tight
sel250_tHmjstight = sel_full + sel250 + seltHmjs_tight


selections = collections.OrderedDict()

selections['ttH'] = []
selections['ttH'].append(selbase)
selections['ttH'].append(sel_top)
selections['ttH'].append(sel_higgs)
#selections['ttH'].append(sel_bs)
selections['ttH'].append(sel_bsTRF)
#selections['ttH'].append(sel_bsless)
selections['ttH'].append(sel_bslessTRF)
selections['ttH'].append(sel_bslessTRF2)
selections['ttH'].append(sel_mass)
selections['ttH'].append(sel_massTRF)
selections['ttH'].append(sel_antibsTRF)
selections['ttH'].append(sel_anti2bsTRF)
selections['ttH'].append(sel_anti3bsTRF)
## tests for tail Mjj removal
#selections['ttH'].append(sel200_no2D) -> the chosen one in the end
#selections['ttH'].append(sel200_2Dloose)
#selections['ttH'].append(sel200_2Dtight)
#selections['ttH'].append(sel250_no2D)
#selections['ttH'].append(sel250_2Dloose)
#selections['ttH'].append(sel250_2Dtight)
#selections['ttH'].append(sel200_tHmjjtight)
#selections['ttH'].append(sel250_tHmjjtight)
#selections['ttH'].append(sel200_tHmjstight)
#selections['ttH'].append(sel250_tHmjstight)

