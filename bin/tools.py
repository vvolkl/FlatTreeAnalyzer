#!/usr/bin/env python
from __future__ import division
import ROOT, collections, os, sys
from ROOT import TFile, TTree, gROOT, TH1D, TH2D, kRed, TLegend, THStack, TVector2,  TGraph, TMultiGraph
from math import sqrt
import warnings
warnings.filterwarnings(action="ignore", category=RuntimeWarning, message="creating converter.*")
warnings.filterwarnings(action="ignore", category=RuntimeWarning, message="Deleting canvas.*")
warnings.filterwarnings(action="ignore", category=RuntimeWarning, message="Replacing existing*")



#_________________________________________
class CutSelector:

    #_____________________________________________________________________________________________________
    def __init__(self, tree, cuts):
        self.cuts = cuts
        self.formula = ROOT.TTreeFormula("Cut_formula", cuts, tree)

    #_____________________________________________________________________________________________________
    def evaluate(self, tree, event):
        # Important otherwise the vector is not loaded correctly
        self.formula.GetNdata()
        return self.formula.EvalInstance(event)

#_____________________________________________
class Process:

    #_____________________________________________________________________________________________________
    def __init__(self, name, tree="", nevents=-1, sumw=-1,xsec=-1., effmatch=1., kfactor=1.):

        self.name = name
        self.rt = tree
        self.n = nevents
        self.x = xsec # in pb
        self.e = effmatch
        self.k = kfactor
        self.s = sumw
        self.w = kfactor*xsec*effmatch/nevents #weight events /pb
        if sumw<nevents:
            self.w = kfactor*xsec*effmatch/sumw
        self.sv = collections.OrderedDict()

    #_____________________________________________________________________________________________________
    def setName(self, name):
        self.name = name
        nsel = 0
        for s in self.sv.keys():
            selstr = 'sel{}'.format(int(nsel))
            nsel += 1
            for v in self.sv[s].keys():
              hname = '{}_{}_{}'.format(name, selstr, v)
              self.sv[s][v].SetName(hname)

    #_____________________________________________________________________________________________________
    def run(self, selections, dv, ch='', name=''):

        # initialize dictionary selection: list of histograms
        if name=='':
            name = self.name
            nsel = 0
            for s in selections:
                self.sv[s] = collections.OrderedDict()
                selstr = 'sel{}'.format(int(nsel))
                nsel += 1
            
                for v in dv.keys() :
                    hname = '{}_{}_{}'.format(name, selstr, v)
                    self.sv[s][v] = TH1D(hname,hname+";"+dv[v]["title"]+";",dv[v]["bin"],dv[v]["xmin"],dv[v]["xmax"])
                    self.sv[s][v].Sumw2()


        rf = TFile(self.rt)
        t = rf.Get("events")
        for s in selections:
            # filter tree according to selection
            nf = TFile("tmp%s%s.root"%(ch,name),"recreate")
            rt = t.CopyTree(s)
            #rt = t

            # loop over events
            numberOfEntries = rt.GetEntries()
            #numberOfEntries = 100
            print 'number of events:', numberOfEntries
            for entry in xrange(numberOfEntries) :
                if (entry+1)%500 == 0: 
                    sys.stdout.write( '... %i events processed ...\r'%(entry+1))
                    sys.stdout.flush()

                rt.GetEntry(entry)
                weight = self.w * getattr(rt,"weight")
                for v in dv.keys():
                    self.sv[s][v].Fill(getattr(rt,dv[v]["name"]), weight)
            os.system('rm tmp%s%s.root'%(ch,name))

    #_____________________________________________________________________________________________________
    def getYields(self):
        yld = dict()
        for s in self.sv.keys():
            if not self.sv[s]:
                print 'you need to define at least one observable to run this analysis ...'
            # access random element to compute yield and error
            else:
                hist = self.sv[s].itervalues().next()
                # get values from first histograms
                err = ROOT.Double()      
                yld[s] = [hist.IntegralAndError(0, hist.GetNbinsX()+1, err), err]
        return yld

    #_____________________________________________________________________________________________________
    # necessary for adding processes 
    def add(self, other):
        for s in self.sv.keys():
            for v in self.sv[s].keys():
               self.sv[s][v].Add(other.sv[s][v])

#_____________________________________________________________________________________________________
def selectionDict(selections):
    
    seldict = collections.OrderedDict()
    for i in xrange(len(selections)):
       seldict[i] = selections[i]
    return seldict

#_____________________________________________________________________________________________________
def producePlots(selections, groups, colors, variables, unc, name, lumi, version, run_full, analysisDir, MT):
    
    name = name.replace("{", "")
    name = name.replace("}", "")
    name = name.replace(" ", "")
    name = name.replace("_", "")
    name = name.replace("=", "_")
    
    print '======================================================================================'
    print '======================================================================================'
    print ''
    print 'Running full analysis:', name
    print ''
    print '======================================================================================'
    print '======================================================================================'
    
    proclist = []
    for label, listproc in groups.iteritems():
	for proc in listproc:
            proclist.append(proc)
    
    seldict = selectionDict(selections)
    selections = seldict.values()

    pdir = "{}/plots_{}/".format(analysisDir,name)
    rdir = "{}/root_{}/".format(analysisDir,name)

    # if analysis has not been ran before
    if run_full:

        if MT:  runAnalysisMT(proclist, selections, variables, groups, name)
        else:   runAnalysis(proclist, selections, variables)

       ### prepare outputs
        os.system("mkdir -p {}".format(pdir))
        os.system("mkdir -p {}".format(rdir))

        processes = []
        for label, procs in groups.items():
            mainproc = procs[0]
            mainproc.setName(label)
            if len(procs) > 0:
                for i in range(1,len(procs)):
                    mainproc.add(procs[i])
                processes.append(mainproc)

        hfile = ROOT.TFile("{}/histos.root".format(rdir),"RECREATE")
        saveHistos(processes, selections, variables, hfile)
        hfile.Close()

    processes = groups.keys()
    hfile = ROOT.TFile("{}/histos.root".format(rdir))
    
    printYieldsFromHistos(processes, selections, variables, unc, lumi, hfile)

    produceStackedPlots(processes, selections, variables, colors, lumi, pdir, version, False, False, hfile)
    produceStackedPlots(processes, selections, variables, colors, lumi, pdir, version, True, False, hfile)
    produceStackedPlots(processes, selections, variables, colors, lumi, pdir, version, False, True, hfile)
    produceStackedPlots(processes, selections, variables, colors, lumi, pdir, version, True, True, hfile)

    print '======================================================================================'
    print '======================================================================================'
    print ''
    print 'DONE'
    print ''
    print '======================================================================================'
    print '======================================================================================'


import multiprocessing as mp

#_____________________________________________________________________________________________________
def runMT_pool(args=('','','','')):
    proc,selections,variables, sh=args
    print "START %s" % (proc.name)
    proc.run(selections, variables, proc.name, sh)
    return proc
    print "END %s" % (proc.name)


#_____________________________________________________________________________________________________
def runMT_join(proc,selections, variables):
    print "START %s" % (proc.name)
    proc.run(selections, variables, proc.name)
    print "END %s" % (proc.name)


#_____________________________________________________________________________________________________
def runAnalysisMT(listOfProcesses, selections, variables, groups, name):
    print 'NUMBER OF CORES    ',mp.cpu_count()
    print ''
    print 'Start looping on process trees:'
    print ''
    threads = []
    for proc in listOfProcesses:
        print '---------------------------'
        print proc.name
        print '---------------------------'
        print ''

        nsel = 0
        for s in selections:
            proc.sv[s] = collections.OrderedDict()
            selstr = 'sel{}'.format(int(nsel))
            nsel += 1
            for v in variables.keys() :
                hname = '{}_{}_{}'.format(proc.name, selstr, v)
                proc.sv[s][v] = TH1D(hname,hname+";"+variables[v]["title"]+";",variables[v]["bin"],variables[v]["xmin"],variables[v]["xmax"])
                proc.sv[s][v].Sumw2()


    #SOLUTION 1
        threads.append((proc, selections, variables, name))
    pool = mp.Pool(16)
    histos_list = pool.map(runMT_pool,threads) 


    for label in groups:
        toadd=[]
        for p in groups[label]:
            for h in histos_list:
                if p.name==h.name:
                    toadd.append(h)
        groups[label]=toadd
                    
    #SOLUTION 2
    #    thread = mp.Process(target=runMT_join,args=(proc, selections, variables,))
    #    thread.start()
    #    threads.append(thread)
    #for proc in threads:
    #    proc.join()

#_____________________________________________________________________________________________________
def runAnalysis(listOfProcesses, selections, variables):
    print ''
    print 'Start looping on process trees:'
    print ''
        
    for proc in listOfProcesses:
        print '---------------------------'
        print proc.name
        print '---------------------------'
        print ''
        proc.run(selections, variables)

#____________________________________________________________________________________________________
def saveHistos(processes, selections, variables, output):

    print ''
    print 'Saving histograms in', output.GetName(), 'file ...'
    for proc in processes:
        for sel in selections:
            for var in variables:
                output.cd()
                proc.sv[sel][var].Write()
    print 'DONE'
    output.Close()

#_____________________________________________________________________________________________________
def significance(s, es, b, eb):
    if s == 0 and b == 0:
        return 0.
    else:
        return s/sqrt(s + (s*es)**2 + b + (b*eb)**2)

#_____________________________________________________________________________________________________
def dMuOverMu(s, es, b, eb):
    if s == 0:
        return 1000.
    else:
        return 100*sqrt(s + (s*es)**2 + b + (b*eb)**2)/s

#_____________________________________________________________________________________________________
def printYields(listOfSignals, listOfBackgrounds, selections, uncertainties, intLumi):

    print ''    
    for sel in selections:
        intLumiab = intLumi/1e+06 
        print ''    
        print '===================================================================================='
        print '         selection:', sel
        print '===================================================================================='

        print ''    
        print '{:>20} {:>12} ({:>4} {:>3}) {:>20}'.format('process', 'yield', intLumiab, 'ab-1', 'stat. error')
        print '    ------------------------------------------------------------'

        # print signal yields
        s = 0
        es = 0
        for proc in listOfSignals:
            yld = proc.getYields()[sel][0]*intLumi
            err = proc.getYields()[sel][1]*intLumi
            s += yld
            es += err**2
            print '{:>20} {:>20} {:>20} {:>20}'.format(proc.name, round(yld,1), round(err,1))
        print '    ------------------------------------------------------------'
        print '{:>20} {:>20} {:>20}'.format('signal', round(s,3), round(sqrt(es),3))
        print ''    
        print ''    

        print ''    
        print '{:>20} {:>12} ({:>4} {:>3}) {:>20}'.format('process', 'yield', intLumiab, 'ab-1', 'stat. error')
        print '    ------------------------------------------------------------'

        # print background yields
        b = 0
        eb = 0
        for proc in listOfBackgrounds:
            yld = proc.getYields()[sel][0]*intLumi
            err = proc.getYields()[sel][1]*intLumi
            b += yld
            eb += err**2
            print '{:>20} {:>20} {:>20}'.format(proc.name, round(yld,1), round(err,1))
        print '    ------------------------------------------------------------'
        print '{:>20} {:>20} {:>20}'.format('background', round(b,3), round(sqrt(eb),3))
        print ''    
        print ''    

        # calculate significance and delta_mu/mu (uncertainty on the signal strength)
        print '{:>24} {:>20} {:>20}'.format('(sig_s, sig_b) (%)', 'significance', 'dmu/mu (%)')
        print '    ------------------------------------------------------------'
        for unc in uncertainties:
            sign = significance(s, unc[0], b, unc[1])
            rel_unc = dMuOverMu(s, unc[0], b, unc[1])
            print '{:>11} {:>7} {:>21} {:>20}'.format(round(unc[0]*100.,1), round(unc[1]*100.,1), round(sign,2), round(rel_unc,2))

#_____________________________________________________________________________________________________
def printYieldsFromHistos(processes, selections, variables, uncertainties, intLumi, hfile):

    print ''    
    nsel = 0
    for sel in selections:
        intLumiab = intLumi/1e+06 
        print ''    
        print '===================================================================================='
        print '         selection:', sel
        print '===================================================================================='

        print ''    
        print '{:>20} {:>12} ({:>4} {:>3}) {:>20} {:>12}'.format('process', 'yield', intLumiab, 'ab-1', 'stat. error', 'raw')
        print '    -------------------------------------------------------------------------------------'

        v = variables.keys()[0]
        selstr = 'sel{}'.format(int(nsel))
        nsel += 1
        
        nproc = 0
        b = 0
        eb = 0
        for p in processes:
            hname = '{}_{}_{}'.format(p, selstr, v)
            h = hfile.Get(hname)
            err = ROOT.Double()
            yld = h.IntegralAndError(0, h.GetNbinsX()+1, err)
            raw = h.GetEntries()

            yld *= intLumi
            err *= intLumi

            if nproc == 0:
                s = yld
                es = err
            else: 
                b += yld
                eb += (err**2)
                
            print '{:>20} {:>20} {:>20} {:>20}'.format(p, round(yld,1), round(err,1),raw)
            nproc += 1
        print '    -------------------------------------------------------------------------------------'
        print '{:>20} {:>20} {:>20}'.format('signal', round(s,3), round(sqrt(es),3))
        print '{:>20} {:>20} {:>20}'.format('background', round(b,3), round(sqrt(eb),3))

        print ''    
        print ''    

        # calculate significance and delta_mu/mu (uncertainty on the signal strength)
        print '{:>24} {:>20} {:>20}'.format('(sig_s, sig_b) (%)', 'significance', 'dmu/mu (%)')
        print '    ------------------------------------------------------------'
        for unc in uncertainties:
            sign = significance(s, unc[0], b, unc[1])
            rel_unc = dMuOverMu(s, unc[0], b, unc[1])
            print '{:>11} {:>7} {:>21} {:>20}'.format(round(unc[0]*100.,1), round(unc[1]*100.,1), round(sign,2), round(rel_unc,2))

#_____________________________________________________________________________________________________
def produceYieldPlots(processes, seldict, variables, uncertainties, intLumi, pdir, delphesVersion, hfile):

    print ''    
    print 'Preparing yield plots ...'    
    # prepare yield plots
    gr_sb = TGraph()
    mg_sign = TMultiGraph()
    mg_dmu = TMultiGraph()

    gr_sb.SetTitle(";p_{T}^{H} (min) [GeV]; S/B")
    mg_sign.SetTitle(";p_{T}^{H} (min) [GeV]; Significance = #frac{S}{#sqrt{S + #sigma_{S}^{2} + B + #sigma_{B}^{2}}}")
    mg_dmu.SetTitle(";p_{T}^{H} (min) [GeV]; #delta #mu / #mu (%)")

    grs_sign = {}
    grs_dmu = {}

    colors = []
    colors.append(ROOT.kBlack);
    colors.append(ROOT.kRed-9);
    colors.append(ROOT.kBlue-3);
    colors.append(ROOT.kGreen+2);
    colors.append(ROOT.kOrange-3);
    colors.append(ROOT.kYellow+2);
    colors.append(ROOT.kMagenta+1);

    index = 0
    gr_sb.SetLineColor(ROOT.kBlack)
    gr_sb.SetLineWidth(3)
    for unc in uncertainties:
        gr_sign = TGraph()
        gr_dmu = TGraph()
        gr_sign.SetLineColor(colors[index])
        gr_dmu.SetLineColor(colors[index])

        gr_sign.SetLineWidth(3)
        gr_dmu.SetLineWidth(3)
        gr_sign.SetMarkerSize(0.0001)
        gr_dmu.SetMarkerSize(0.0001)
        gr_sign.SetFillColor(0)
        gr_dmu.SetFillColor(0)

        grs_sign[index] = gr_sign
        grs_dmu[index] = gr_dmu
        index += 1

    # fill yield graphs
    nsel = 0
    
    maxsb = -999
    minsb = 999
    maxsig = -999
    minsig = 999
    maxdmu = -999
    mindmu = 999

    for cut in seldict.keys():
        index = 0
        v = variables.keys()[0]
        selstr = 'sel{}'.format(int(nsel))
        nproc = 0
        b = 0
        for p in processes:
            hname = '{}_{}_{}'.format(p, selstr, v)
            h = hfile.Get(hname)
            err = ROOT.Double()
            yld = h.IntegralAndError(0, h.GetNbinsX()+1, err)
            yld *= intLumi
            err *= intLumi
            
            if nproc == 0:
                s = yld
            else: 
                b += yld
            nproc += 1
        if b == 0:
           gr_sb.SetPoint(nsel,cut,0.)
           if 0 < minsb : minsb = 0.
           if 0 > maxsb : maxsb = 0.
        else:
           if s/b < minsb : minsb = s/b
           if s/b > maxsb : maxsb = s/b
           gr_sb.SetPoint(nsel,cut,s/b)
        for unc in uncertainties:
            sign = significance(s, unc[0], b, unc[1])
            rel_unc = dMuOverMu(s, unc[0], b, unc[1])
            if sign < minsig : minsig = sign
            if sign > maxsig : maxsig = sign
            if rel_unc < mindmu : mindmu = rel_unc
            if rel_unc > maxdmu : maxdmu = rel_unc
            
            grs_sign[index].SetPoint(nsel,cut,sign)
            grs_dmu[index].SetPoint(nsel,cut,rel_unc)
            
            title = '#sigma_{{S}}/S = {}, #sigma_{{B}}/B = {}'.format(unc[0], unc[1])
            
            grs_sign[index].SetTitle(title)
            grs_dmu[index].SetTitle(title)
            
            index += 1
        nsel += 1

    index = 0
    for unc in uncertainties:
        mg_sign.Add(grs_sign[index])
        mg_dmu.Add(grs_dmu[index])
        index += 1

    intLumiab = intLumi/1e+06 
    rt = 'RECO: Delphes-{}'.format(delphesVersion)
    lt = '#sqrt{{s}} = 100 TeV, L = {} ab^{{-1}}'.format(intLumiab)

    drawMultiGraph(mg_sign, 'optim_sign', lt, rt, pdir, minsig/10., maxsig*10., True)
    drawMultiGraph(mg_dmu, 'optim_dmu', lt, rt, pdir , mindmu/10., maxdmu*10., True)
    drawMultiGraph(gr_sb, 'optim_sb', lt, rt, pdir, minsb/10., maxsb*10., True,  False)
    print 'DONE'

#_____________________________________________________________________________________________________
def drawMultiGraph(mg, name, lt, rt, pdir, ymin, ymax, log, bl = True):

    myStyle()
    gROOT.SetBatch(True)
    ROOT.gStyle.SetOptStat(0000000)
    ROOT.gStyle.SetTextFont(132)

    canvas = ROOT.TCanvas('', '', 800,600) 

    ROOT.gPad.SetLeftMargin(0.20) ; 
    ROOT.gPad.SetRightMargin(0.05) ; 
    ROOT.gPad.SetBottomMargin(0.20) ; 
    ROOT.gStyle.SetOptStat(0000000);
    ROOT.gStyle.SetTextFont(132);
   
    Tleft = ROOT.TLatex(0.23, 0.92, lt) 
    Tleft.SetNDC(ROOT.kTRUE) 
    Tleft.SetTextSize(0.044) 
    Tleft.SetTextFont(132) 
    
    Tright = ROOT.TText(0.95, 0.92, rt) ;
    Tright.SetTextAlign(31);
    Tright.SetNDC(ROOT.kTRUE) 
    Tright.SetTextSize(0.044) 
    Tright.SetTextFont(132) 

    canvas.cd(0)
    
    mg.Draw("AL")
    mg.GetYaxis().SetLabelFont(132)
    mg.GetYaxis().SetTitleFont(132)
    mg.GetYaxis().SetLabelOffset(0.02)
    mg.GetYaxis().CenterTitle()
    mg.GetYaxis().SetNdivisions(505)
    mg.GetYaxis().SetTitleOffset(1.8)

    mg.GetXaxis().SetTitleFont(132)
    mg.GetXaxis().SetLabelFont(132)
    mg.GetXaxis().SetLabelOffset(0.02)
    mg.GetXaxis().SetTitleOffset(1.5)
    mg.GetXaxis().SetTitleSize(0.06)
    mg.GetYaxis().SetTitleSize(0.048)
    mg.GetXaxis().SetLabelSize(0.06)
    mg.GetYaxis().SetLabelSize(0.06)
    mg.SetMinimum(ymin)
    mg.SetMaximum(ymax)
    
    if log: ROOT.gPad.SetLogy()

    if bl:
        leg = canvas.BuildLegend(0.65,0.70,0.90,0.88)
        leg.SetTextFont(132) 
        leg.SetFillColor(0)
        leg.SetFillStyle(0)
        leg.SetLineColor(0)
        leg.Draw() 
    
    Tleft.Draw() 
    Tright.Draw() 
    canvas.Print('{}/{}.png'.format(pdir, name), 'png')
    
#___________________________________________________________________________
def produceStackedPlots(processes, selections, variables, colors, intLumi, pdir, delphesVersion, log, stacksig, hfile):
    
    print ''
    print 'Preparing distribution plots ...'

    myStyle()
    gROOT.SetBatch(True)

    intLumiab = intLumi/1e+06 

    yl = "Events"
    rt = "RECO: Delphes-{}".format(delphesVersion)
    lt = "#sqrt{{s}} = 100 TeV, L = {} ab^{{-1}}".format(intLumiab)

    ff = "png"

    logstr = ''
    if log:
       logstr = 'log'
    else:
       logstr = 'lin'
    
    stackstr = ''
    if stacksig:
       stackstr = 'stack'
    else:
       stackstr = 'nostack'

    hfile.cd()

    nsel = 0
    for s in selections:
        selstr = 'sel{}'.format(int(nsel))
        nsel += 1
        for v in variables.keys() :
             histos = []
             i = 0

             filename = '{}_{}_{}_{}'.format(v, selstr, stackstr, logstr)

             leg = TLegend(0.70,0.65,0.95,0.88)
             leg.SetFillColor(0)
             leg.SetFillStyle(0)
             leg.SetLineColor(0)

             cols = []
             for p in processes:
                 hname = '{}_{}_{}'.format(p, selstr, v)
                 h = hfile.Get(hname)
                 hh = TH1D.Clone(h)
                 hh.Scale(intLumi)
                 histos.append(hh)
                 cols.append(colors[p])
                 if i > 0: 
                     leg.AddEntry(hh,p,"f")
                 else: 
                     leg.AddEntry(hh,p,"l")
                 i+=1
             drawStack(filename, yl, leg, lt, rt, ff, pdir, log, stacksig, histos, cols)
    print 'DONE.'

#_____________________________________________________________________________________________________________
def drawStack(name, ylabel, legend, leftText, rightText, format, directory, logY, stacksig, histos, colors):

    canvas = ROOT.TCanvas(name, name, 800, 600) 
    
    font = 132
    
    ROOT.gPad.SetLeftMargin(0.20) ; 
    ROOT.gPad.SetRightMargin(0.10) ; 
    ROOT.gPad.SetBottomMargin(0.20) ; 
    ROOT.gStyle.SetOptStat(0000000);
    ROOT.gStyle.SetTextFont(font);
    
    Tleft = ROOT.TLatex(0.23, 0.82, leftText) 
    Tleft.SetNDC(ROOT.kTRUE) 
    Tleft.SetTextSize(0.044) 
    Tleft.SetTextFont(font) 
    
    Tright = ROOT.TText(0.90, 0.92, rightText) ;
    Tright.SetTextAlign(31);
    Tright.SetNDC(ROOT.kTRUE) 
    Tright.SetTextSize(0.044) 
    Tright.SetTextFont(font) 
    
    # first retrieve maximum 
    sumhistos = histos[0].Clone()
    iterh = iter(histos)
    next(iterh)
    
    for h in iterh:
      sumhistos.Add(h)

    maxh = sumhistos.GetMaximum()
    minh = sumhistos.GetMinimum()

    if logY: 
       canvas.SetLogy(1)

    # define stacked histo
    hStack = ROOT.THStack("hstack","")

    # first plot backgrounds
         
    histos[1].SetLineWidth(0)
    histos[1].SetFillColor(colors[1])
    
    hStack.Add(histos[1])
    
    # now loop over other background (skipping first)
    iterh = iter(histos)
    next(iterh)
    next(iterh)
    
    k = 2
    for h in iterh:
       h.SetLineWidth(0)
       h.SetLineColor(ROOT.kBlack)
       h.SetFillColor(colors[k])
       hStack.Add(h)
       k += 1
    
    
    # finally add signal on top
    histos[0].SetLineWidth(3)
    histos[0].SetLineColor(colors[0])
    
    if stacksig:
        hStack.Add(histos[0])

    hStack.Draw("hist")

    hStack.GetXaxis().SetTitleFont(font)
    hStack.GetXaxis().SetLabelFont(font)
    hStack.GetXaxis().SetTitle(histos[1].GetXaxis().GetTitle())
    hStack.GetYaxis().SetTitle(ylabel)
    hStack.GetYaxis().SetTitleFont(font)
    hStack.GetYaxis().SetLabelFont(font)
    hStack.GetXaxis().SetTitleOffset(1.5)
    hStack.GetYaxis().SetTitleOffset(1.6)
    hStack.GetXaxis().SetLabelOffset(0.02)
    hStack.GetYaxis().SetLabelOffset(0.02)
    hStack.GetXaxis().SetTitleSize(0.06)
    hStack.GetYaxis().SetTitleSize(0.06)
    hStack.GetXaxis().SetLabelSize(0.06)
    hStack.GetYaxis().SetLabelSize(0.06)
    hStack.GetXaxis().SetNdivisions(505);
    hStack.GetYaxis().SetNdivisions(505);
    hStack.SetTitle("") 
    #hStack.SetMaximum(1.5*maxh) 
    
    if logY:
        hStack.SetMaximum(100*maxh)
        hStack.SetMinimum(0.00000001*maxh)
    else:
        hStack.SetMaximum(1.7*maxh)
        hStack.SetMinimum(0.)

    if not stacksig:
        histos[0].Draw("same hist")
   
    legend.SetTextFont(font) 
    legend.Draw() 
    Tleft.Draw() 
    Tright.Draw() 
    printCanvas(canvas, name, format, directory) 

#____________________________________________________
def printCanvas(canvas, name, format, directory):

    if format != "":
        if not os.path.exists(directory) :
                os.system("mkdir "+directory)
        outFile = os.path.join(directory, name) + "." + format
        canvas.Print(outFile)

#____________________________________________________
def myStyle():
    ROOT.gStyle.SetFrameBorderMode(0)
    ROOT.gStyle.SetCanvasBorderMode(0)
    ROOT.gStyle.SetPadBorderMode(0)

    ROOT.gStyle.SetFrameFillColor(0)
    ROOT.gStyle.SetPadColor(0)
    ROOT.gStyle.SetCanvasColor(0)
    ROOT.gStyle.SetTitleColor(1)
    ROOT.gStyle.SetStatColor(0)

    # set the paper & margin sizes
    ROOT.gStyle.SetPaperSize(20,26)
    ROOT.gStyle.SetPadTopMargin(0.10)
    ROOT.gStyle.SetPadRightMargin(0.03)
    ROOT.gStyle.SetPadBottomMargin(0.13)
    ROOT.gStyle.SetPadLeftMargin(0.125)
    ROOT.gStyle.SetPadTickX(1)
    ROOT.gStyle.SetPadTickY(1)
    
    ROOT.gStyle.SetTextFont(42) #132
    ROOT.gStyle.SetTextSize(0.09)
    ROOT.gStyle.SetLabelFont(42,"xyz")
    ROOT.gStyle.SetTitleFont(42,"xyz")
    ROOT.gStyle.SetLabelSize(0.045,"xyz") #0.035
    ROOT.gStyle.SetTitleSize(0.045,"xyz")
    ROOT.gStyle.SetTitleOffset(1.15,"y")
    
    # use bold lines and markers
    ROOT.gStyle.SetMarkerStyle(8)
    ROOT.gStyle.SetHistLineWidth(2)
    ROOT.gStyle.SetLineWidth(1)
    #ROOT.gStyle.SetLineStyleString(2,"[12 12]") // postscript dashes

    # do not display any of the standard histogram decorations
    ROOT.gStyle.SetOptTitle(1)
    ROOT.gStyle.SetOptStat(0) #("m")
    ROOT.gStyle.SetOptFit(0)
    
    #ROOT.gStyle.SetPalette(1,0)
    ROOT.gStyle.cd()
    ROOT.gROOT.ForceStyle()
