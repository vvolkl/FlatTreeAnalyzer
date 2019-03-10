import ROOT, os, sys
from ROOT import *

''' 
the way to get fit params :
---------------------------

import ROOT, os, sys
from ROOT import *
tree="outputs/analysis_fcc_v02/zptt_degrade2/root_m_Z_10TeV/histos.root"
low_x=5.
high_x=20.
lumi="sqrt(100.)"
fit_func="[0]*((1-(x/"+lumi+"))^[1])*((x/"+lumi+")^[2])*((x/"+lumi+")^([3]*log(x/"+lumi+")))"
rebin=10
rf = TFile(tree,"READ")
hist = rf.Get("vv_sel0_Mj1j2_pf08_MetCorr")
new_hist = hist.Clone()
hist.Rebin(rebin)
myfit = ROOT.TF1("myfit",fit_func, low_x, high_x)
hist.Fit("myfit","S","",6.,45.)
hist.Fit("myfit","S","",7.,45.)

-> adjust x bounds to get the best fit

for dijet need to reconstruct an histo starting from 0:
-------------------------------------------------------
hist0=ROOT.TH1D("hist0","hist0",250,low_x,high_x)
for i_bin in xrange( 1, hist0.GetNbinsX()+1 ):
  the_val=0.
  if i_bin>50 : the_val=hist.GetBinContent(i_bin-50)
  hist0.SetBinContent(i_bin, the_val)
myfit = ROOT.TF1("myfit",fit_func, low_x, high_x)
hist0.Fit("myfit","S","",5.,25.)

then to check how it is good, fill an histo:
--------------------------------------------

for i_bin in xrange( 1, new_hist.GetNbinsX()+1 ):
  the_val = myfit.Eval(new_hist.GetBinCenter(i_bin))
  if the_val<0. : the_val=0.
  if new_hist.GetBinCenter(i_bin)<low_x : the_val=0.
  #print the_val
  new_hist.SetBinContent(i_bin, the_val)
  new_hist.SetBinError(i_bin,0.)
new_hist.Scale( hist.Integral() / new_hist.Integral() )
new_hist.Rebin(rebin)
new_hist.Draw("same")

then run :
----------
python scripts/fit_histo_Mjj.py outputs/analysis_fcc_v02/RSGww/root_m_RSG_10TeV/histos.root

'''

isFCChh = True
#isFCChh = False

#tmp_fix=True
tmp_fix=False

degrade=0
#degrade=1
#degrade=2
#degrade=3

tree = sys.argv[1]

ana=""
if tree.find("m_RSG")>=0 : ana="RSG"
elif tree.find("m_Z")>=0 : ana="zptt"
elif tree.find("m_Q")>=0 : ana="dijet"

variable=""
if ana=="RSG"     : variable="Mj1j2_pf08"
elif ana=="zptt"  : variable="Mj1j2_pf08_MetCorr"
elif ana=="dijet" : variable="Mj1j2_pf04"

extra_out="_fit"
extra=variable+"_"

low_x=5.
if ana=="dijet" : low_x=10.
if isFCChh == False : low_x=2.
high_x=50.
if isFCChh == True : lumi="sqrt(100.)"
else               : lumi="sqrt(27.)"
fit_func="[0]*((1-(x/"+lumi+"))^[1])*((x/"+lumi+")^[2])*((x/"+lumi+")^([3]*log(x/"+lumi+")))"
# [0]*((1-(x/sqrt(100.)))^[1])*((x/sqrt(100.))^[2])*((x/sqrt(100.))^([3]*log(x/sqrt(100.))))

fitList = []
fitList.append(["RSG","vv_sel0"  ,3.59052e-04,0.00000e+00,-2.02738e+00,-5.08291e+00])
fitList.append(["RSG","vj_sel0"  ,1.01537e-02,0.00000e+00,-2.68316e+00,-3.95167e+00])
fitList.append(["RSG","tt_sel0"  ,6.89166e-03,0.00000e+00,-2.45027e+00,-5.02780e+00])
#fitList.append(["RSG","QCD_sel0" ,,,,])
fitList.append(["RSG","vv_sel1"  ,6.16372e-05,0.00000e+00,-3.47524e+00,-3.34073e+00])
fitList.append(["RSG","vj_sel1"  ,6.81562e-04,0.00000e+00,-3.69566e+00,-3.75166e+00])
fitList.append(["RSG","tt_sel1"  ,8.03044e-05,0.00000e+00,-3.49127e+00,-4.96826e+00])
fitList.append(["RSG","QCD_sel1" ,1.16048e-02,0.00000e+00,-2.64228e+00,-4.03688e+00])
fitList.append(["RSG","vv_sel2"  ,2.07918e-05,0.00000e+00,-1.69753e+00,-4.11780e+00])
fitList.append(["RSG","vj_sel2"  ,2.13894e-04,0.00000e+00,-2.14716e+00,-4.32275e+00])
fitList.append(["RSG","tt_sel2"  ,1.67178e-05,0.00000e+00,-1.53805e+00,-5.73859e+00])
fitList.append(["RSG","QCD_sel2" ,3.27486e-03,0.00000e+00,-1.10809e+00,-4.93517e+00])
fitList.append(["RSG","vv_sel3"  ,5.17682e-05,0.00000e+00,-2.54201e+00,-3.67304e+00])
fitList.append(["RSG","vj_sel3"  ,3.85578e-04,0.00000e+00,-2.38532e+00,-3.94256e+00])
fitList.append(["RSG","tt_sel3"  ,2.83434e-05,0.00000e+00,-3.57324e+00,-4.23561e+00])
fitList.append(["RSG","QCD_sel3" ,1.67663e-03,0.00000e+00,-1.77258e+00,-3.62955e+00])
fitList.append(["RSG","vv_sel4"  ,4.58470e-05,0.00000e+00,-2.88536e+00,-3.44451e+00])
fitList.append(["RSG","vj_sel4"  ,1.93022e-04,0.00000e+00,-2.65115e+00,-3.61228e+00])
fitList.append(["RSG","tt_sel4"  ,2.41222e-05,0.00000e+00,-3.75255e+00,-4.06993e+00])
fitList.append(["RSG","QCD_sel4" ,5.05153e-04,0.00000e+00,-1.27060e+00,-3.77269e+00])
if degrade==0:
  fitList.append(["zptt","vv_sel0" ,3.38130e-04,0.00000e+00,-5.45947e-01,-5.02950e+00])
  fitList.append(["zptt","vj_sel0" ,9.56826e-03,0.00000e+00,-9.56949e-01,-4.36535e+00])
  fitList.append(["zptt","tt_sel0" ,7.26207e-03,0.00000e+00,-1.29401e+00,-4.80901e+00])
  #fitList.append(["zptt","QCD_sel0",,,,])
if degrade==1:
  fitList.append(["zptt","vv_sel0" ,1.37070e-07,0.00000e+00,-2.13006e+00,-6.30723e+00])
  fitList.append(["zptt","vj_sel0" ,2.04681e-06,0.00000e+00,-2.76323e+00,-6.16998e+00])
  fitList.append(["zptt","tt_sel0" ,6.33758e-04,0.00000e+00,-1.95219e+00,-6.84066e+00])
  fitList.append(["zptt","QCD_sel0",9.85091e-05,0.00000e+00,-1.19073e+00,-7.59997e+00])
if degrade==2:
  fitList.append(["zptt","vv_sel0" ,1.12822e-07,0.00000e+00,-2.28136e+00,-6.16197e+00])
  fitList.append(["zptt","vj_sel0" ,1.70528e-06,0.00000e+00,-2.93202e+00,-6.16569e+00])
  fitList.append(["zptt","tt_sel0" ,5.05950e-04,0.00000e+00,-2.14359e+00,-7.24253e+00])
  fitList.append(["zptt","QCD_sel0",7.88840e-05,0.00000e+00,-1.32488e+00,-7.44150e+00])
if degrade==3:
  fitList.append(["zptt","vv_sel0" ,8.22419e-08,0.00000e+00,-2.49031e+00,-6.24499e+00])
  fitList.append(["zptt","vj_sel0" ,1.20856e-06,0.00000e+00,-3.27191e+00,-6.08640e+00])
  fitList.append(["zptt","tt_sel0" ,3.22710e-04,0.00000e+00,-2.63806e+00,-8.22407e+00])
  fitList.append(["zptt","QCD_sel0",5.15323e-05,0.00000e+00,-1.85175e+00,-6.91684e+00])
fitList.append(["zptt","vv_sel1" ,6.01333e-06,0.00000e+00,-3.92261e+00,-2.93296e+00])
fitList.append(["zptt","vj_sel1" ,4.14374e-04,0.00000e+00,-1.17864e+00,-3.82622e+00])
fitList.append(["zptt","tt_sel1" ,1.54320e-03,0.00000e+00,-1.80813e+00,-4.10498e+00])
#fitList.append(["zptt","QCD_sel1",,,,])
fitList.append(["zptt","vv_sel2" ,1.74388e-08,0.00000e+00,5.44460e-01,-5.26937e+00])
fitList.append(["zptt","vj_sel2" ,1.24621e-08,0.00000e+00,-1.92212e-01,-4.01644e+00])
#fitList.append(["zptt","tt_sel2" ,,,,])
#fitList.append(["zptt","QCD_sel2",,,,])
fitList.append(["zptt","vv_sel3" ,5.60656e-05,0.00000e+00,-2.52746e+00,-4.10275e+00])
#fitList.append(["zptt","vj_sel3" ,,,,])
#fitList.append(["zptt","tt_sel3" ,,,,])
fitList.append(["zptt","QCD_sel3",2.42870e-02,0.00000e+00,-5.45131e-01,-5.41634e+00])
fitList.append(["zptt","vv_sel4" ,5.49774e-05,0.00000e+00,-2.53919e+00,-4.08325e+00])
#fitList.append(["zptt","vj_sel4" ,,,,])
#fitList.append(["zptt","tt_sel4" ,,,,])
fitList.append(["zptt","QCD_sel4",2.37592e-02,0.00000e+00,-5.65974e-01,-5.43926e+00])
fitList.append(["zptt","vv_sel5" ,1.97292e-10,0.00000e+00,-2.24265e+00,-9.68543e+00])
fitList.append(["zptt","vj_sel5" ,5.73773e-07,0.00000e+00,-2.27145e+00,-7.16070e+00])
fitList.append(["zptt","tt_sel5" ,4.64431e-04,0.00000e+00,-1.72420e+00,-6.44843e+00])
fitList.append(["zptt","QCD_sel5",1.74469e-04,0.00000e+00,-6.14594e-01,-6.78934e+00])
fitList.append(["zptt","vv_sel6" ,1.74570e-07,0.00000e+00,-1.99785e+00,-5.77198e+00])
fitList.append(["zptt","vj_sel6" ,3.21598e-06,0.00000e+00,-2.38041e+00,-6.69842e+00])
fitList.append(["zptt","tt_sel6" ,8.97904e-04,0.00000e+00,-1.72103e+00,-7.25101e+00])
fitList.append(["zptt","QCD_sel6",1.42757e-04,0.00000e+00,-1.94134e+00,-4.35175e+00])
fitList.append(["zptt","vv_sel7" ,1.70108e-10,0.00000e+00,-2.48855e+00,-5.37723e+00])
fitList.append(["zptt","vj_sel7" ,3.20604e-08,0.00000e+00,1.56869e-01,-6.71284e+00])
fitList.append(["zptt","tt_sel7" ,4.42636e-04,0.00000e+00,-1.89085e+00,-6.15429e+00])
fitList.append(["zptt","QCD_sel7",8.83330e-05,0.00000e+00,-3.82989e-01,-5.84592e+00])
fitList.append(["zptt","vv_sel8" ,1.54104e-07,0.00000e+00,-2.03855e+00,-6.37648e+00])
fitList.append(["zptt","vj_sel8" ,2.31778e-06,0.00000e+00,-2.63856e+00,-6.25726e+00])
fitList.append(["zptt","tt_sel8" ,7.27016e-04,0.00000e+00,-1.85126e+00,-6.63731e+00])
fitList.append(["zptt","QCD_sel8",1.12662e-04,0.00000e+00,-1.10449e+00,-7.70251e+00])
fitList.append(["dijet","QCD_sel0",2.78876e-01,0.00000e+00,-3.36772e+00,-1.21888e+00])
fitList.append(["dijet","QCD_sel1",2.66067e-01,0.00000e+00,-2.49503e+00,-3.68841e+00])

fitList_27 = []
fitList_27.append(["RSG","vv_sel4"  ,2.44844e-06,0.00000e+00,-4.10323e+00,-4.77460e+00])
fitList_27.append(["RSG","vj_sel4"  ,6.28039e-06,0.00000e+00,-4.03591e+00,-4.51547e+00])
fitList_27.append(["RSG","tt_sel4"  ,1.55086e-06,0.00000e+00,-8.18615e+00,-7.98745e+00])
fitList_27.append(["RSG","QCD_sel4" ,5.72396e-06,0.00000e+00,2.42211e+00,-8.38424e+00])
if tmp_fix==True :
  # Zptt
  fitList_27.append(["zptt","vv_sel0" ,1.17109e-07,0.00000e+00,-3.99751e+00,-5.76939e+00])
  fitList_27.append(["zptt","vj_sel0" ,9.46013e-07,0.00000e+00,-4.17355e+00,-5.54113e+00])
  fitList_27.append(["zptt","tt_sel0" ,4.01787e-04,0.00000e+00,-3.95015e+00,-6.43429e+00])
  fitList_27.append(["zptt","QCD_sel0",2.30000e-05,0.00000e+00,-3.09631e+00,-5.00743e+00])
  # Zpbb
  #fitList_27.append(["zptt","vv_sel0" ,8.88212e-09,0.00000e+00,-5.64782e+00,-5.42419e+00])
  #fitList_27.append(["zptt","vj_sel0" ,1.31956e-06,0.00000e+00,-5.19483e+00,-5.32341e+00])
  #fitList_27.append(["zptt","tt_sel0" ,1.71020e-06,0.00000e+00,-6.51345e+00,-5.79119e+00])
  #fitList_27.append(["zptt","QCD_sel0",6.62478e-04,0.00000e+00,-5.14257e+00,-6.00409e+00])
fitList_27.append(["zptt","vv_sel8" ,1.17109e-07,0.00000e+00,-3.99751e+00,-5.76939e+00])
fitList_27.append(["zptt","vj_sel8" ,9.46013e-07,0.00000e+00,-4.17355e+00,-5.54113e+00])
fitList_27.append(["zptt","tt_sel8" ,4.01787e-04,0.00000e+00,-3.95015e+00,-6.43429e+00])
fitList_27.append(["zptt","QCD_sel8",2.30000e-05,0.00000e+00,-3.09631e+00,-5.00743e+00])


# FCC-hh
if isFCChh == True : the_fitList = fitList
# HELHC
else : the_fitList = fitList_27

rf = TFile(tree,"UPDATE")

for tkey in rf.GetListOfKeys():
  key = tkey.GetName()
  plotToFit=False
  isSig=False
  #if key.find(variable)>=0 and key.find(extra_out)<0: # old fail with dijet ana
  if key.find(variable)>=0 and key.find(extra)<0:
    if key.find("} =")>=0 : isSig=True
    print key
    # check key
    for sample in the_fitList:
      if ana==sample[0] and key.find(sample[1])>=0 :
        plotToFit=True
        p0=sample[2]
        p1=sample[3]
        p2=sample[4]
        p3=sample[5]
    # get init histo
    hist = rf.Get(key)
    new_hist = hist.Clone()
    if plotToFit==True and isSig==False :
      myfit = ROOT.TF1("myfit",fit_func, low_x, high_x)
      myfit.SetParameters(p0,p1,p2,p3)
      # fill new histo
      for i_bin in xrange( 1, new_hist.GetNbinsX()+1 ):
        the_val = myfit.Eval(new_hist.GetBinCenter(i_bin))
        if the_val<0. : the_val=0.
        if new_hist.GetBinCenter(i_bin)<low_x : the_val=0.
        new_hist.SetBinContent(i_bin, the_val)
        new_hist.SetBinError(i_bin,0.)
      # keep norm
      if isFCChh == False and key == "QCD_sel4_Mj1j2_pf08":
        new_hist.Scale( hist.Integral( hist.FindBin(4.),hist.FindBin(20.) ) / new_hist.Integral( hist.FindBin(4.),hist.FindBin(20.) ) )
      elif isFCChh == False and key == "QCD_sel8_Mj1j2_pf08_MetCorr":
        new_hist.Scale( hist.Integral( hist.FindBin(6.),hist.FindBin(20.) ) / new_hist.Integral( hist.FindBin(6.),hist.FindBin(20.) ) )
      elif isFCChh == False and key == "QCD_sel0_Mj1j2_pf08_MetCorr" and tmp_fix==True:
        new_hist.Scale( hist.Integral( hist.FindBin(6.),hist.FindBin(20.) ) / new_hist.Integral( hist.FindBin(6.),hist.FindBin(20.) ) )
      else :
        new_hist.Scale( hist.Integral() / new_hist.Integral() )
    # save it
    new_hist.SetName(key+extra_out)
    new_hist.Write()

rf.Close()
