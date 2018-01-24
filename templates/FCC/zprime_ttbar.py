import ROOT
import collections

### variable list
variables = {
	'Jet1_tau21':{'name':'Jet1_trk02_tau21','title':'Jet1 #tau_{2,1}','bin':50,'xmin':0.0,'xmax':1.0},
        'Jet1_tau32':{'name':'Jet1_trk02_tau32','title':'Jet1 #tau_{3,2}','bin':50,'xmin':0.0,'xmax':1.0},
        'Jet1_tau31':{'name':'Jet1_trk02_tau31','title':'Jet1 #tau_{3,1}','bin':50,'xmin':0.0,'xmax':1.0},

        'Jet1_SD_Cor_pt':{'name':'Jet1_trk02_SD_Corr_pt','title':'Jet1 p_{T} (SD cor) [TeV]','bin':65,'xmin':2,'xmax':15, 'divide':1000},
        'Jet1_SD_Cor_eta':{'name':'Jet1_trk02_SD_Corr_eta','title':'Jet1 #eta (SD cor)','bin':50,'xmin':-5.0,'xmax':5.0},
        'Jet1_SD_Cor_m':{'name':'Jet1_trk02_SD_Corr_m','title':'Jet1 mass (SD cor) [GeV]','bin':100,'xmin':0.0,'xmax':500},

        'Jet1_SD_Cor_MetCor_pt':{'name':'Jet1_trk02_SD_Corr_MetCorr_pt','title':'Jet1 p_{T} (SD cor) [TeV]','bin':65,'xmin':0.0,'xmax':15, 'divide':1000},
        'Jet1_SD_Cor_MetCor_eta':{'name':'Jet1_trk02_SD_Corr_MetCorr_eta','title':'Jet1 #eta (SD cor)','bin':50,'xmin':-5.0,'xmax':5.0},
        'Jet1_SD_Cor_MetCor_m':{'name':'Jet1_trk02_SD_Corr_MetCorr_m','title':'Jet1 mass (SD cor) [GeV]','bin':100,'xmin':0.0,'xmax':500},

	'Jet2_tau21':{'name':'Jet2_trk02_tau21','title':'Jet2 #tau_{2,1}','bin':50,'xmin':0.0,'xmax':1.0},
        'Jet2_tau32':{'name':'Jet2_trk02_tau32','title':'Jet2 #tau_{3,2}','bin':50,'xmin':0.0,'xmax':1.0},
        'Jet2_tau31':{'name':'Jet2_trk02_tau31','title':'Jet2 #tau_{3,1}','bin':50,'xmin':0.0,'xmax':1.0},

        'Jet2_SD_Cor_pt':{'name':'Jet2_trk02_SD_Corr_pt','title':'Jet2 p_{T} (SD cor) [TeV]','bin':65,'xmin':2,'xmax':15, 'divide':1000},
        'Jet2_SD_Cor_eta':{'name':'Jet2_trk02_SD_Corr_eta','title':'Jet2 #eta (SD cor)','bin':50,'xmin':-5.0,'xmax':5.0},
        'Jet2_SD_Cor_m':{'name':'Jet2_trk02_SD_Corr_m','title':'Jet2 mass (SD cor) [GeV]','bin':100,'xmin':0.0,'xmax':500},

        'Jet2_SD_Cor_MetCor_pt':{'name':'Jet2_trk02_SD_Corr_MetCorr_pt','title':'Jet2 p_{T} (SD cor) [TeV]','bin':65,'xmin':2,'xmax':15, 'divide':1000},
        'Jet2_SD_Cor_MetCor_eta':{'name':'Jet2_trk02_SD_Corr_MetCorr_eta','title':'Jet2 #eta (SD cor)','bin':50,'xmin':-5.0,'xmax':5.0},
        'Jet2_SD_Cor_MetCor_m':{'name':'Jet2_trk02_SD_Corr_MetCorr_m','title':'Jet2 mass (SD cor) [GeV]','bin':100,'xmin':0.0,'xmax':500},

        'rapiditySeparation':{'name':'rapiditySeparation_trk02','title':'Rapidity Separation','bin':50,'xmin':0.0,'xmax':10.0},
        'transverseMomentumAsymmetry':{'name':'transverseMomentumAsymmetry_trk02','title':'Transverse Momentum Asymmetry','bin':50,'xmin':0.0,'xmax':1.0},

        'Mj1j2_trk02' :{'name':'Mj1j2_trk02','title':'m_{Z\'} [TeV] (trk02)','bin':125,'xmin':5.0,'xmax':30.0, 'divide':1000},
        'Mj1j2_trk02_Corr' :{'name':'Mj1j2_trk02_Corr','title':'m_{Z\'} [TeV] (trk02 cor)','bin':125,'xmin':5.0,'xmax':30.0, 'divide':1000},
        'Mj1j2_trk02_MetCorr' :{'name':'Mj1j2_trk02_MetCorr','title':'m_{Z\'} [TeV] (trk02 metcor)','bin':125,'xmin':5.0,'xmax':30.0, 'divide':1000},
        'Mj1j2_trk02_Corr_MetCorr' :{'name':'Mj1j2_trk02_Corr_MetCorr','title':'m_{Z\'} [TeV] (trk02 corr metcor)','bin':125,'xmin':5.0,'xmax':30.0, 'divide':1000},

        'Mj1j2_pf02' :{'name':'Mj1j2_pf02','title':'m_{Z\'} [TeV] (pf02)','bin':125,'xmin':5.0,'xmax':30.0, 'divide':1000},
        'Mj1j2_pf02_MetCorr' :{'name':'Mj1j2_pf02_MetCorr','title':'m_{Z\'} [TeV] (pf02 metcor)','bin':125,'xmin':5.0,'xmax':30.0, 'divide':1000},

        'Mj1j2_pf04' :{'name':'Mj1j2_pf04','title':'m_{Z\'} [TeV] (pf04)','bin':125,'xmin':5.0,'xmax':30.0, 'divide':1000},
        'Mj1j2_pf04_MetCorr' :{'name':'Mj1j2_pf04_MetCorr','title':'m_{Z\'} [TeV] (pf04 metcor)','bin':125,'xmin':5.0,'xmax':30.0, 'divide':1000},

        'Mj1j2_pf08' :{'name':'Mj1j2_pf08','title':'m_{Z\'} [TeV] (pf08)','bin':125,'xmin':5.0,'xmax':30.0, 'divide':1000},
        'Mj1j2_pf08_MetCorr' :{'name':'Mj1j2_pf08_MetCorr','title':'m_{Z\'} [TeV] (pf08 metcor)','bin':125,'xmin':5.0,'xmax':30.0, 'divide':1000},

        'Jet1_dR_lep' :{'name':'Jet1_trk02_dR_lep','title':'#DeltaR(l,j1) (trk02)','bin':50,'xmin':0,'xmax':5},
        'Jet2_dR_lep' :{'name':'Jet2_trk02_dR_lep','title':'#DeltaR(l,j2) (trk02)','bin':50,'xmin':0,'xmax':5},
}

variables2D = {}


colors = {}
colors['m_{Z} = 2 TeV'] = ROOT.kBlue
colors['m_{Z} = 5 TeV'] = ROOT.kBlue
colors['m_{Z} = 10 TeV'] = ROOT.kBlue
colors['m_{Z} = 15 TeV'] = ROOT.kBlue
colors['m_{Z} = 20 TeV'] = ROOT.kBlue
colors['m_{Z} = 25 TeV'] = ROOT.kBlue
colors['m_{Z} = 30 TeV'] = ROOT.kBlue
colors['m_{Z} = 35 TeV'] = ROOT.kBlue
colors['m_{Z} = 40 TeV'] = ROOT.kBlue
colors['QCD'] = ROOT.kGreen
colors['tt'] = ROOT.kRed
colors['vv'] = ROOT.kOrange
colors['vj'] = ROOT.kBlack

signal_groups = collections.OrderedDict()
#signal_groups['m_{Z} = 2 TeV'] = ['pp_Zprime_2TeV_ttbar']
#signal_groups['m_{Z} = 5 TeV'] = ['pp_Zprime_5TeV_ttbar']
signal_groups['m_{Z} = 10 TeV'] = ['pp_Zprime_10TeV_ttbar']
signal_groups['m_{Z} = 15 TeV'] = ['pp_Zprime_15TeV_ttbar']
signal_groups['m_{Z} = 20 TeV'] = ['pp_Zprime_20TeV_ttbar']
signal_groups['m_{Z} = 25 TeV'] = ['pp_Zprime_25TeV_ttbar']
signal_groups['m_{Z} = 30 TeV'] = ['pp_Zprime_30TeV_ttbar']
#signal_groups['m_{Z} = 35 TeV'] = ['pp_Zprime_35TeV_ttbar']
#signal_groups['m_{Z} = 40 TeV'] = ['pp_Zprime_40TeV_ttbar']

background_groups = collections.OrderedDict()

background_groups['vv']  = ['pp_vv_lo'] 
background_groups['vj'] = ['pp_vj_4f_M_5000_inf']
background_groups['tt']  = ['pp_tt_lo']
background_groups['QCD'] = ['pp_jj_lo']



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

# base pre-#selections
#selbase = 'Jet1_pt > 2800. && Jet2_pt > 2800. && abs(Jet1_eta) < 3. && abs(Jet2_eta) < 3. && BDTvariable_qcd > 0.2'
selbase = 'Jet1_trk02_SD_Corr_pt > 3000. && Jet2_trk02_SD_Corr_pt > 3000. && abs(Jet1_trk02_SD_Corr_eta) < 3. && abs(Jet1_trk02_SD_Corr_eta) < 3.'
sel1 = selbase + '&& Jet1_trk02_tau32 < 0.7  && Jet1_trk02_SD_Corr_m > 100. && Jet1_trk02_tau21 < 0.7 &&  Jet1_trk02_tau21 > 0.3'
sel2 = sel1 +    '&& Jet2_trk02_tau32 < 0.75 && Jet2_trk02_SD_Corr_m > 100. && Jet2_trk02_tau21 < 0.7 &&  Jet2_trk02_tau21 > 0.3'
sel3 = sel2 +    '&&(Jet1_trk02_SD_Corr_MetCorr_pdgid ==5 || Jet2_trk02_SD_Corr_MetCorr_pdgid ==5) '
sel4 = sel2 +    '&& Jet1_trk02_SD_Corr_MetCorr_pdgid ==5 && Jet2_trk02_SD_Corr_MetCorr_pdgid ==5 '

# add mass-dependent list of event #selections here if needed...

selections = collections.OrderedDict()
selections['m_{Z} = 10 TeV'] = []
#selections['m_{Z} = 10 TeV'].append(selbase)
#selections['m_{Z} = 10 TeV'].append(sel1)
selections['m_{Z} = 10 TeV'].append(selbase)
selections['m_{Z} = 10 TeV'].append(sel1)
selections['m_{Z} = 10 TeV'].append(sel2)
selections['m_{Z} = 10 TeV'].append(sel3)
selections['m_{Z} = 10 TeV'].append(sel4)

#selections['m_{Z} = 15 TeV'] = []
#selections['m_{Z} = 15 TeV'].append(sel3)
#selections['m_{Z} = 15 TeV'].append(sel4)

#selections['m_{Z} = 20 TeV'] = []
#selections['m_{Z} = 20 TeV'].append(sel3)
#selections['m_{Z} = 20 TeV'].append(sel4)

#selections['m_{Z} = 25 TeV'] = []
#selections['m_{Z} = 25 TeV'].append(sel3)
#selections['m_{Z} = 25 TeV'].append(sel4)

#selections['m_{Z} = 30 TeV'] = []
#selections['m_{Z} = 30 TeV'].append(sel3)
#selections['m_{Z} = 30 TeV'].append(sel4)





