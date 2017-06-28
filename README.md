# FlatTreeAnalyzer

This scripts allows to easily design an analysis based on produced flat trees with the [Heppy](https://github.com/cbernet/heppy) framework.

First initialize:

```
source ./init.sh
```

Example:
```
./bin/analyze.py -n [analysis_name_in_heppy] -c [heppy_cfg] -t [heppy_tree_location] -o [output_dir] -p [analysis_parameters] -j [proc_dict]
```
