#!/usr/bin/env python3
import os
import glob
import json
import shutil

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

output = "packages_by_cwe"
configs = glob.glob("packages/**/*.json", recursive=True)

for conf_path in configs:
    conf = json_of_file(conf_path)
    cwes = get_cwes(conf)
    pkg_src = os.path.dirname(conf_path)
    pkg_base = os.path.basename(pkg_src)
    for cwe in cwes:
        cwe = cwe.strip()
        pkg_dst = os.path.join(output, cwe, pkg_base)
        shutil.copytree(pkg_src, pkg_dst)

print("All done.")
