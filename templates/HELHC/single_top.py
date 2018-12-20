import ROOT
import collections

### variable list
variables = {
	'Jet1_tau21':{'name':'Jet1_trk02_tau21','title':'Jet1 #tau_{2,1}','bin':50,'xmin':0.0,'xmax':1.0},
        'Jet1_tau32':{'name':'Jet1_trk02_tau32','title':'Jet1 #tau_{3,2}','bin':50,'xmin':0.0,'xmax':1.0},
        'Jet1_tau31':{'name':'Jet1_trk02_tau31','title':'Jet1 #tau_{3,1}','bin':50,'xmin':0.0,'xmax':1.0},

        'Jet1_trk02_SD_Corr_pt':{'name':'Jet1_trk02_SD_Corr_pt','title':'Jet1 p_{T} (SD cor) [TeV]','bin':50,'xmin':0,'xmax':10, 'divide':1000},
        'Jet1_trk02_SD_Corr_eta':{'name':'Jet1_trk02_SD_Corr_eta','title':'Jet1 #eta (SD cor)','bin':50,'xmin':-5.0,'xmax':5.0},
        'Jet1_trk02_SD_Cor_m':{'name':'Jet1_trk02_SD_Corr_m','title':'Jet1 trk02 mass (SD cor) [GeV]','bin':100,'xmin':0.0,'xmax':500},
        'Jet1_trk04_SD_Cor_m':{'name':'Jet1_trk04_SD_Corr_m','title':'Jet1 trk04 mass (SD cor) [GeV]','bin':100,'xmin':0.0,'xmax':500},
        'Jet1_trk08_SD_Cor_m':{'name':'Jet1_trk08_SD_Corr_m','title':'Jet1 trk08 mass (SD cor) [GeV]','bin':100,'xmin':0.0,'xmax':500},

        'Jet1_SD_Cor_MetCor_pt':{'name':'Jet1_trk02_SD_Corr_MetCorr_pt','title':'Jet1 p_{T} (SD cor) [TeV]','bin':50,'xmin':0.,'xmax':10., 'divide':1000},
        'Jet1_SD_Cor_MetCor_eta':{'name':'Jet1_trk02_SD_Corr_MetCorr_eta','title':'Jet1 #eta (SD cor)','bin':50,'xmin':-5.0,'xmax':5.0},
        'Jet1_SD_Cor_MetCor_m':{'name':'Jet1_trk02_SD_Corr_MetCorr_m','title':'Jet1 mass (SD cor) [GeV]','bin':100,'xmin':0.0,'xmax':500},

	'Jet2_tau21':{'name':'Jet2_trk02_tau21','title':'Jet2 #tau_{2,1}','bin':50,'xmin':0.0,'xmax':1.0},
        'Jet2_tau32':{'name':'Jet2_trk02_tau32','title':'Jet2 #tau_{3,2}','bin':50,'xmin':0.0,'xmax':1.0},
        'Jet2_tau31':{'name':'Jet2_trk02_tau31','title':'Jet2 #tau_{3,1}','bin':50,'xmin':0.0,'xmax':1.0},

        'Jet2_trk02_SD_Corr_pt':{'name':'Jet2_trk02_SD_Corr_pt','title':'Jet2 p_{T} (SD cor) [TeV]','bin':50,'xmin':0,'xmax':10, 'divide':1000},
        'Jet2_trk02_SD_Corr_eta':{'name':'Jet2_trk02_SD_Corr_eta','title':'Jet2 #eta (SD cor)','bin':50,'xmin':-5.0,'xmax':5.0},
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
        # rebin 2
        #'Mj1j2_pf08_MetCorr' :{'name':'Mj1j2_pf08_MetCorr','title':'m_{W^{*}} [TeV] (pf08 metcor)','bin':50,'xmin':0.0,'xmax':20.0, 'divide':1000},

#        'Jet1_dR_lep' :{'name':'Jet1_trk02_dR_lep','title':'#DeltaR(l,j1) (trk02)','bin':50,'xmin':0,'xmax':5},
#        'Jet2_dR_lep' :{'name':'Jet2_trk02_dR_lep','title':'#DeltaR(l,j2) (trk02)','bin':50,'xmin':0,'xmax':5},
#        'BDTvariable_qcd' :{'name':'BDTvariable_qcd','title':'QCD BDT score','bin':100,'xmin':-0.5,'xmax':0.5},
        'Jet1_thad_vs_QCD_tagger' :{'name':'Jet1_thad_vs_QCD_tagger','title':'Jet1 top had. vs QCD tagger','bin':50,'xmin':-1.,'xmax':1.},
        'Jet2_thad_vs_QCD_tagger' :{'name':'Jet2_thad_vs_QCD_tagger','title':'Jet2 top had. vs QCD tagger','bin':50,'xmin':-1.,'xmax':1.},
        #'weight_2tagex' :{'name':'weight_2tagex','title':'TRF 2b-tags exclusive weight','bin':100,'xmin':0.,'xmax':1.}
        'Jet1_trk02_dR_Jet2_trk02' :{'name':'Jet1_trk02_dR_Jet2_trk02','title':'#DeltaR(j1,j2) (trk02)','bin':50,'xmin':0,'xmax':5},

}

variables2D = {}


colors = {}
colors['single top']  = ROOT.kRed
#
colors['QCD'] = ROOT.kBlue+1
colors['tt']  = ROOT.kOrange-2
colors['vv']  = ROOT.kGreen+2
colors['vj']  = ROOT.kMagenta+2
colors['Wt']  = ROOT.kAzure+1

signal_groups = collections.OrderedDict()
signal_groups['single top']  = ['mgp8_pp_tj_5f']
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
background_groups['Wt']  = ['mgp8_pp_tvj_5f']
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
runFull = True

HELHC=True

#####################
# base pre-selections
#####################
# clean cuts
selbase = 'Jet1_trk02_tau21>0 && Jet1_trk02_tau31>0 && Jet1_trk02_tau32>0 && Jet2_trk02_tau21>0 && Jet2_trk02_tau31>0 && Jet2_trk02_tau32>0'
# add extra free clean cut
selbase += ' && rapiditySeparation_trk02<2.4'
# dR(t,b)>>0 (works in all channels)
selbase += ' && (Jet1_trk02_dR_Jet2_trk02>2.9 && Jet1_trk02_dR_Jet2_trk02<3.6)'

#####################
# toptag definition
#####################
# -->  optmized with signal on all regions
anti_toptagJet1_had = ' && Jet1_thad_vs_QCD_tagger<-0.1'
anti_toptagJet2_had = ' && Jet2_thad_vs_QCD_tagger<-0.1'
# --> keep same OP as Zptt
toptagJet1_had = 'Jet1_thad_vs_QCD_tagger>0.15' + anti_toptagJet2_had
toptagJet2_had = 'Jet2_thad_vs_QCD_tagger>0.15' + anti_toptagJet1_had
# --> pTlep/pTjet>15% to exclude semi-lep decay lepton in computing lepclose
toptagJet1_lep = 'Jet1_lepclose==1' + anti_toptagJet2_had
toptagJet2_lep = 'Jet2_lepclose==1' + anti_toptagJet1_had

#####################
# s-channel
#####################
# had -> 2 hight pT jets + 2 btags + 1 top tag had + no iso lepton
# lep -> 2 hight pT jets + 2 btags + 1 lepton close [top tag lep]

# 2 hight pT jets (relaxed from 1 TeV to 0.8 TeV to save some signal)
#-----------------
selschan_base  = selbase + ' && Jet1_trk02_SD_Corr_pt > 800. && Jet2_trk02_SD_Corr_pt > 800. && abs(Jet1_trk02_SD_Corr_eta) < 3. && abs(Jet1_trk02_SD_Corr_eta) < 3.'
# + dR(t,b)>>0
#selschan_base += '  && (Jet1_trk02_dR_Jet2_trk02>2.9 && Jet1_trk02_dR_Jet2_trk02<3.6)'

# 2 btags
#-----------------
#selschan_2btag = selschan_base + ' && Jet1_trk02_SD_Corr_MetCorr_pdgid==5 && Jet2_trk02_SD_Corr_MetCorr_pdgid==5'
selschan_2btag = 'weight_2tagex**' + selschan_base

#####################
# 1 top tagger had
#-----------------
selschan_1tophad = selschan_2btag + ' && ( (' + toptagJet1_had + ') || (' + toptagJet2_had + ') )'
selschan_1tophad += ' && lepton_iso==0'
#
selschan_1tophad_jet1 = selschan_2btag + ' && ' + toptagJet1_had
selschan_1tophad_jet1 += ' && lepton_iso==0'
selschan_1tophad_jet2 = selschan_2btag + ' && ' + toptagJet2_had
selschan_1tophad_jet2 += ' && lepton_iso==0'

#####################
# 1 top tag lep
#-----------------
selschan_1toplep = selschan_2btag + ' && ( (' + toptagJet1_lep + ') || (' + toptagJet2_lep + ') )'
#
selschan_1toplep_jet1 = selschan_2btag + ' && ' + toptagJet1_lep
selschan_1toplep_jet2 = selschan_2btag + ' && ' + toptagJet2_lep 

#####################
# t-channel
#####################
# had -> >=1 hight pT jet + 1 (btag + top tag had) + no iso lepton
# lep -> >=1 hight pT jet + 1 (btag + top tag lep [=lepton close])
# -> 1 btag jet TRF for Jet1 or Jet2 separately handled separately in selections -> merged in fit

# >= 1 hight pT jets
#-----------------
seltchan_base  = selbase + ' && Jet1_trk02_SD_Corr_pt > 800. && abs(Jet1_trk02_SD_Corr_eta) < 3. && abs(Jet1_trk02_SD_Corr_eta) < 3.'

#####################
# Jet1 top tag had + btag
#-----------------
seltchan_1tophad_1btag_jet1 = seltchan_base + ' && ' + toptagJet1_had + ' && Jet1_trk02_SD_Corr_MetCorr_pdgid==5 && Jet2_trk02_SD_Corr_MetCorr_pdgid!=5'
seltchan_1tophad_1btag_jet1 += ' && lepton_iso==0'
#
seltchan_1tophad_1btagtrf_jet1 = 'weight_1tagexJet1**' + seltchan_base + ' && ' + toptagJet1_had
seltchan_1tophad_1btagtrf_jet1 += ' && lepton_iso==0'

# Jet2 top tag had + btag
#-----------------
seltchan_1tophad_1btag_jet2 = seltchan_base + ' && ' + toptagJet2_had + ' && Jet1_trk02_SD_Corr_MetCorr_pdgid!=5 && Jet2_trk02_SD_Corr_MetCorr_pdgid==5'
seltchan_1tophad_1btag_jet2 += ' && lepton_iso==0'
#
seltchan_1tophad_1btagtrf_jet2 = 'weight_1tagexJet2**' + seltchan_base + ' && ' + toptagJet2_had
seltchan_1tophad_1btagtrf_jet2 += ' && lepton_iso==0'

#####################
# Jet1 top tag lep + btag
#-----------------
seltchan_1toplep_1btag_jet1 = seltchan_base + ' && ' + toptagJet1_lep + ' && Jet1_trk02_SD_Corr_MetCorr_pdgid==5 && Jet2_trk02_SD_Corr_MetCorr_pdgid!=5'
seltchan_1toplep_1btagtrf_jet1 = 'weight_1tagexJet1**' + seltchan_base + ' && ' + toptagJet1_lep

# Jet2 top tag lep + btag
#-----------------
seltchan_1toplep_1btag_jet2 = seltchan_base + ' && ' + toptagJet2_lep + ' && Jet1_trk02_SD_Corr_MetCorr_pdgid!=5 && Jet2_trk02_SD_Corr_MetCorr_pdgid==5'
seltchan_1toplep_1btagtrf_jet2 = 'weight_1tagexJet2**' + seltchan_base + ' && ' + toptagJet2_lep

# tmp direct tag handled in 1 sel
#seltchan_1tophad_1btag = '(' + seltchan_1tophad_1btag_jet1 + ') || (' +  seltchan_1tophad_1btag_jet2 + ')'
#seltchan_1toplep_1btag = '(' + seltchan_1toplep_1btag_jet1 + ') || (' +  seltchan_1toplep_1btag_jet2 + ')'

selections = collections.OrderedDict()

selections['single top'] = []
#selections['single top'].append(selbase)
#selections['single top'].append(selschan_base)
#selections['single top'].append(selschan_2btag)
#selections['single top'].append(selschan_1tophad)
#selections['single top'].append(selschan_1toplep)
selections['single top'].append(selschan_1tophad_jet1)
selections['single top'].append(selschan_1tophad_jet2)
selections['single top'].append(selschan_1toplep_jet1)
selections['single top'].append(selschan_1toplep_jet2)
#selections['single top'].append(seltchan_base)
##selections['single top'].append(seltchan_1tophad_1btag_jet1)
##selections['single top'].append(seltchan_1tophad_1btag_jet2)
##selections['single top'].append(seltchan_1tophad_1btag)
selections['single top'].append(seltchan_1tophad_1btagtrf_jet1)
selections['single top'].append(seltchan_1tophad_1btagtrf_jet2)
##selections['single top'].append(seltchan_1toplep_1btag_jet1)
##selections['single top'].append(seltchan_1toplep_1btag_jet2)
##selections['single top'].append(seltchan_1toplep_1btag)
selections['single top'].append(seltchan_1toplep_1btagtrf_jet1)
selections['single top'].append(seltchan_1toplep_1btagtrf_jet2)

