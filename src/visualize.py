#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_path',required=True)
parser.add_argument('--key',required=True)
parser.add_argument('--percent',action='store_true')
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
print(keys)
print(values)
fig = plt.figure(figsize = (10,5))
plt.bar(keys, values)
plt.xlabel('data keys')
plt.ylabel('frequency of the keys in the data')
plt.title("Bar chat of key and it's frequency.")
plt.rcParams['savefig.directory'] = '../visuals/figs'
plt.savefig(f"'{args.key}.png'" , dpi=300, format='png')

