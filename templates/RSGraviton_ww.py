import ROOT
import collections

### variable list
variables = {
    'RSGravitonReconstructedMass':{'name':'RSGravitonReconstructedMass','title':'RSG Reconstructed Mass (Ungroomed)','bin':50,'xmin':0.0,'xmax':50000.0},
    'RSGravitonReconstructedMass_softDropped':{'name':'RSGravitonReconstructedMass_softDropped','title':'RSG Reconstructed Mass (SoftDropped)','bin':50,'xmin':0.0,'xmax':50000.0},
    'softDroppedJet1_m':{'name':'softDroppedJet1_m','title':'Soft Dropped Mass','bin':50,'xmin':0.0,'xmax':1000.0},
    'softDroppedJet2_m':{'name':'softDroppedJet2_m','title':'Soft Dropped Mass Jet2','bin':50,'xmin':0.0,'xmax':1000.0},
#    'trimmedJet1_m':{'name':'trimmedJet1_m','title':'Trimmed Mass','bin':50,'xmin':0.0,'xmax':150.0},
#    'trimmedJet2_m':{'name':'trimmedJet2_m','title':'Trimmed Mass Jet2','bin':50,'xmin':0.0,'xmax':1000.0},
    'Jet1_pt':{'name':'Jet1_pt','title':'jet_pt','bin':50,'xmin':2000.0,'xmax':10000.0},
    'Jet2_pt':{'name':'Jet2_pt','title':'jet2_pt','bin':50,'xmin':2000.0,'xmax':10000.0},
    'Jet1_tau21':{'name':'Jet1_tau21','title':'#tau_{2,1}','bin':50,'xmin':0.0,'xmax':1.0},
    'Jet2_tau21':{'name':'Jet2_tau21','title':'#tau_{2,1} Jet2','bin':50,'xmin':0.0,'xmax':1.0},
    'Jet1_tau32':{'name':'Jet1_tau32','title':'#tau_{3,2}','bin':50,'xmin':0.2,'xmax':1.0},
    'Jet2_tau32':{'name':'Jet2_tau32','title':'#tau_{3,2} Jet2','bin':50,'xmin':0.0,'xmax':1.0},
    'Jet1_Flow15':{'name':'Jet1_Flow15','title':'Flow_{1,5} Jet_1','bin':50,'xmin':0.0,'xmax':1.0},
    'Jet2_Flow15':{'name':'Jet2_Flow15','title':'Flow_{1,5} Jet_2','bin':50,'xmin':0.0,'xmax':1.0},
    'Jet1_Flow25':{'name':'Jet1_Flow25','title':'Flow_{2,5} Jet_1','bin':50,'xmin':0.0,'xmax':1.0},
    'Jet2_Flow25':{'name':'Jet2_Flow25','title':'Flow_{2,5} Jet_2','bin':50,'xmin':0.0,'xmax':1.0},
    'met_pt':{'name':'met_pt','title':'met_{pT}','bin':50,'xmin':0.0,'xmax':8000.},
#    'rapiditySeparation':{'name':'rapiditySeparation','title':'#Delta Y','bin':50,'xmin':0.0,'xmax':4.0},
}

colors = {}
colors['m_{RSG} = 2 TeV'] = ROOT.kBlue
colors['m_{RSG} = 5 TeV'] = ROOT.kBlue
colors['m_{RSG} = 10 TeV'] = ROOT.kBlue
colors['m_{RSG} = 15 TeV'] = ROOT.kBlue
colors['m_{RSG} = 20 TeV'] = ROOT.kBlue
colors['m_{RSG} = 25 TeV'] = ROOT.kBlue
colors['m_{RSG} = 30 TeV'] = ROOT.kBlue
colors['m_{RSG} = 35 TeV'] = ROOT.kBlue
colors['m_{RSG} = 40 TeV'] = ROOT.kBlue
colors['QCD'] = ROOT.kYellow
colors['tt'] = ROOT.kOrange
colors['VV'] = ROOT.kRed

signal_groups = collections.OrderedDict()
signal_groups['m_{RSG} = 2 TeV']  = ['pp_RSGraviton_2TeV_ww']
signal_groups['m_{RSG} = 5 TeV']  = ['pp_RSGraviton_5TeV_ww']
signal_groups['m_{RSG} = 10 TeV'] = ['pp_RSGraviton_10TeV_ww']
signal_groups['m_{RSG} = 15 TeV'] = ['pp_RSGraviton_15TeV_ww']
signal_groups['m_{RSG} = 20 TeV'] = ['pp_RSGraviton_20TeV_ww']
signal_groups['m_{RSG} = 25 TeV'] = ['pp_RSGraviton_25TeV_ww']
signal_groups['m_{RSG} = 30 TeV'] = ['pp_RSGraviton_30TeV_ww']
signal_groups['m_{RSG} = 35 TeV'] = ['pp_RSGraviton_35TeV_ww']
signal_groups['m_{RSG} = 40 TeV'] = ['pp_RSGraviton_40TeV_ww']

background_groups = collections.OrderedDict()
background_groups['VV']  = [
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
selbase = 'Jet1_pt > 2000. && abs(Jet1_eta) < 2.4 && abs(Jet2_eta) < 2.4 && Jet1_tau21 < 0.6 && softDroppedJet1_m > 50 && softDroppedJet1_m < 100 && Jet1_tau21 > 0 && Jet1_tau32 > 0 && Jet2_tau21 > 0 && Jet2_tau32 > 0'

# add mass-dependent list of event #selections here if needed...

selections = collections.OrderedDict()

selections['m_{RSG} = 2 TeV'] = []
selections['m_{RSG} = 2 TeV'].append(selbase + ' && nelectrons == 0 && nmuons == 0 && Jet2_pt > 2000. && Jet2_tau21 < 0.6 && softDroppedJet2_m > 50 && softDroppedJet2_m < 100 && Jet1_Flow15 > 0.8 && Jet2_Flow15 > 0.8 && Jet1_Flow25 < 0.1 && Jet2_Flow25 < 0.1') #allHad
selections['m_{RSG} = 2 TeV'].append(selbase + ' && (nelectrons > 0 || nmuons > 0) && Jet1_Flow15 > 0.6') #semiLep

