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
./bin/analyze.py -n Zprime_ttbar -c ../heppy/FCChhAnalyses/HELHC/Zprime_ttbar/analysis.py -t /eos/experiment/fcc/helhc/analyses/Zprime_ttbar/heppy_outputs/helhc_v01/ -o /eos/experiment/fcc/helhc/analyses/Zprime_ttbar/FlatTreeAnalyzer_outputs/helhc_v01/ -p templates/HELHC/Zprime_ttbar.py -j /afs/cern.ch/work/h/helsens/public/FCCDicts/procDict_helhc_v01.json
```
To run with multi-threads, simply add "-m" to the execution line

To save time
