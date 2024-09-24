#!/usr/bin/env python3
import re
import sys
import glob
import json

from os.path import basename, dirname, join, splitext

def json_of_file(path):
    with open(path, 'r') as fd:
        return json.load(fd)

def get_cwes(report):
    correct_cwe = report["correct_cwe"]
    if isinstance(correct_cwe, str):
        return [ correct_cwe ]
    elif isinstance(correct_cwe, list):
        return correct_cwe
    else:
        assert(False)

results = {}
configs = glob.glob("packages/**/*.json", recursive=True)
pattern = r"([a-zA-Z0-9-]+)-(\d+\.\d+\.\d+(?:-[a-zA-Z]+\.\d+)?)"

output = "index.json" if len(sys.argv) < 2 else sys.argv[1]

for conf_path in configs:
    conf = json_of_file(conf_path)
    cwes = get_cwes(conf)
    package_link = conf["correct_package_link"]
    package_name = basename(package_link)
    package_name, _ = splitext(package_name)
    match = re.search(pattern, package_name)
    if match:
        package_name = match.group(1)
        version = match.group(2)
        for cwe in cwes:
            cwe = cwe.strip()
            if cwe not in results:
                results[cwe] = []
            results[cwe].append({ "id": package_name, "version": version})
    else:
        print("Ignoring:", package_name, file=sys.stderr)

with open(output, 'w') as fd:
    json.dump(results, fd, indent=2)

print("All done.", file=sys.stderr)
