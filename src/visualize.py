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
top_ten = sorted(items[:11] or items.most_common(10), reverse=False)
keys = list(top_ten.keys())
values = list(top_ten.values())
plt.bar(keys, values)
plt.xlabel('data keys')
plt.ylabel('frequency of the keys in the data')
plt.title("Bar chat of key and it's frequency.")
plt.savefig('../visuals/figs',dpi='figure', format='png')
for k,v in items:
    print(k,':',v)