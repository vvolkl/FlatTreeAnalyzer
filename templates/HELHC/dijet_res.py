import ROOT
import collections

### variable list
variables = {

#        'Jet1_pf04_pt':{'name':'Jet1_pf04_pt','title':'Jet1 p_{T} [TeV]','bin':115,'xmin':0,'xmax':10, 'divide':1000},
#        'Jet1_pf04_eta':{'name':'Jet1_pf04_eta','title':'Jet1 #eta','bin':50,'xmin':-5.0,'xmax':5.0},
#
#        'Jet2_pf04_pt':{'name':'Jet2_pf04_pt','title':'Jet2 p_{T} [TeV]','bin':115,'xmin':0,'xmax':10, 'divide':1000},
#        'Jet2_pf04_eta':{'name':'Jet2_pf04_eta','title':'Jet2 #eta','bin':50,'xmin':-5.0,'xmax':5.0},
#
#        'Jet1_calo04_pt':{'name':'Jet1_calo04_pt','title':'Jet1 p_{T} [TeV]','bin':115,'xmin':0,'xmax':10, 'divide':1000},
#        'Jet1_calo04_eta':{'name':'Jet1_calo04_eta','title':'Jet1 #eta','bin':50,'xmin':-5.0,'xmax':5.0},
#
#        'Jet2_calo04_pt':{'name':'Jet2_calo04_pt','title':'Jet2 p_{T} [TeV]','bin':115,'xmin':0,'xmax':10, 'divide':1000},
#        'Jet2_calo04_eta':{'name':'Jet2_calo04_eta','title':'Jet2 #eta','bin':50,'xmin':-5.0,'xmax':5.0},
#
#        'rapiditySeparation_pf04':{'name':'rapiditySeparation_pf04','title':'Rapidity Separation','bin':60,'xmin':0.0,'xmax':3.0},
#        'pseudorapiditySeparation_pf04':{'name':'pseudorapiditySeparation_pf04','title':'pseudo Rapidity Separation','bin':60,'xmin':0.0,'xmax':6.0},
#
#        'transverseMomentumAsymmetry_pf_04':{'name':'transverseMomentumAsymmetry_pf04','title':'Transverse Momentum Asymmetry','bin':50,'xmin':0.0,'xmax':1.0},
#
#        'Mj1j2_pf04' :{'name':'Mj1j2_pf04','title':'m_{Q*} [TeV] (pf04)','bin':200,'xmin':0.0,'xmax':20.0, 'divide':1000},
#        'Mj1j2_calo04' :{'name':'Mj1j2_calo04','title':'m_{Q*} [TeV] (calo04)','bin':200,'xmin':0.0,'xmax':20.0, 'divide':1000},

        'Mj1j2_pf04' :{'name':'Mj1j2_pf04','title':'m_{Q*} [TeV] (pf04)','bin':200,'xmin':0.0,'xmax':20.0, 'divide':1000},

}

variables2D = {}


colors = {}
colors['m_{Q*} = 2 TeV']  = ROOT.kRed
colors['m_{Q*} = 4 TeV']  = ROOT.kRed
colors['m_{Q*} = 6 TeV']  = ROOT.kRed
colors['m_{Q*} = 8 TeV']  = ROOT.kRed
colors['m_{Q*} = 10 TeV'] = ROOT.kRed
colors['m_{Q*} = 12 TeV'] = ROOT.kRed
colors['m_{Q*} = 14 TeV'] = ROOT.kRed
colors['m_{Q*} = 16 TeV'] = ROOT.kRed
colors['QCD'] = ROOT.kGreen+2

signal_groups = collections.OrderedDict()

signal_groups['m_{Q*} = 2 TeV']  = ['p8_pp_ExcitedQ_2TeV_qq']
signal_groups['m_{Q*} = 4 TeV']  = ['p8_pp_ExcitedQ_4TeV_qq']
signal_groups['m_{Q*} = 6 TeV']  = ['p8_pp_ExcitedQ_6TeV_qq']
signal_groups['m_{Q*} = 8 TeV']  = ['p8_pp_ExcitedQ_8TeV_qq']
signal_groups['m_{Q*} = 10 TeV'] = ['p8_pp_ExcitedQ_10TeV_qq']
signal_groups['m_{Q*} = 12 TeV'] = ['p8_pp_ExcitedQ_12TeV_qq']
signal_groups['m_{Q*} = 14 TeV'] = ['p8_pp_ExcitedQ_14TeV_qq']
signal_groups['m_{Q*} = 16 TeV'] = ['p8_pp_ExcitedQ_16TeV_qq']

background_groups = collections.OrderedDict()

background_groups['QCD'] = [
'mgp8_pp_jj_5f_HT_500_1000',
'mgp8_pp_jj_5f_HT_1000_2000',
'mgp8_pp_jj_5f_HT_2000_5000',
'mgp8_pp_jj_5f_HT_5000_10000',
'mgp8_pp_jj_5f_HT_10000_27000',
]


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

# base pre-#selections
selbase  = 'Jet1_calo04_pt > 1000. && Jet2_calo04_pt > 1000.'
selbase += ' && Mj1j2_calo04 > 2000.0'
sel1     = selbase + ' && rapiditySeparation_pf04 < 1.5'

selections = collections.OrderedDict()
selections['m_{Q*} = 2 TeV'] = []
selections['m_{Q*} = 2 TeV'].append(selbase)
selections['m_{Q*} = 2 TeV'].append(sel1)

selections['m_{Q*} = 4 TeV'] = []
selections['m_{Q*} = 4 TeV'].append(selbase)
selections['m_{Q*} = 4 TeV'].append(sel1)

selections['m_{Q*} = 6 TeV'] = []
selections['m_{Q*} = 6 TeV'].append(selbase)
selections['m_{Q*} = 6 TeV'].append(sel1)

selections['m_{Q*} = 8 TeV'] = []
selections['m_{Q*} = 8 TeV'].append(selbase)
selections['m_{Q*} = 8 TeV'].append(sel1)

selections['m_{Q*} = 10 TeV'] = []
selections['m_{Q*} = 10 TeV'].append(selbase)
selections['m_{Q*} = 10 TeV'].append(sel1)

selections['m_{Q*} = 12 TeV'] = []
selections['m_{Q*} = 12 TeV'].append(selbase)
selections['m_{Q*} = 12 TeV'].append(sel1)

selections['m_{Q*} = 14 TeV'] = []
selections['m_{Q*} = 14 TeV'].append(selbase)
selections['m_{Q*} = 14 TeV'].append(sel1)

selections['m_{Q*} = 16 TeV'] = []
selections['m_{Q*} = 16 TeV'].append(selbase)
selections['m_{Q*} = 16 TeV'].append(sel1)

