import ROOT
import collections

variables = {
    "haa_m":{"name":"haa_m","title":"m_{#gamma #gamma} [GeV]","bin":40,"xmin":115.0,"xmax":135.0},
    "hbb_m":{"name":"hbb_m","title":"m_{j j} [GeV]","bin":40,"xmin":50.0,"xmax":200.0},
    "hh_m":{"name":"hh_m","title":"m_{j j #gamma #gamma} [GeV]","bin":30,"xmin":100.0,"xmax":1000.0},
    "nljets":{"name":"nljets","title":"N_{jets}^{light}","bin":10,"xmin":-.05,"xmax":9.5},
    "nlep":{"name":"nlep","title":"N_{leptons}","bin":5,"xmin":-.05,"xmax":4.5},
    "met":{"name":"met_pt","title":"E_{T}^{miss}","bin":50,"xmin":0,"xmax":500.},

}

variables2D = {
    "hmaa_mbb":{ 
                  "namex":"haa_m","namey":"hbb_m","titlex":"m_{#gamma #gamma} [GeV]","titley":"m_{j j} [GeV]",
                  "binx":50,"xmin":120.0,"xmax":130.0,"biny":50,"ymin":80.0,"ymax":140.0
               },

    "hmaa_mhh":{ 
                  "namex":"haa_m","namey":"hh_m","titlex":"m_{#gamma #gamma} [GeV]","titley":"m_{h h} [GeV]",
                  "binx":50,"xmin":120.0,"xmax":130.0,"biny":75,"ymin":240.0,"ymax":1500.0
               },

}




colors = {}
colors['HH(#kappa_{l}=0.50)'] = ROOT.kRed
colors['HH(#kappa_{l}=0.90)'] = ROOT.kRed
colors['HH(#kappa_{l}=0.95)'] = ROOT.kRed
colors['HH(#kappa_{l}=1.00)'] = ROOT.kRed
colors['HH(#kappa_{l}=1.05)'] = ROOT.kRed
colors['HH(#kappa_{l}=1.10)'] = ROOT.kRed
colors['HH(#kappa_{l}=1.50)'] = ROOT.kRed

colors['j#gamma + Jets'] = ROOT.kAzure+1
colors['#gamma#gamma + Jets'] = ROOT.kCyan-8
colors['ttH'] = ROOT.kViolet

signal_groups = collections.OrderedDict()
signal_groups['HH(#kappa_{l}=0.50)'] = ['pp_hh_lambda050_5f']
signal_groups['HH(#kappa_{l}=0.90)'] = ['pp_hh_lambda090_5f']
signal_groups['HH(#kappa_{l}=0.95)'] = ['pp_hh_lambda095_5f']
signal_groups['HH(#kappa_{l}=1.00)'] = ['pp_hh_lambda100_5f']
signal_groups['HH(#kappa_{l}=1.05)'] = ['pp_hh_lambda105_5f']
signal_groups['HH(#kappa_{l}=1.10)'] = ['pp_hh_lambda110_5f']
signal_groups['HH(#kappa_{l}=1.50)'] = ['pp_hh_lambda150_5f']

background_groups = collections.OrderedDict()
background_groups['ttH'] = ['pp_tth01j_5f']
background_groups['j#gamma + Jets'] = ['pp_jjja_5f']
background_groups['#gamma#gamma + Jets'] = ['pp_jjaa_5f']

# global parameters
intLumi = 30000000
delphesVersion = '3.4.2'

uncertainties = []
uncertainties.append([0., 0.])
uncertainties.append([0.02, 0.0])
uncertainties.append([0.02, 0.02])
uncertainties.append([0.02, 0.10])

# the first time needs to be set to True
runFull = True
#runFull = False


# base pre-selections

tthcut = ' && nlep == 0 && nljets < 4 && met_pt < 100'
mcut = ' && abs(haa_m - 125.) < 50 && hbb_m > 80. && hbb_m < 140.'
mbbcut = ' && hbb_m > 80. && hbb_m < 140.'
maacut = ' && abs(haa_m - 125.) < 5.0 '
yrcut = ' && a1_pt > 60. && b1_pt > 60. && a2_pt > 35. && b2_pt > 35. && haa_pt > 100. && hbb_pt > 100.'


selection_yr  = []
selection_cms = []
selection_new = []


sel0  = 'abs(b1_eta) < 6.0 && abs(b2_eta) < 6.0 && '
sel0 += 'abs(a1_eta) < 6.0 && abs(a2_eta) < 6.0 && '
sel0 += 'a1_pt > 35. && b1_pt > 35. && '
sel0 += 'a2_pt > 35. && b2_pt > 35. && '
sel0 += 'haa_m > 100. && haa_m < 180. && '
sel0 += 'hbb_m > 70. && hbb_m < 190.'

sel1 = sel0
sel1 += ' && abs(b1_eta) < 4.5 && abs(b2_eta) < 4.5 && '
sel1 += 'abs(a1_eta) < 4.5 && abs(a2_eta) < 4.5 && '
sel1 += 'a1_pt > 60. && b1_pt > 60. && '
sel1 += 'a2_pt > 35. && b2_pt > 35. && '
sel1 += 'haa_pt > 100. && hbb_pt > 100. && '
sel1 += 'draa < 3.5 && drbb < 3.5'

sel2 = sel1 + mbbcut
sel3 = sel2 + maacut

selection_yr.append(sel0)
selection_yr.append(sel1)
selection_yr.append(sel2)
selection_yr.append(sel3)


sel4  = 'a1_pt > 30. && a1_pt > haa_m/3.0 && abs(a1_eta) < 2.5 && '
sel4 += 'a2_pt > 20. && a2_pt > haa_m/4.0 && abs(a2_eta) < 2.5 && '
sel4 += 'b1_pt > 25. && abs(b1_eta) < 2.5 && '
sel4 += 'b2_pt > 25. && abs(b2_eta) < 2.5 && '
sel4 += 'haa_m > 100 && haa_m < 180 && '
sel4 += 'hbb_m > 70 && hbb_m < 190'

sel5 = sel4 + mbbcut
sel6 = sel5 + maacut

selection_cms.append(sel4)
selection_cms.append(sel5)
selection_cms.append(sel6)


sel7  = 'a1_pt > 30. && a1_pt > haa_m/3.0 && abs(a1_eta) < 2.5 && '
sel7 += 'a2_pt > 20. && a2_pt > haa_m/4.0 && abs(a2_eta) < 2.5 && '
sel7 += 'b1_pt > 25. && abs(b1_eta) < 2.5 && '
sel7 += 'b2_pt > 25. && abs(b2_eta) < 2.5 && '
sel7 += 'haa_m > 100. && haa_m < 180. && '
sel7 += 'hbb_m > 70. && hbb_m < 190.'

sel8 = sel7 + yrcut
sel9 = sel8 + mbbcut
sel10 = sel9 + maacut

selection_new.append(sel7)
selection_new.append(sel8)
selection_new.append(sel9)
selection_new.append(sel10)


# add mass-dependent list of event selections here if needed...
selections = collections.OrderedDict()

selections['HH(#kappa_{l}=0.50)'] = []
selections['HH(#kappa_{l}=0.90)'] = []
selections['HH(#kappa_{l}=0.95)'] = []
selections['HH(#kappa_{l}=1.00)'] = []
selections['HH(#kappa_{l}=1.05)'] = []
selections['HH(#kappa_{l}=1.10)'] = []
selections['HH(#kappa_{l}=1.50)'] = []

for sel in selection_yr:
    selections['HH(#kappa_{l}=0.50)'].append(sel)
    selections['HH(#kappa_{l}=0.90)'].append(sel)
    selections['HH(#kappa_{l}=0.95)'].append(sel)
    selections['HH(#kappa_{l}=1.00)'].append(sel)
    selections['HH(#kappa_{l}=1.05)'].append(sel)
    selections['HH(#kappa_{l}=1.10)'].append(sel)
    selections['HH(#kappa_{l}=1.50)'].append(sel)

for sel in selection_cms:
    selections['HH(#kappa_{l}=0.50)'].append(sel)
    selections['HH(#kappa_{l}=0.90)'].append(sel)
    selections['HH(#kappa_{l}=0.95)'].append(sel)
    selections['HH(#kappa_{l}=1.00)'].append(sel)
    selections['HH(#kappa_{l}=1.05)'].append(sel)
    selections['HH(#kappa_{l}=1.10)'].append(sel)
    selections['HH(#kappa_{l}=1.50)'].append(sel)

for sel in selection_new:
    selections['HH(#kappa_{l}=0.50)'].append(sel)
    selections['HH(#kappa_{l}=0.90)'].append(sel)
    selections['HH(#kappa_{l}=0.95)'].append(sel)
    selections['HH(#kappa_{l}=1.00)'].append(sel)
    selections['HH(#kappa_{l}=1.05)'].append(sel)
    selections['HH(#kappa_{l}=1.10)'].append(sel)
    selections['HH(#kappa_{l}=1.50)'].append(sel)
