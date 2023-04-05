#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_path',required=True)
parser.add_argument('--key',required=True)
parser.add_argument('--percent',action='store_true')
parser.add_argument('--filename', required=True)
args = parser.parse_args()

# imports
import os
import json
from collections import Counter,defaultdict
import matplotlib.pyplot as plt

# open the input path
with open(args.input_path) as f:
    counts = json.load(f)

# normalize the counts by the total values
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]

# print the count values
items = sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=True)
top_ten = items[:10]
keys = []
values = []
for k,v in top_ten:
    keys.append(k)
    values.append(v)
keys.reverse()
values.reverse()
fig = plt.figure(figsize = (10,5))
plt.bar(keys, sorted(values))
plt.xlabel('data keys')
plt.ylabel('frequency of {args.key} in the data')
plt.title(f"Bar chat of {args.key} and it's frequency.")
plt.savefig('./visuals/figs/'+f"{args.filename}.png", format='png')
