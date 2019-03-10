FlatTreeAnalyzer
================
This scripts allows to easily design an analysis based on produced flat trees with the [Heppy](https://github.com/HEP-FCC/heppy) framework.


Table of contents
=================
  * [FlatTreeAnalyzer](#flattreeanalyser)
  * [Table of contents](#table-of-contents)
  * [Clone and initialisation](#clone-and-initilisation)
 

Clone and initialisation
========================

If you do not attempt to contribute to the FCChhAnalyses repository, simply clone it:
```
git clone git@github.com:FCC-hh-framework/FlatTreeAnalyzer.git
```

If you aim at contributing to the heppy repository, you need to fork and then clone the forked repository:
```
git clone git@github.com:YOURGITUSERNAME/FlatTreeAnalyzer.git
```

then initialize:

```
source ./init.sh
```

Analyses are run the following way:
```
./bin/analyze.py -n [analysis_name_in_heppy] -c [heppy_cfg] -t [heppy_tree_location] -o [output_dir] -p [analysis_parameters] -j [proc_dict]
```

```
./bin/analyze.py -n Zprime_ttbar -c ../heppy/FCChhAnalyses/HELHC/Zprime_ttbar/analysis.py -t /eos/experiment/fcc/helhc/analyses/Zprime_ttbar/heppy_outputs/helhc_v01/ -o /eos/experiment/fcc/helhc/analyses/Zprime_ttbar/FlatTreeAnalyzer_outputs/helhc_v01/ -p templates/HELHC/Zprime_ttbar.py -j /afs/cern.ch/work/h/helsens/public/FCCDicts/FCC_procDict_fcc_v02.json 
```
To run with multi-threads, simply add "-m" to the execution line


LSF submission
=================

It is also possible to send one lxbatch job per signal hypothesis. Each hypothesis will then run on a separate node
(multi-threading on that node is allowed). For instance:


```
python bin/analyze.py \
  -n tth_boosted \
  -c ../../../FCCSW/heppy/FCChhAnalyses/tth_boosted/analysis.py \
  -t /eos/user/s/selvaggi/heppyTrees/tth_boosted/ \
  -p templates/FCC/test_lsf.py \
  -j /afs/cern.ch/work/h/helsens/public/FCCDicts/FCC_procDict_fcc_v02.json \
  -o test_lsf \
  --nev 1000 \
  --multi_threading \
  --lsf \
  --queue 8nh \
  --force \
```

In order to collect jobs when running is over re-run the exact same command. 
If some jobs has failed, the script will automatically re-submit them.
When all jobs are completed, they will be collected and stored in the output directory specified by the ```-o``` option,
and the yield tables and final plots will be produced.

After every plot is done, you can clean LSF junk with the ```--cleanlsf``` option.
