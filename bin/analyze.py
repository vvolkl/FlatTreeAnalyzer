#!/usr/bin/env python
import subprocess, glob, optparse, json, ast, os, sys, collections
from tools import producePlots, Process
from pprint import pprint
import ntpath
import importlib
import yaml

#_____________________________________________________________________________
def options():
    parser = optparse.OptionParser(description="analysis parser")
    parser.add_option('-n', '--analysis_name', dest='analysis_name', type=str, default='')
    parser.add_option('-c', '--heppy_cfg', dest='heppy_cfg', type=str, default='')
    parser.add_option('-j', '--proc_file_json', dest='proc_file_json', type=str, default='/afs/cern.ch/work/h/helsens/public/FCCDicts/procDict.json')
    parser.add_option('-t', '--heppy_tree_dir', dest='heppy_tree_dir', type=str, default='')
    parser.add_option('-o', '--analysis_output', dest='analysis_output', type=str, default='')
    parser.add_option('-p', '--param_file', dest='param_file', type=str, default='')
    parser.add_option('-m', '--multi_threading', dest='MT', default=False, action='store_true')
    parser.add_option('-l', '--latex_table', dest='latex_table', default=False, action='store_true')
    parser.add_option('--no_plots', dest='no_plots', default=False, action='store_true')

    return parser.parse_args()

#______________________________________________________________________________
def main():
    
    ops, args = options()

    args = split_comma_args(args)

    # give this analysis a name
    analysisName = ops.analysis_name

    # heppy analysis configuration
    heppyCfg = ops.heppy_cfg

    # process dictionary
    processDict = ops.proc_file_json

    # heppy trees location directory
    treeDir = ops.heppy_tree_dir

    # analysis dir
    analysisDir = ops.analysis_output

    # param file
    paramFile = ops.param_file

    module_path = os.path.abspath(paramFile)
    module_dir = os.path.dirname(module_path)
    base_name = os.path.splitext(ntpath.basename(paramFile))[0]
   
    sys.path.insert(0, module_dir)
    param = importlib.import_module(base_name)
    
    # tree location
    treePath = '/heppy.FCChhAnalyses.{}.TreeProducer.TreeProducer_1/tree.root'.format(analysisName)

    #multi-threading
    MT = ops.MT


    print treeDir

    # retrieve list of processes from heppy cfg
    processes = []
    with open(heppyCfg) as f:
        lines = f.readlines()
        for l in lines:
            if 'splitFactor' in l:
                processes.append(l.rsplit('.', 1)[0])

    with open(processDict) as f:
        procDict = json.load(f)
    
    # prepare analysis dir
    os.system('mkdir -p {}'.format(analysisDir))

    ### produce process dictionnaries
    if not MT:
        for sh in param.selections.keys():

            block = collections.OrderedDict()

            formBlock(processes, procDict, param.signal_groups,param.background_groups,sh, treeDir, treePath, block)

        ### run analysis
            producePlots(param.selections[sh], 
                         block, 
                         param.colors, 
                         param.variables, 
                         param.variables2D, 
                         param.uncertainties, 
                         sh, 
                         param.intLumi, 
                         param.delphesVersion, 
                         param.runFull,
                         analysisDir,
                         MT,
                         latex_table=ops.latex_table,
                         no_plots=ops.no_plots
                         )
    else:
        runMT(processes, procDict, param, treeDir, treePath, analysisDir, MT, ops)


import multiprocessing as mp
#_____________________________________________________________________________________________________
def runMT(processes, procDict, param, treeDir, treePath, analysisDir, MT, ops):
    threads = []
    for sh in param.selections.keys():

        block = collections.OrderedDict()
        formBlock(processes, procDict, param.signal_groups,param.background_groups,sh, treeDir, treePath, block)
        thread = mp.Process(target=runMT_join,args=(block, param, sh,analysisDir, MT, ops ))
        thread.start()
        threads.append(thread)
    for proc in threads:
        proc.join()

 

#_____________________________________________________________________________________________________
def runMT_join(block, param, sh, analysisDir, MT, ops):
    print "START %s" % (sh)
    producePlots(param.selections[sh], 
                 block, 
                 param.colors, 
                 param.variables, 
                 param.variables2D, 
                 param.uncertainties, 
                 sh, 
                 param.intLumi, 
                 param.delphesVersion, 
                 param.runFull,
                 analysisDir,
                 MT,
                 latex_table=ops.latex_table,
                 no_plots=ops.no_plots)

    print "END %s" % (sh)


#_____________________________________________________________________________________________________
def runMT_pool(args=('','','')):
    print "START %s" % (sh)
    block, param, sh,analysisDir, MT, ops=args
    producePlots(param.selections[sh], 
                 block, 
                 param.colors, 
                 param.variables, 
                 param.variables2D, 
                 param.uncertainties, 
                 sh, 
                 param.intLumi, 
                 param.delphesVersion, 
                 param.runFull,
                 analysisDir,
                 MT,
                 latex_table=ops.latex_table,
                 no_plots=ops.no_plots)
    print "END %s" % (sh)

#______________________________________________________________________________
def formBlock(processes, procdict, sb, bb, shyp, treedir, treepath, block):
    
    for label, procs in sb.iteritems():
       if label == shyp:
           block[shyp] = fillBlock(procs, processes, procdict, treedir, treepath)
    for label, procs in bb.iteritems():
       block[label] = fillBlock(procs, processes, procdict, treedir, treepath)

#______________________________________________________________________________
def fillBlock(procs, processes, procdict, treedir, treepath):
     blocklist = []
     for procstr in procs:
         for pname in processes:
             if procstr in pname:
                 xsec = procdict[pname]['crossSection']
                 nev = procdict[pname]['numberOfEvents']
                 sumw = procdict[pname]['sumOfWeights']
                 eff = procdict[pname]['matchingEfficiency']
                 kf = procdict[pname]['kfactor']
                 matched_xsec = xsec*eff
                 tree = '{}/{}/{}'.format(os.path.abspath(treedir), pname, treepath)
                 
                 #read from heppy yaml file job efficiency       
                 filestr = os.path.abspath(treedir) + '/' + pname + '/processing.yaml'
                 corrFac = 1.
                 with open(filestr, 'r') as stream:
                     try:
                        dico = yaml.load(stream)
                        corrFac *= float(dico['processing']['nfiles'])/dico['processing']['ngoodfiles']                  
                     except yaml.YAMLError as exc:
                        print(exc)                 
                 sumw *= corrFac
                 nev *= corrFac    
                 blocklist.append(Process(pname,tree,nev,sumw,xsec,eff,kf))
     return blocklist

#______________________________________________________________________________
def split_comma_args(args):
    new_args = []
    for arg in args:
        new_args.extend( arg.split(',') )
    return new_args
#______________________________________________________________________________
if __name__ == '__main__': 
    main()
