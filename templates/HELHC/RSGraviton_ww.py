import ROOT
import collections

ana_tex = "G_{RS} #rightarrow W^{+}W^{-}"

### variable list
variables = {
#	'Jet1_tau21':{'name':'Jet1_trk02_tau21','title':'Jet1 #tau_{2,1}','bin':50,'xmin':0.0,'xmax':1.0},
#        'Jet1_tau32':{'name':'Jet1_trk02_tau32','title':'Jet1 #tau_{3,2}','bin':50,'xmin':0.0,'xmax':1.0},
#        'Jet1_tau31':{'name':'Jet1_trk02_tau31','title':'Jet1 #tau_{3,1}','bin':50,'xmin':0.0,'xmax':1.0},
#
#        'Jet1_SD_Cor_pt':{'name':'Jet1_trk02_SD_Corr_pt','title':'Jet1 p_{T} (SD cor) [TeV]','bin':50,'xmin':0.,'xmax':10., 'divide':1000},
#        'Jet1_SD_Cor_eta':{'name':'Jet1_trk02_SD_Corr_eta','title':'Jet1 #eta (SD cor)','bin':50,'xmin':-5.0,'xmax':5.0},
#        'Jet1_trk02_SD_Cor_m':{'name':'Jet1_trk02_SD_Corr_m','title':'Jet1 trk02 mass (SD cor) [GeV]','bin':100,'xmin':0.0,'xmax':500},
#        'Jet1_trk04_SD_Cor_m':{'name':'Jet1_trk04_SD_Corr_m','title':'Jet1 trk04 mass (SD cor) [GeV]','bin':100,'xmin':0.0,'xmax':500},
#        'Jet1_trk08_SD_Cor_m':{'name':'Jet1_trk08_SD_Corr_m','title':'Jet1 trk08 mass (SD cor) [GeV]','bin':100,'xmin':0.0,'xmax':500},
#
#	'Jet2_tau21':{'name':'Jet2_trk02_tau21','title':'Jet2 #tau_{2,1}','bin':50,'xmin':0.0,'xmax':1.0},
#        'Jet2_tau32':{'name':'Jet2_trk02_tau32','title':'Jet2 #tau_{3,2}','bin':50,'xmin':0.0,'xmax':1.0},
#        'Jet2_tau31':{'name':'Jet2_trk02_tau31','title':'Jet2 #tau_{3,1}','bin':50,'xmin':0.0,'xmax':1.0},
#
#        'Jet2_SD_Cor_pt':{'name':'Jet2_trk02_SD_Corr_pt','title':'Jet2 p_{T} (SD cor) [TeV]','bin':50,'xmin':0.,'xmax':10., 'divide':1000},
#        'Jet2_SD_Cor_eta':{'name':'Jet2_trk02_SD_Corr_eta','title':'Jet2 #eta (SD cor)','bin':50,'xmin':-5.0,'xmax':5.0},
#        'Jet2_trk02_SD_Cor_m':{'name':'Jet2_trk02_SD_Corr_m','title':'Jet2 trk02 mass (SD cor) [GeV]','bin':100,'xmin':0.0,'xmax':500},
#        'Jet2_trk04_SD_Cor_m':{'name':'Jet2_trk04_SD_Corr_m','title':'Jet2 trk04 mass (SD cor) [GeV]','bin':100,'xmin':0.0,'xmax':500},
#        'Jet2_trk08_SD_Cor_m':{'name':'Jet2_trk08_SD_Corr_m','title':'Jet2 trk08 mass (SD cor) [GeV]','bin':100,'xmin':0.0,'xmax':500},
#
#        'rapiditySeparation':{'name':'rapiditySeparation_trk02','title':'Rapidity Separation','bin':50,'xmin':0.0,'xmax':10.0},
#        'transverseMomentumAsymmetry':{'name':'transverseMomentumAsymmetry_trk02','title':'Transverse Momentum Asymmetry','bin':50,'xmin':0.0,'xmax':1.0},
#
##        'Mj1j2_trk02' :{'name':'Mj1j2_trk02','title':'m_{RSG\'} [TeV] (trk02)','bin':125,'xmin':5.0,'xmax':30.0, 'divide':1000},
##        'Mj1j2_trk02_Corr' :{'name':'Mj1j2_trk02_Corr','title':'m_{RSG\'} [TeV] (trk02 cor)','bin':125,'xmin':5.0,'xmax':30.0, 'divide':1000},
#
##        'Mj1j2_pf02' :{'name':'Mj1j2_pf02','title':'m_{RSG\'} [TeV] (pf02)','bin':125,'xmin':5.0,'xmax':30.0, 'divide':1000},
#
##        'Mj1j2_pf04' :{'name':'Mj1j2_pf04','title':'m_{RSG\'} [TeV] (pf04)','bin':125,'xmin':5.0,'xmax':30.0, 'divide':1000},
#
#        'Mj1j2_pf08' :{'name':'Mj1j2_pf08','title':'m_{RSG} [TeV] (pf08)','bin':250,'xmin':0.0,'xmax':20.0, 'divide':1000},
#
#        'Jet1_Flow15':{'name':'Jet1_Flow15','title':'Flow_{1,5} Jet_1','bin':200,'xmin':0.0,'xmax':1.0},
#        'Jet2_Flow15':{'name':'Jet2_Flow15','title':'Flow_{1,5} Jet_2','bin':200,'xmin':0.0,'xmax':1.0},
#        'Jet1_Flow25':{'name':'Jet1_Flow25','title':'Flow_{2,5} Jet_1','bin':200,'xmin':0.0,'xmax':1.0},
#        'Jet2_Flow25':{'name':'Jet2_Flow25','title':'Flow_{2,5} Jet_2','bin':200,'xmin':0.0,'xmax':1.0},
#        'Jet1_Flow35':{'name':'Jet1_Flow35','title':'Flow_{3,5} Jet_1','bin':200,'xmin':0.0,'xmax':1.0},
#        'Jet2_Flow35':{'name':'Jet2_Flow35','title':'Flow_{3,5} Jet_2','bin':200,'xmin':0.0,'xmax':1.0},
#        'Jet1_Flow45':{'name':'Jet1_Flow45','title':'Flow_{4,5} Jet_1','bin':200,'xmin':0.0,'xmax':1.0},
#        'Jet2_Flow45':{'name':'Jet2_Flow45','title':'Flow_{4,5} Jet_2','bin':200,'xmin':0.0,'xmax':1.0},
#        'Jet1_Flow55':{'name':'Jet1_Flow55','title':'Flow_{5,5} Jet_1','bin':200,'xmin':0.0,'xmax':1.0},
#        'Jet2_Flow55':{'name':'Jet2_Flow55','title':'Flow_{5,5} Jet_2','bin':200,'xmin':0.0,'xmax':1.0},
#        'Jet1_Whad_vs_QCD_tagger' :{'name':'Jet1_Whad_vs_QCD_tagger','title':'Jet1 W had. vs QCD tagger','bin':100,'xmin':-1.,'xmax':1.},
#        'Jet2_Whad_vs_QCD_tagger' :{'name':'Jet2_Whad_vs_QCD_tagger','title':'Jet2 W had. vs QCD tagger','bin':100,'xmin':-1.,'xmax':1.},
####################
## rebin for note ##
####################
#        'Mj1j2_pf08' :{'name':'Mj1j2_pf08','title':'m_{RSG} [TeV] (pf08)','bin':50,'xmin':0.0,'xmax':25.0, 'divide':1000},
#        'Mj1j2_pf08_fit' :{'name':'Mj1j2_pf08_fit','title':'m_{RSG} [TeV] (pf08)','bin':50,'xmin':0.0,'xmax':20.5, 'divide':1000},
#        'Jet1_trk02_SD_Cor_m':{'name':'Jet1_trk02_SD_Corr_m','title':'Jet1 trk02 mass (SD cor) [GeV]','bin':25,'xmin':0.0,'xmax':500},
#        'Jet2_trk02_SD_Cor_m':{'name':'Jet2_trk02_SD_Corr_m','title':'Jet2 trk02 mass (SD cor) [GeV]','bin':25,'xmin':0.0,'xmax':500},
#       'Jet1_tau21':{'name':'Jet1_trk02_tau21','title':'Jet1 #tau_{2,1}','bin':25,'xmin':0.0,'xmax':1.0},
#       'Jet2_tau21':{'name':'Jet2_trk02_tau21','title':'Jet2 #tau_{2,1}','bin':25,'xmin':0.0,'xmax':1.0},
#        'Jet1_Flow45':{'name':'Jet1_Flow45','title':'Flow_{4,5} Jet_1','bin':25,'xmin':0.0,'xmax':1.0},
#        'Jet2_Flow45':{'name':'Jet2_Flow45','title':'Flow_{4,5} Jet_2','bin':25,'xmin':0.0,'xmax':1.0},
#        'Jet1_Flow55':{'name':'Jet1_Flow55','title':'Flow_{5,5} Jet_1','bin':25,'xmin':0.0,'xmax':1.0},
#        'Jet2_Flow55':{'name':'Jet2_Flow55','title':'Flow_{5,5} Jet_2','bin':25,'xmin':0.0,'xmax':1.0},
#        'Jet1_Whad_vs_QCD_tagger' :{'name':'Jet1_Whad_vs_QCD_tagger','title':'Jet1 W had. vs QCD tagger','bin':25,'xmin':-1.,'xmax':1.},
#        'Jet2_Whad_vs_QCD_tagger' :{'name':'Jet2_Whad_vs_QCD_tagger','title':'Jet2 W had. vs QCD tagger','bin':25,'xmin':-1.,'xmax':1.},

        'Mj1j2_pf08_fit' :{'name':'Mj1j2_pf08_fit','title':'m_{RSG} [TeV] (pf08)','bin':50,'xmin':0.0,'xmax':20.5, 'divide':1000},
}

variables2D = {}


colors = {}
colors['m_{RSG} = 2 TeV']  = ROOT.kRed
colors['m_{RSG} = 4 TeV']  = ROOT.kRed
colors['m_{RSG} = 6 TeV'] = ROOT.kRed
colors['m_{RSG} = 8 TeV'] = ROOT.kRed
colors['m_{RSG} = 10 TeV'] = ROOT.kRed
colors['m_{RSG} = 12 TeV'] = ROOT.kRed
colors['m_{RSG} = 14 TeV'] = ROOT.kRed
colors['QCD'] = ROOT.kBlue+1
colors['tt']  = ROOT.kOrange-2
colors['vv']  = ROOT.kGreen+2
colors['vj']  = ROOT.kMagenta+2

signal_groups = collections.OrderedDict()
signal_groups['m_{RSG} = 2 TeV']  = ['p8_pp_RSGraviton_2TeV_ww']
signal_groups['m_{RSG} = 4 TeV']  = ['p8_pp_RSGraviton_4TeV_ww']
signal_groups['m_{RSG} = 6 TeV']  = ['p8_pp_RSGraviton_6TeV_ww']
signal_groups['m_{RSG} = 8 TeV']  = ['p8_pp_RSGraviton_8TeV_ww']
signal_groups['m_{RSG} = 10 TeV'] = ['p8_pp_RSGraviton_10TeV_ww']
signal_groups['m_{RSG} = 12 TeV'] = ['p8_pp_RSGraviton_12TeV_ww']
signal_groups['m_{RSG} = 14 TeV'] = ['p8_pp_RSGraviton_14TeV_ww']

background_groups = collections.OrderedDict()
background_groups['vv']  = [
'mgp8_pp_vv_5f_HT_500_1000',
'mgp8_pp_vv_5f_HT_1000_2000',
'mgp8_pp_vv_5f_HT_2000_5000',
'mgp8_pp_vv_5f_HT_5000_10000',
'mgp8_pp_vv_5f_HT_10000_27000']
background_groups['vj']  = [
'mgp8_pp_vj_5f_HT_500_1000',
'mgp8_pp_vj_5f_HT_1000_2000',
'mgp8_pp_vj_5f_HT_2000_5000',
'mgp8_pp_vj_5f_HT_5000_10000',
'mgp8_pp_vj_5f_HT_10000_27000']
background_groups['tt']  = [
'mgp8_pp_tt_5f_HT_500_1000',
'mgp8_pp_tt_5f_HT_1000_2000',
'mgp8_pp_tt_5f_HT_2000_5000',
'mgp8_pp_tt_5f_HT_5000_10000',
'mgp8_pp_tt_5f_HT_10000_27000']
background_groups['QCD'] = [
'mgp8_pp_jj_5f_HT_500_1000',
'mgp8_pp_jj_5f_HT_1000_2000',
'mgp8_pp_jj_5f_HT_2000_5000',
'mgp8_pp_jj_5f_HT_5000_10000',
'mgp8_pp_jj_5f_HT_10000_27000']

# global parameters
intLumi = 1.5e+07
delphesVersion = '3.4.2'

uncertainties = []
uncertainties.append([0., 0.])
uncertainties.append([0.02, 0.0])
uncertainties.append([0.02, 0.02])
uncertainties.append([0.02, 0.10])

# the first time needs to be set to True
runFull = False

HELHC=True

#####################
# base pre-selections
#####################
selbase = 'Jet1_trk02_SD_Corr_pt > 1000. && Jet2_trk02_SD_Corr_pt > 1000. && abs(Jet1_trk02_SD_Corr_eta) < 3.&& abs(Jet1_trk02_SD_Corr_eta) < 3.'
# clean cuts
selbase += ' && Jet1_trk02_tau21>0 && Jet1_trk02_tau31>0 && Jet1_trk02_tau32>0 && Jet2_trk02_tau21>0 && Jet2_trk02_tau31>0 && Jet2_trk02_tau32>0'
# add extra free clean cut
selbase += ' && rapiditySeparation_trk02<2.4 && Mj1j2_pf08>2.0'

#####################
# CUT base selection
#####################
sel1c = selbase + ' && Jet1_trk02_SD_Corr_m > 50.&& Jet1_trk02_SD_Corr_m < 100. && Jet2_trk02_SD_Corr_m > 50.&& Jet2_trk02_SD_Corr_m < 100. && Jet1_trk02_tau21 <0.6 && Jet2_trk02_tau21 <0.6'
sel2c = sel1c   + ' && Jet1_Flow45 < 0.07 && Jet2_Flow45 < 0.07 && Jet1_Flow55 < 0.07 && Jet2_Flow55 < 0.07'

#####################
# anti-QCD jet tagger selection
#####################
sel1t = selbase + ' && Jet1_Whad_vs_QCD_tagger>0.15 && Jet2_Whad_vs_QCD_tagger>0.15'
## + extra cuts
sel2t = sel1t   + ' && Jet1_trk02_SD_Corr_m>40. && Jet2_trk02_SD_Corr_m>40.'

selections = collections.OrderedDict()

selections['m_{RSG} = 2 TeV'] = []
selections['m_{RSG} = 2 TeV'].append(selbase)
selections['m_{RSG} = 2 TeV'].append(sel1c)
selections['m_{RSG} = 2 TeV'].append(sel2c)
selections['m_{RSG} = 2 TeV'].append(sel1t)
selections['m_{RSG} = 2 TeV'].append(sel2t)

selections['m_{RSG} = 4 TeV'] = []
selections['m_{RSG} = 4 TeV'].append(selbase)
selections['m_{RSG} = 4 TeV'].append(sel1c)
selections['m_{RSG} = 4 TeV'].append(sel2c)
selections['m_{RSG} = 4 TeV'].append(sel1t)
selections['m_{RSG} = 4 TeV'].append(sel2t)

selections['m_{RSG} = 6 TeV'] = []
selections['m_{RSG} = 6 TeV'].append(selbase)
selections['m_{RSG} = 6 TeV'].append(sel1c)
selections['m_{RSG} = 6 TeV'].append(sel2c)
selections['m_{RSG} = 6 TeV'].append(sel1t)
selections['m_{RSG} = 6 TeV'].append(sel2t)

selections['m_{RSG} = 8 TeV'] = []
selections['m_{RSG} = 8 TeV'].append(selbase)
selections['m_{RSG} = 8 TeV'].append(sel1c)
selections['m_{RSG} = 8 TeV'].append(sel2c)
selections['m_{RSG} = 8 TeV'].append(sel1t)
selections['m_{RSG} = 8 TeV'].append(sel2t)

selections['m_{RSG} = 10 TeV'] = []
selections['m_{RSG} = 10 TeV'].append(selbase)
selections['m_{RSG} = 10 TeV'].append(sel1c)
selections['m_{RSG} = 10 TeV'].append(sel2c)
selections['m_{RSG} = 10 TeV'].append(sel1t)
selections['m_{RSG} = 10 TeV'].append(sel2t)

selections['m_{RSG} = 12 TeV'] = []
selections['m_{RSG} = 12 TeV'].append(selbase)
selections['m_{RSG} = 12 TeV'].append(sel1c)
selections['m_{RSG} = 12 TeV'].append(sel2c)
selections['m_{RSG} = 12 TeV'].append(sel1t)
selections['m_{RSG} = 12 TeV'].append(sel2t)

selections['m_{RSG} = 14 TeV'] = []
selections['m_{RSG} = 14 TeV'].append(selbase)
selections['m_{RSG} = 14 TeV'].append(sel1c)
selections['m_{RSG} = 14 TeV'].append(sel2c)
selections['m_{RSG} = 14 TeV'].append(sel1t)
selections['m_{RSG} = 14 TeV'].append(sel2t)
