from json import dump, load
import os
from flask import jsonify


def read_json(filepath):
    try:
        with open(filepath, "r") as file_json:
            data = load(file_json)
            return data
    except:
        return []

def write_json(filepath, payload):
    list_json = read_json(filepath)
    list_json.append(payload)
    with open(filepath,'w') as file_json:
        dump(list_json, file_json, indent=4)
    
    return payload