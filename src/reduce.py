#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_paths',nargs='+',required=True)
parser.add_argument('--output_path',required=True)
args = parser.parse_args()

# imports
import os
import json
from collections import Counter,defaultdict

# load each of the input paths
total = defaultdict(lambda: Counter())
for path in args.input_paths:
    with open(path) as f:
        tmp = json.load(f)
        # combining covid* into one key and corona* into one key
        for k in tmp:
            if 'covid' in k:
                total['#covid19'] += tmp[k]
            elif 'corona' in k:
                total['#corona'] += tmp[k]
            else:
                total[k] += tmp[k]

# write the output path
with open(args.output_path,'w') as f:
    f.write(json.dumps(total))
