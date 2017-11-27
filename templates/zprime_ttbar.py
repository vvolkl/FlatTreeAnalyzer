import ROOT
import collections

### variable list
variables = {
	'Jet1_tau21':{'name':'Jet1_tau21','title':'#tau_{2,1}','bin':50,'xmin':0.0,'xmax':1.0},
        'Jet1_tau32':{'name':'Jet1_tau32','title':'#tau_{3,2}','bin':50,'xmin':0.0,'xmax':1.0},
        'Jet1_tau31':{'name':'Jet1_tau31','title':'#tau_{3,1}','bin':50,'xmin':0.0,'xmax':1.0},

        'softDroppedJet1_pt':{'name':'softDroppedJet1_pt','title':'Leading jet (soft dropped) p_{T}','bin':50,'xmin':0.0,'xmax':20000},
        'softDroppedJet1_eta':{'name':'softDroppedJet1_eta','title':'Leading jet (soft dropped) eta','bin':50,'xmin':-5.0,'xmax':5.0},
        'softDroppedJet1_m':{'name':'softDroppedJet1_m','title':'Leading jet (soft dropped) mass','bin':50,'xmin':0.0,'xmax':1000},

	'Jet2_tau21':{'name':'Jet2_tau21','title':'#tau_{2,1}','bin':50,'xmin':0.0,'xmax':1.0},
        'Jet2_tau32':{'name':'Jet2_tau32','title':'#tau_{3,2}','bin':50,'xmin':0.0,'xmax':1.0},
        'Jet2_tau31':{'name':'Jet2_tau31','title':'#tau_{3,1}','bin':50,'xmin':0.0,'xmax':1.0},

        'Jet2_pt':{'name':'Jet2_pt','title':'Leading jet (ungroomed) p_{T}','bin':50,'xmin':0.0,'xmax':20000},
        'Jet2_eta':{'name':'Jet2_eta','title':'Leading jet (ungroomed) eta','bin':50,'xmin':-2.5,'xmax':2.5},
        'Jet2_m':{'name':'Jet2_m','title':'Leading jet (ungroomed) mass','bin':50,'xmin':0.0,'xmax':1000},

        'softDroppedJet2_pt':{'name':'softDroppedJet2_pt','title':'Leading jet (soft dropped) p_{T}','bin':50,'xmin':0.0,'xmax':20000},
        'softDroppedJet2_eta':{'name':'softDroppedJet2_eta','title':'Leading jet (soft dropped) eta','bin':50,'xmin':-2.5,'xmax':2.5},
        'softDroppedJet2_m':{'name':'softDroppedJet2_m','title':'Leading jet (soft dropped) mass','bin':50,'xmin':0.0,'xmax':1000},

        'zPrimeReconstructedMass':{'name':'zPrimeReconstructedMass','title':'Zprime Reconstructed Mass (Ungroomed)','bin':50,'xmin':5000.0,'xmax':25000.0},

        'rapiditySeparation':{'name':'rapiditySeparation','title':'Rapidity Separation','bin':50,'xmin':0.0,'xmax':10.0},
        'transverseMomentumAsymmetry':{'name':'transverseMomentumAsymmetry','title':'Transverse Momentum Asymmetry','bin':50,'xmin':0.0,'xmax':1.0},

	'topJetMassDifference':{'name':'topJetMassDifference','title':'Top Jet Mass Difference','bin':50,'xmin':0.0,'xmax':1000},
	'Jet3_pt':{'name':'Jet3_pt','title':'Third Jet p_{T}','bin':50,'xmin':0.0,'xmax':1000},

	'BDTvariable_qcd':{'name':'BDTvariable_qcd','title':'BDT Variable QCD','bin':50,'xmin':-0.5,'xmax':0.5},
#	'BDTvariable_ttbar':{'name':'BDTvariable_ttbar','title':'BDT Variable ttbar','bin':50,'xmin':-0.5,'xmax':0.5},
}

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
colors['QCD'] = ROOT.kYellow
colors['tt'] = ROOT.kRed
colors['vv'] = ROOT.kOrange

signal_groups = collections.OrderedDict()
signal_groups['m_{Z} = 2 TeV'] = ['pp_Zprime_2TeV_ttbar']
signal_groups['m_{Z} = 5 TeV'] = ['pp_Zprime_5TeV_ttbar']
signal_groups['m_{Z} = 10 TeV'] = ['pp_Zprime_10TeV_ttbar']
signal_groups['m_{Z} = 15 TeV'] = ['pp_Zprime_15TeV_ttbar']
signal_groups['m_{Z} = 20 TeV'] = ['pp_Zprime_20TeV_ttbar']
signal_groups['m_{Z} = 25 TeV'] = ['pp_Zprime_25TeV_ttbar']
signal_groups['m_{Z} = 30 TeV'] = ['pp_Zprime_30TeV_ttbar']
signal_groups['m_{Z} = 35 TeV'] = ['pp_Zprime_35TeV_ttbar']
signal_groups['m_{Z} = 40 TeV'] = ['pp_Zprime_40TeV_ttbar']

background_groups = collections.OrderedDict()

background_groups['vv']  = [
				'pp_vv_M_5000_10000',
                                'pp_vv_M_10000_15000',
                                'pp_vv_M_15000_100000',
		           ] 

background_groups['tt']  = [
				'pp_tt_M_5000_10000',
				'pp_tt_M_10000_15000',
				'pp_tt_M_15000_100000',
			   ]

background_groups['QCD'] = [
                                'pp_jj_M_5000_10000',
                                'pp_jj_M_10000_15000',
                                'pp_jj_M_15000_100000',
                           ]

# global parameters
intLumi = 1.0e+07
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
selbase = 'Jet1_pt > 3000. && Jet2_pt > 3000. && abs(Jet1_eta) < 3. && abs(Jet2_eta) < 3.'
sel = selbase + '&& Jet1_tau32 < 0.7 && Jet2_tau32 < 0.7 && softDroppedJet1_m > 140. && softDroppedJet2_m > 140.'

# add mass-dependent list of event #selections here if needed...

selections = collections.OrderedDict()
selections['m_{Z} = 10 TeV'] = []
selections['m_{Z} = 10 TeV'].append(selbase)
selections['m_{Z} = 10 TeV'].append(sel)


'''selections['m_{Z} = 15 TeV'] = []
selections['m_{Z} = 15 TeV'].append(selbase)
selections['m_{Z} = 20 TeV'] = []
selections['m_{Z} = 20 TeV'].append(selbase)
selections['m_{Z} = 25 TeV'] = []
selections['m_{Z} = 25 TeV'].append(selbase)
selections['m_{Z} = 30 TeV'] = []
selections['m_{Z} = 30 TeV'].append(selbase)'''


