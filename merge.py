#!/usr/bin/env python
"""
Script to download each airdrop snapshot file (for Atom, Juno, etc.), merge
them, and write the merged data out as a json file.
"""

import json
import csv
import sys

from urllib.request import urlopen


def main(output_filepath: str = "./merged.json"):
    url_template = "https://raw.githubusercontent.com/Gelotto/airdrop-snapshot-info/main/{}.txt"
    assets = ["atom", "juno", "scrt", "neta", "osmo", "stars"]
    prefixes = ["cosmos", "juno", "secret", "neta", "osmo", "stars"]
    merged = {}

    print("merging airdrop CSV files...")

    for asset, prefix in zip(assets, prefixes):
        csv_file_url = url_template.format(asset)
        print(f"fetching {csv_file_url}...")
        csv_lines = [line.decode() for line in urlopen(csv_file_url)]
        for addr, _, amount in csv.reader(csv_lines[1:]):
            merged[addr] = float(amount)

    print(f"writing merged data to {output_filepath}...")

    with open(output_filepath, "w") as output_json_file:
        json.dump(merged, output_json_file)


if __name__ == "__main__":
    sys.exit(main())
