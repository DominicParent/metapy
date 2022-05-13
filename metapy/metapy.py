import argparse
import json
import os

# Takes a path and loads it from json to python dictionaries.
def read_meta(path_to_file):
    with open(path_to_file, "r") as f:
        meta = json.load(f)

    return meta

# Writes a python dictionary to an indented json file.
def write_meta(meta, path_to_file):
    json_meta = json.dumps(meta, indent = 4)

    with open(path_to_file, "w") as f:
        f.write(json_meta)

# From a root folder, explorer all subfolders for all metadata.json files.
def find_metafiles(root_path):
    metafiles = []
    for (root,dirs,files) in os.walk(root_path):
        if "metadata.json" in files:
            metafiles.append(root + "/metadata.json")

    return metafiles

# Not currently implemented.
# Look through a metafile for a search_key and search_value.
def search_metafiles(metafile, search_key, search_value):
    pass

# Returns an empty set of dictionaries that can be serialized to a standard-compliant metadata.json file.
def init_meta():
    metafile_init = {"dataset":{"title":"", "description":"", "keyword":[], "modified":"", "publisher":{"name":""}, "contactPoint":{"fn":""}, "identifier":"", "refPeriod":""}}

    return metafile_init
