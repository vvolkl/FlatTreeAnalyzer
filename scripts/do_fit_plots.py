import ROOT as r
import re

Ana=[
#'RSGww',
#'Zptt',
'dijet',
]

Sample=[
'QCD',
#'tt',
#'vv',
#'vj',
]

############
Sel = {}
Sel['RSGww']=[
#"sel0",
#"sel1",
"sel2",
#"sel3",
"sel4",
]
Sel['Zptt']=[
#"sel0",
#"sel1",
#"sel2",
#"sel3",
#"sel4",
"sel5",
"sel6",
"sel7",
"sel8",
]
Sel['dijet']=[
"sel0",
"sel1",
]

############
Colors = {}
Colors['QCD'] = r.kBlue+1
Colors['tt']  = r.kOrange-2
Colors['vv']  = r.kGreen+2
Colors['vj']  = r.kMagenta+2

############
Var = {}
Var['RSGww']="Mj1j2_pf08"
Var['Zptt']="Mj1j2_pf08_MetCorr"
Var['dijet']="Mj1j2_pf04"

############
Path = {}
Path['RSGww']='/eos/experiment/fcc/hh/analyses/RSGraviton_ww/FlatTreeAnalyzer_outputs/fcc_v02/May2018_HTsplit_prod/root_m_RSG_10TeV/histos.root'
Path['Zptt']='/eos/experiment/fcc/hh/analyses/Zprime_tt/FlatTreeAnalyzer_outputs/fcc_v02/May2018_HTsplit_prod/root_m_Z_10TeV/histos.root'
Path['dijet']='/eos/experiment/fcc/hh/analyses/Dijet_reso/FlatTreeAnalyzer_outputs/fcc_v02/root_m_Q*_50TeV/histos.root'

############
Title = {}
Title['RSGww']='m_{RSG} [TeV] (pf08)'
Title['Zptt']='m_{Z\'} [TeV] (pf08 metcor)'
Title['dijet']='m_{Z\'} [TeV] (pf04)'

############
for ana in Ana :
  for sample in Sample :
    for sel in Sel[ana] :

      color=Colors[sample]
      var=Var[ana]
      path=Path[ana]
      title=Title[ana]
      hist=sample+"_"+sel+"_"+var

      ############
      infile = r.TFile.Open(path)
      h_ini = infile.Get(hist)
      h_fit = infile.Get(hist+'_fit')
      
      h_ini.Rebin(5)
      h_fit.Rebin(5)
      
      h_ini.SetLineWidth(3)
      #h_fit.SetLineWidth(3)
      
      h_ini.SetLineColor(r.kBlack)
      h_fit.SetLineColor(color)
      h_fit.SetFillColor(color)

      ###########
      lumi = 3.0e+07
      delphesVersion = '3.4.2'
      intLumiab = lumi/1e+06
      leftText  = "FCC-hh Simulation (Delphes)"
      rightText = "#sqrt{s} = 100 TeV,   L = "+str(intLumiab)+" ab^{-1}"
      ylabel = "events"
      logY=True
      
      unit = 'GeV'
      if 'TeV' in str(title):
          unit = 'TeV'
      
      if unit in str(title):
          bwidth=h_ini.GetBinWidth(1)
          if bwidth.is_integer():
              ylabel+=' / '+str(int(bwidth))+' '+str(unit)
          else:
              ylabel+=' / '+str(float(bwidth))+' '+str(unit)
      
      
      ##########
      canvas = r.TCanvas(hist, hist, 600, 600)
      canvas.SetLogy(logY)
      canvas.SetTicks(1,1)
      canvas.SetLeftMargin(0.14)
      canvas.SetRightMargin(0.08)
      r.gStyle.SetOptStat(0)
      
      leg = r.TLegend(0.60,0.70,0.86,0.88)
      leg.SetFillColor(0)
      leg.SetFillStyle(0)
      leg.SetLineColor(0)
      leg.SetShadowColor(10)
      leg.SetTextSize(0.035)
      leg.SetTextFont(42)
      leg.AddEntry(h_ini,sample+" initial","lpe")
      leg.AddEntry(h_fit,sample+" fit","f")
      
      h_ini.GetYaxis().SetTitleOffset(1.95)
      h_ini.GetXaxis().SetTitleOffset(1.40)
      h_ini.SetTitle("")
      h_ini.GetXaxis().SetTitle(title)
      h_ini.GetYaxis().SetTitle(ylabel)
      
      h_ini.Scale(lumi)
      h_fit.Scale(lumi)
      
      maxh = h_ini.GetMaximum()
      minh = h_ini.GetMinimum()
      
      if logY:
          h_ini.SetMaximum(1000*maxh)
      #    h_ini.SetMinimum(0.000001*maxh)
      else:
          h_ini.SetMaximum(2.0*maxh)
          h_ini.SetMinimum(0.)
      
      h_ini.Draw()
      h_fit.Draw("same")
      leg.Draw("same")
      h_ini.Draw("same")
      
      Text = r.TLatex()
      
      Text.SetNDC()
      Text.SetTextAlign(31);
      Text.SetTextSize(0.04)
      
      text = '#it{' + leftText +'}'
      
      Text.DrawLatex(0.90, 0.92, text)
      
      rightText = re.split(",", rightText)
      text = '#bf{#it{' + rightText[0] +'}}'
      
      Text.SetTextAlign(12);
      Text.SetNDC(r.kTRUE)
      Text.SetTextSize(0.04)
      Text.DrawLatex(0.18, 0.83, text)
      
      text = '#bf{#it{' + rightText[1] +'}}'
      Text.SetTextSize(0.035)
      Text.DrawLatex(0.18, 0.78, text)
      
      canvas.RedrawAxis()
      canvas.GetFrame().SetBorderSize( 12 )
      canvas.Modified()
      canvas.Update()
      
      canvas.Print(ana+"_"+hist+"_fit.eps")

