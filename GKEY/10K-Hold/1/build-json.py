#!/usr/bin/env python

import json
from collections import defaultdict


with open('juno-osmo-1.txt') as fin:
    allocations = defaultdict(lambda: {'amount': 0, 'assets': ['glto']})
    receivers = []
    fin.readline() # skip header line
    for line in fin.readlines():
        [juno_addr, juno_amount, _osmo_addr, osmo_amount, _total_amount] = line.split()
        amount = int(0.0089 * 1e6)
        allocations[juno_addr]['amount'] = str(amount)
        receivers.append({"address": juno_addr, "amount": str(amount)})
            
with open('allocations.json', 'w') as allocations_file:
    json.dump(allocations, allocations_file)

with open('receivers.json', 'w') as receivers_file:
    json.dump(receivers, receivers_file)
