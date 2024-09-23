#!/usr/bin/env python3
import sys
import glob
import json

from os.path import (
    basename,
    dirname,
    join,
    splitext
)

def json_of_file(path):
    with open(path, 'r') as fd:
        return json.load(fd)

def gen_sink_locations(pkg, conf):
    for vuln in conf["vulnerability"]["vulnerability_location"]:
        if "sink" in vuln:
            yield vuln["sink"]["file"]
        elif "block" in vuln:
            yield vuln["block"]["file"]
        else:
          print(f"Could not find file of sink for package: {pkg}")
          continue

output = "index.json" if sys.argv[1] is None else sys.argv[1]
configs = glob.glob(join("packages", "**", "*.json"), recursive=True)

results = {}
for conf_path in configs:
    conf = json_of_file(conf_path)
    dir_pkg = dirname(conf_path)
    dir_cwe = dirname(dir_pkg)
    if dir_cwe not in results:
        results[dir_cwe] = []

    package_link = conf["correct_package_link"]
    package_name = basename(package_link)
    package_name, ext = splitext(package_name)
    # assert(ext == ".tgz" or ext == ".gz" or ext == ".zip")
    relative_package_name = join(basename(dir_pkg), package_name)
    for file in gen_sink_locations(relative_package_name, conf):
        file = join(relative_package_name, file)
        if file not in results[dir_cwe]:
            results[dir_cwe].append(file)

with open(output, 'w') as fd:
    json.dump(results, fd, indent=2)

exit(0)
