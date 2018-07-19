import ROOT
import collections

### variable list
variables = {
	'Jet1_tau21':{'name':'Jet1_trk02_tau21','title':'Jet1 #tau_{2,1}','bin':50,'xmin':0.0,'xmax':1.0},
        'Jet1_tau32':{'name':'Jet1_trk02_tau32','title':'Jet1 #tau_{3,2}','bin':50,'xmin':0.0,'xmax':1.0},
        'Jet1_tau31':{'name':'Jet1_trk02_tau31','title':'Jet1 #tau_{3,1}','bin':50,'xmin':0.0,'xmax':1.0},

#        'Jet1_SD_Cor_pt':{'name':'Jet1_trk02_SD_Corr_pt','title':'Jet1 p_{T} (SD cor) [TeV]','bin':65,'xmin':2,'xmax':15, 'divide':1000},
#        'Jet1_SD_Cor_eta':{'name':'Jet1_trk02_SD_Corr_eta','title':'Jet1 #eta (SD cor)','bin':50,'xmin':-5.0,'xmax':5.0},
        'Jet1_trk02_SD_Cor_m':{'name':'Jet1_trk02_SD_Corr_m','title':'Jet1 trk02 mass (SD cor) [GeV]','bin':100,'xmin':0.0,'xmax':500},
        'Jet1_trk04_SD_Cor_m':{'name':'Jet1_trk04_SD_Corr_m','title':'Jet1 trk04 mass (SD cor) [GeV]','bin':100,'xmin':0.0,'xmax':500},
        'Jet1_trk08_SD_Cor_m':{'name':'Jet1_trk08_SD_Corr_m','title':'Jet1 trk08 mass (SD cor) [GeV]','bin':100,'xmin':0.0,'xmax':500},

        'Jet1_SD_Cor_MetCor_pt':{'name':'Jet1_trk02_SD_Corr_MetCorr_pt','title':'Jet1 p_{T} (SD cor) [TeV]','bin':50,'xmin':0.,'xmax':10., 'divide':1000},
        'Jet1_SD_Cor_MetCor_eta':{'name':'Jet1_trk02_SD_Corr_MetCorr_eta','title':'Jet1 #eta (SD cor)','bin':50,'xmin':-5.0,'xmax':5.0},
        'Jet1_SD_Cor_MetCor_m':{'name':'Jet1_trk02_SD_Corr_MetCorr_m','title':'Jet1 mass (SD cor) [GeV]','bin':100,'xmin':0.0,'xmax':500},

	'Jet2_tau21':{'name':'Jet2_trk02_tau21','title':'Jet2 #tau_{2,1}','bin':50,'xmin':0.0,'xmax':1.0},
        'Jet2_tau32':{'name':'Jet2_trk02_tau32','title':'Jet2 #tau_{3,2}','bin':50,'xmin':0.0,'xmax':1.0},
        'Jet2_tau31':{'name':'Jet2_trk02_tau31','title':'Jet2 #tau_{3,1}','bin':50,'xmin':0.0,'xmax':1.0},

#        'Jet2_SD_Cor_pt':{'name':'Jet2_trk02_SD_Corr_pt','title':'Jet2 p_{T} (SD cor) [TeV]','bin':65,'xmin':2,'xmax':15, 'divide':1000},
#        'Jet2_SD_Cor_eta':{'name':'Jet2_trk02_SD_Corr_eta','title':'Jet2 #eta (SD cor)','bin':50,'xmin':-5.0,'xmax':5.0},
        'Jet2_trk02_SD_Cor_m':{'name':'Jet2_trk02_SD_Corr_m','title':'Jet2 trk02 mass (SD cor) [GeV]','bin':100,'xmin':0.0,'xmax':500},
        'Jet2_trk04_SD_Cor_m':{'name':'Jet2_trk04_SD_Corr_m','title':'Jet2 trk04 mass (SD cor) [GeV]','bin':100,'xmin':0.0,'xmax':500},
        'Jet2_trk08_SD_Cor_m':{'name':'Jet2_trk08_SD_Corr_m','title':'Jet2 trk08 mass (SD cor) [GeV]','bin':100,'xmin':0.0,'xmax':500},

        'Jet2_SD_Cor_MetCor_pt':{'name':'Jet2_trk02_SD_Corr_MetCorr_pt','title':'Jet2 p_{T} (SD cor) [TeV]','bin':50,'xmin':0.,'xmax':10., 'divide':1000},
        'Jet2_SD_Cor_MetCor_eta':{'name':'Jet2_trk02_SD_Corr_MetCorr_eta','title':'Jet2 #eta (SD cor)','bin':50,'xmin':-5.0,'xmax':5.0},
        'Jet2_SD_Cor_MetCor_m':{'name':'Jet2_trk02_SD_Corr_MetCorr_m','title':'Jet2 mass (SD cor) [GeV]','bin':100,'xmin':0.0,'xmax':500},

        'rapiditySeparation':{'name':'rapiditySeparation_trk02','title':'Rapidity Separation','bin':50,'xmin':0.0,'xmax':10.0},
        'transverseMomentumAsymmetry':{'name':'transverseMomentumAsymmetry_trk02','title':'Transverse Momentum Asymmetry','bin':50,'xmin':0.0,'xmax':1.0},

#        'Mj1j2_trk02' :{'name':'Mj1j2_trk02','title':'m_{Z\'} [TeV] (trk02)','bin':125,'xmin':5.0,'xmax':30.0, 'divide':1000},
#        'Mj1j2_trk02_Corr' :{'name':'Mj1j2_trk02_Corr','title':'m_{Z\'} [TeV] (trk02 cor)','bin':125,'xmin':5.0,'xmax':30.0, 'divide':1000},
#        'Mj1j2_trk02_MetCorr' :{'name':'Mj1j2_trk02_MetCorr','title':'m_{Z\'} [TeV] (trk02 metcor)','bin':125,'xmin':5.0,'xmax':30.0, 'divide':1000},
#        'Mj1j2_trk02_Corr_MetCorr' :{'name':'Mj1j2_trk02_Corr_MetCorr','title':'m_{Z\'} [TeV] (trk02 corr metcor)','bin':125,'xmin':5.0,'xmax':30.0, 'divide':1000},

#        'Mj1j2_pf02' :{'name':'Mj1j2_pf02','title':'m_{Z\'} [TeV] (pf02)','bin':125,'xmin':5.0,'xmax':30.0, 'divide':1000},
#        'Mj1j2_pf02_MetCorr' :{'name':'Mj1j2_pf02_MetCorr','title':'m_{Z\'} [TeV] (pf02 metcor)','bin':125,'xmin':5.0,'xmax':30.0, 'divide':1000},

#        'Mj1j2_pf04' :{'name':'Mj1j2_pf04','title':'m_{Z\'} [TeV] (pf04)','bin':125,'xmin':5.0,'xmax':30.0, 'divide':1000},
 #       'Mj1j2_pf04_MetCorr' :{'name':'Mj1j2_pf04_MetCorr','title':'m_{Z\'} [TeV] (pf04 metcor)','bin':125,'xmin':5.0,'xmax':30.0, 'divide':1000},

#        'Mj1j2_pf08' :{'name':'Mj1j2_pf08','title':'m_{Z\'} [TeV] (pf08)','bin':125,'xmin':5.0,'xmax':30.0, 'divide':1000},
        'Mj1j2_pf08_MetCorr' :{'name':'Mj1j2_pf08_MetCorr','title':'m_{Z\'} [TeV] (pf08 metcor)','bin':100,'xmin':0.0,'xmax':20.0, 'divide':1000},

#        'Jet1_dR_lep' :{'name':'Jet1_trk02_dR_lep','title':'#DeltaR(l,j1) (trk02)','bin':50,'xmin':0,'xmax':5},
#        'Jet2_dR_lep' :{'name':'Jet2_trk02_dR_lep','title':'#DeltaR(l,j2) (trk02)','bin':50,'xmin':0,'xmax':5},
#        'BDTvariable_qcd' :{'name':'BDTvariable_qcd','title':'QCD BDT score','bin':100,'xmin':-0.5,'xmax':0.5},
        'Jet1_thad_vs_QCD_tagger' :{'name':'Jet1_thad_vs_QCD_tagger','title':'Jet1 top had. vs QCD tagger','bin':100,'xmin':-1.,'xmax':1.},
        'Jet2_thad_vs_QCD_tagger' :{'name':'Jet2_thad_vs_QCD_tagger','title':'Jet2 top had. vs QCD tagger','bin':100,'xmin':-1.,'xmax':1.},
        'weight_2tagex' :{'name':'weight_2tagex','title':'TRF 2b-tags exclusive weight','bin':100,'xmin':0.,'xmax':1.}
####################
## rebin for note ##
####################
#       'Mj1j2_pf08_MetCorr' :{'name':'Mj1j2_pf08_MetCorr','title':'m_{Z\'} [TeV] (pf08 metcor)','bin':25,'xmin':0.0,'xmax':20.0, 'divide':1000},
#       'Mj1j2_pf08_MetCorr_fit' :{'name':'Mj1j2_pf08_MetCorr_fit','title':'m_{Z\'} [TeV] (pf08 metcor)','bin':25,'xmin':0.0,'xmax':20.0, 'divide':1000},
#       'Jet1_tau21':{'name':'Jet1_trk02_tau21','title':'Jet1 #tau_{2,1}','bin':25,'xmin':0.0,'xmax':1.0},
#       'Jet1_tau32':{'name':'Jet1_trk02_tau32','title':'Jet1 #tau_{3,2}','bin':25,'xmin':0.0,'xmax':1.0},
#       'Jet1_trk02_SD_Cor_m':{'name':'Jet1_trk02_SD_Corr_m','title':'Jet1 trk02 mass (SD cor) [GeV]','bin':25,'xmin':0.0,'xmax':500},
#       'Jet2_tau21':{'name':'Jet2_trk02_tau21','title':'Jet2 #tau_{2,1}','bin':25,'xmin':0.0,'xmax':1.0},
#       'Jet2_tau32':{'name':'Jet2_trk02_tau32','title':'Jet2 #tau_{3,2}','bin':25,'xmin':0.0,'xmax':1.0},
#       'Jet2_trk02_SD_Cor_m':{'name':'Jet2_trk02_SD_Corr_m','title':'Jet2 trk02 mass (SD cor) [GeV]','bin':25,'xmin':0.0,'xmax':500},
#       'Jet1_thad_vs_QCD_tagger' :{'name':'Jet1_thad_vs_QCD_tagger','title':'Jet1 top had. vs QCD tagger','bin':25,'xmin':-1.,'xmax':1.},
#       'Jet2_thad_vs_QCD_tagger' :{'name':'Jet2_thad_vs_QCD_tagger','title':'Jet2 top had. vs QCD tagger','bin':25,'xmin':-1.,'xmax':1.},
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
#
colors['m_{Z_I} = 2 TeV']   = ROOT.kRed
colors['m_{Z_I} = 4 TeV']   = ROOT.kRed
colors['m_{Z_I} = 6 TeV']   = ROOT.kRed
colors['m_{Z_PSI} = 2 TeV'] = ROOT.kRed
colors['m_{Z_PSI} = 4 TeV'] = ROOT.kRed
colors['m_{Z_PSI} = 6 TeV'] = ROOT.kRed
colors['m_{Z_CHI} = 2 TeV'] = ROOT.kRed
colors['m_{Z_CHI} = 4 TeV'] = ROOT.kRed
colors['m_{Z_CHI} = 6 TeV'] = ROOT.kRed
colors['m_{Z_LRM} = 2 TeV'] = ROOT.kRed
colors['m_{Z_LRM} = 4 TeV'] = ROOT.kRed
colors['m_{Z_LRM} = 6 TeV'] = ROOT.kRed
colors['m_{Z_SSM} = 2 TeV'] = ROOT.kRed
colors['m_{Z_SSM} = 4 TeV'] = ROOT.kRed
colors['m_{Z_SSM} = 6 TeV'] = ROOT.kRed
colors['m_{Z_ETA} = 2 TeV'] = ROOT.kRed
colors['m_{Z_ETA} = 4 TeV'] = ROOT.kRed
colors['m_{Z_ETA} = 6 TeV'] = ROOT.kRed
#
colors['QCD'] = ROOT.kBlue+1
colors['tt']  = ROOT.kOrange-2
colors['vv']  = ROOT.kGreen+2
colors['vj']  = ROOT.kMagenta+2

signal_groups = collections.OrderedDict()
signal_groups['m_{Z} = 2 TeV']  = ['p8_pp_Zprime_2TeV_ttbar']
signal_groups['m_{Z} = 4 TeV']  = ['p8_pp_Zprime_4TeV_ttbar']
signal_groups['m_{Z} = 6 TeV']  = ['p8_pp_Zprime_6TeV_ttbar']
signal_groups['m_{Z} = 8 TeV']  = ['p8_pp_Zprime_8TeV_ttbar']
signal_groups['m_{Z} = 10 TeV'] = ['p8_pp_Zprime_10TeV_ttbar']
signal_groups['m_{Z} = 12 TeV'] = ['p8_pp_Zprime_12TeV_ttbar']
signal_groups['m_{Z} = 14 TeV'] = ['p8_pp_Zprime_14TeV_ttbar']
#
signal_groups['m_{Z_I} = 2 TeV']    = ['p8_pp_ZprimeI_2TeV_ttbar']
signal_groups['m_{Z_I} = 4 TeV']    = ['p8_pp_ZprimeI_4TeV_ttbar']
signal_groups['m_{Z_I} = 6 TeV']    = ['p8_pp_ZprimeI_6TeV_ttbar']
signal_groups['m_{Z_CHI} = 2 TeV']  = ['p8_pp_ZprimeCHI_2TeV_ttbar']
signal_groups['m_{Z_CHI} = 4 TeV']  = ['p8_pp_ZprimeCHI_4TeV_ttbar']
signal_groups['m_{Z_CHI} = 6 TeV']  = ['p8_pp_ZprimeCHI_6TeV_ttbar']
signal_groups['m_{Z_PSI} = 2 TeV']  = ['p8_pp_ZprimePSI_2TeV_ttbar']
signal_groups['m_{Z_PSI} = 4 TeV']  = ['p8_pp_ZprimePSI_4TeV_ttbar']
signal_groups['m_{Z_PSI} = 6 TeV']  = ['p8_pp_ZprimePSI_6TeV_ttbar']
signal_groups['m_{Z_LRM} = 2 TeV']  = ['p8_pp_ZprimeLRM_2TeV_ttbar']
signal_groups['m_{Z_LRM} = 4 TeV']  = ['p8_pp_ZprimeLRM_4TeV_ttbar']
signal_groups['m_{Z_LRM} = 6 TeV']  = ['p8_pp_ZprimeLRM_6TeV_ttbar']
signal_groups['m_{Z_SSM} = 2 TeV']  = ['p8_pp_ZprimeSSM_2TeV_ttbar']
signal_groups['m_{Z_SSM} = 4 TeV']  = ['p8_pp_ZprimeSSM_4TeV_ttbar']
signal_groups['m_{Z_SSM} = 6 TeV']  = ['p8_pp_ZprimeSSM_6TeV_ttbar']
signal_groups['m_{Z_ETA} = 2 TeV']  = ['p8_pp_ZprimeETA_2TeV_ttbar']
signal_groups['m_{Z_ETA} = 4 TeV']  = ['p8_pp_ZprimeETA_4TeV_ttbar']
signal_groups['m_{Z_ETA} = 6 TeV']  = ['p8_pp_ZprimeETA_6TeV_ttbar']
#
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
background_groups['QCD'] = [
'mgp8_pp_jj_5f_HT_500_1000',
'mgp8_pp_jj_5f_HT_1000_2000',
'mgp8_pp_jj_5f_HT_2000_5000',
'mgp8_pp_jj_5f_HT_5000_10000',
'mgp8_pp_jj_5f_HT_10000_27000']
background_groups['tt']  = [
'mgp8_pp_tt_5f_HT_500_1000',
'mgp8_pp_tt_5f_HT_1000_2000',
'mgp8_pp_tt_5f_HT_2000_5000',
'mgp8_pp_tt_5f_HT_5000_10000',
'mgp8_pp_tt_5f_HT_10000_27000']

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

#####################
# base pre-selections
#####################
selbase  = 'Jet1_trk02_SD_Corr_pt > 1000. && Jet2_trk02_SD_Corr_pt > 1000. && abs(Jet1_trk02_SD_Corr_eta) < 3. && abs(Jet1_trk02_SD_Corr_eta) < 3.'
# clean cuts
selbase += ' && Jet1_trk02_tau21>0 && Jet1_trk02_tau31>0 && Jet1_trk02_tau32>0 && Jet2_trk02_tau21>0 && Jet2_trk02_tau31>0 && Jet2_trk02_tau32>0'
# add extra free clean cut
selbase += ' && rapiditySeparation_trk02<2.4 && Mj1j2_pf08_MetCorr>2.0'

#####################
# CUT base selection
#####################
sel1c = selbase + '&& Jet1_trk02_tau32 < 0.7  && Jet1_trk02_SD_Corr_m > 100. && Jet1_trk02_tau21 < 0.7 &&  Jet1_trk02_tau21 > 0.3'
sel2c = sel1c + '&& Jet2_trk02_tau32 < 0.75 && Jet2_trk02_SD_Corr_m > 100. && Jet2_trk02_tau21 < 0.7 &&  Jet2_trk02_tau21 > 0.3'

#####################
# anti-QCD jet tagger selection
#####################
sel1t = selbase + ' && Jet1_thad_vs_QCD_tagger>0.15 &&  Jet2_thad_vs_QCD_tagger>0.15'
sel2t = sel1t   + ' && Jet1_trk02_SD_Corr_m>40. && Jet2_trk02_SD_Corr_m>40.'

#####################
# bTag selection
#####################
# direct btag
sel3c = sel2c + '&& Jet1_trk02_SD_Corr_MetCorr_pdgid ==5 && Jet2_trk02_SD_Corr_MetCorr_pdgid ==5 '
sel3t = sel2t + '&& Jet1_trk02_SD_Corr_MetCorr_pdgid ==5 && Jet2_trk02_SD_Corr_MetCorr_pdgid ==5 '
# apply 2 btag weight TRF
sel4c = 'weight_2tagex**' + sel2c
sel4t = 'weight_2tagex**' + sel2t

# add mass-dependent list of event #selections here if needed...

selections = collections.OrderedDict()

#selections['m_{Z} = 2 TeV'] = []
#selections['m_{Z} = 2 TeV'].append(selbase)
#selections['m_{Z} = 2 TeV'].append(sel1c)
#selections['m_{Z} = 2 TeV'].append(sel2c)
#selections['m_{Z} = 2 TeV'].append(sel1t)
#selections['m_{Z} = 2 TeV'].append(sel2t)
#selections['m_{Z} = 2 TeV'].append(sel3c)
#selections['m_{Z} = 2 TeV'].append(sel3t)
#selections['m_{Z} = 2 TeV'].append(sel4c)
#selections['m_{Z} = 2 TeV'].append(sel4t)
#
#selections['m_{Z} = 4 TeV'] = []
#selections['m_{Z} = 4 TeV'].append(selbase)
#selections['m_{Z} = 4 TeV'].append(sel1c)
#selections['m_{Z} = 4 TeV'].append(sel2c)
#selections['m_{Z} = 4 TeV'].append(sel1t)
#selections['m_{Z} = 4 TeV'].append(sel2t)
#selections['m_{Z} = 4 TeV'].append(sel3c)
#selections['m_{Z} = 4 TeV'].append(sel3t)
#selections['m_{Z} = 4 TeV'].append(sel4c)
#selections['m_{Z} = 4 TeV'].append(sel4t)
#
#selections['m_{Z} = 6 TeV'] = []
#selections['m_{Z} = 6 TeV'].append(selbase)
#selections['m_{Z} = 6 TeV'].append(sel1c)
#selections['m_{Z} = 6 TeV'].append(sel2c)
#selections['m_{Z} = 6 TeV'].append(sel1t)
#selections['m_{Z} = 6 TeV'].append(sel2t)
#selections['m_{Z} = 6 TeV'].append(sel3c)
#selections['m_{Z} = 6 TeV'].append(sel3t)
#selections['m_{Z} = 6 TeV'].append(sel4c)
#selections['m_{Z} = 6 TeV'].append(sel4t)
#
#selections['m_{Z} = 8 TeV'] = []
#selections['m_{Z} = 8 TeV'].append(selbase)
#selections['m_{Z} = 8 TeV'].append(sel1c)
#selections['m_{Z} = 8 TeV'].append(sel2c)
#selections['m_{Z} = 8 TeV'].append(sel1t)
#selections['m_{Z} = 8 TeV'].append(sel2t)
#selections['m_{Z} = 8 TeV'].append(sel3c)
#selections['m_{Z} = 8 TeV'].append(sel3t)
#selections['m_{Z} = 8 TeV'].append(sel4c)
#selections['m_{Z} = 8 TeV'].append(sel4t)
#
#selections['m_{Z} = 10 TeV'] = []
#selections['m_{Z} = 10 TeV'].append(selbase)
#selections['m_{Z} = 10 TeV'].append(sel1c)
#selections['m_{Z} = 10 TeV'].append(sel2c)
#selections['m_{Z} = 10 TeV'].append(sel1t)
#selections['m_{Z} = 10 TeV'].append(sel2t)
#selections['m_{Z} = 10 TeV'].append(sel3c)
#selections['m_{Z} = 10 TeV'].append(sel3t)
#selections['m_{Z} = 10 TeV'].append(sel4c)
#selections['m_{Z} = 10 TeV'].append(sel4t)
#
#selections['m_{Z} = 12 TeV'] = []
#selections['m_{Z} = 12 TeV'].append(selbase)
#selections['m_{Z} = 12 TeV'].append(sel1c)
#selections['m_{Z} = 12 TeV'].append(sel2c)
#selections['m_{Z} = 12 TeV'].append(sel1t)
#selections['m_{Z} = 12 TeV'].append(sel2t)
#selections['m_{Z} = 12 TeV'].append(sel3c)
#selections['m_{Z} = 12 TeV'].append(sel3t)
#selections['m_{Z} = 12 TeV'].append(sel4c)
#selections['m_{Z} = 12 TeV'].append(sel4t)
#
#selections['m_{Z} = 14 TeV'] = []
#selections['m_{Z} = 14 TeV'].append(selbase)
#selections['m_{Z} = 14 TeV'].append(sel1c)
#selections['m_{Z} = 14 TeV'].append(sel2c)
#selections['m_{Z} = 14 TeV'].append(sel1t)
#selections['m_{Z} = 14 TeV'].append(sel2t)
#selections['m_{Z} = 14 TeV'].append(sel3c)
#selections['m_{Z} = 14 TeV'].append(sel3t)
#selections['m_{Z} = 14 TeV'].append(sel4c)
#selections['m_{Z} = 14 TeV'].append(sel4t)

#################
selections['m_{Z_I} = 2 TeV'] = []
selections['m_{Z_I} = 2 TeV'].append(sel4t)
selections['m_{Z_I} = 4 TeV'] = []
selections['m_{Z_I} = 4 TeV'].append(sel4t)
selections['m_{Z_I} = 6 TeV'] = []
selections['m_{Z_I} = 6 TeV'].append(sel4t)

selections['m_{Z_PSI} = 2 TeV'] = []
selections['m_{Z_PSI} = 2 TeV'].append(sel4t)
selections['m_{Z_PSI} = 4 TeV'] = []
selections['m_{Z_PSI} = 4 TeV'].append(sel4t)
selections['m_{Z_PSI} = 6 TeV'] = []
selections['m_{Z_PSI} = 6 TeV'].append(sel4t)

selections['m_{Z_CHI} = 2 TeV'] = []
selections['m_{Z_CHI} = 2 TeV'].append(sel4t)
selections['m_{Z_CHI} = 4 TeV'] = []
selections['m_{Z_CHI} = 4 TeV'].append(sel4t)
selections['m_{Z_CHI} = 6 TeV'] = []
selections['m_{Z_CHI} = 6 TeV'].append(sel4t)

selections['m_{Z_LRM} = 2 TeV'] = []
selections['m_{Z_LRM} = 2 TeV'].append(sel4t)
selections['m_{Z_LRM} = 4 TeV'] = []
selections['m_{Z_LRM} = 4 TeV'].append(sel4t)
selections['m_{Z_LRM} = 6 TeV'] = []
selections['m_{Z_LRM} = 6 TeV'].append(sel4t)

selections['m_{Z_SSM} = 2 TeV'] = []
selections['m_{Z_SSM} = 2 TeV'].append(sel4t)
selections['m_{Z_SSM} = 4 TeV'] = []
selections['m_{Z_SSM} = 4 TeV'].append(sel4t)
selections['m_{Z_SSM} = 6 TeV'] = []
selections['m_{Z_SSM} = 6 TeV'].append(sel4t)

selections['m_{Z_ETA} = 2 TeV'] = []
selections['m_{Z_ETA} = 2 TeV'].append(sel4t)
selections['m_{Z_ETA} = 4 TeV'] = []
selections['m_{Z_ETA} = 4 TeV'].append(sel4t)
selections['m_{Z_ETA} = 6 TeV'] = []
selections['m_{Z_ETA} = 6 TeV'].append(sel4t)

