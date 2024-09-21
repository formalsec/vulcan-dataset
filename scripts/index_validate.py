#!/usr/bin/env python3
import sys
import json

from os.path import join, exists

def json_of_file(path):
    with open(path, 'r') as fd:
        return json.load(fd)

index = "./index.json" if sys.argv [1] is None else sys.argv[1]
index = json_of_file(index)
build = "./_build"
errors = []
for (pkg_cwe, paths) in index.items():
    for path in paths:
        full_path = join(build, pkg_cwe, path)
        if not exists(full_path):
            errors.append(full_path)

if len(errors) > 0:
    for full_path in errors:
        print(f"File {full_path} does not exist!", file=sys.stderr)
    exit(1)
exit(0)
