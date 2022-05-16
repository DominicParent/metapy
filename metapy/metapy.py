import argparse
import json
import os

# Takes a path and loads metadata from json to python dictionaries.
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

# Recursive look through a metafile for a search_key and search_value.
def rec_search_metafile(metafile, search_key, search_value, result):

    for key, value in metafile.items():
        if type(value) is dict:
            result = rec_search_metafile(value, search_key, search_value, result)
        if key == search_key and value == search_value:
            result = True

    return result

# Publicly called function for rec_search_metafile.
def search_metafile(metafile, search_key, search_value):
    result = False

    return rec_search_metafile(metafile, search_key, search_value, result)


# Returns an empty set of dictionaries that can be serialized to a standard-compliant metadata.json file.
def init_meta():
    metafile_init = {"dataset":{"title":"", "description":"", "keyword":[], "modified":"", "publisher":{"name":""}, "contactPoint":{"fn":""}, "identifier":"", "refPeriod":""}}

    return metafile_init
