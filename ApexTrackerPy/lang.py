# Author: nerrog(YU-PEI)
# Copyright (c) 2021 nerrog
# License: MIT

import ApexTrackerPy
import json


IS_PRE_LOAD_LANG = False
load_lang = {}

def pre_load_lang(*lang):
    global IS_PRE_LOAD_LANG
    global load_lang
    LANG = ApexTrackerPy.LANG
    if lang:
        LANG = lang[0]

    with open(ApexTrackerPy.__path__[0]+"/lang/"+LANG+".json", 'r', encoding="utf_8") as f:
        load_lang = json.load(f)
        IS_PRE_LOAD_LANG = True


def translate(input, type):
    global load_lang
    LANG = ApexTrackerPy.LANG

    if LANG == "en-US":
        return input

    if not IS_PRE_LOAD_LANG:    
        with open(ApexTrackerPy.__path__[0]+"/lang/"+LANG+".json", 'r', encoding="utf_8") as f:
            load_lang = json.load(f)

    for key in load_lang[type].keys():
        tmp = input.replace(key, load_lang[type][key])
        if tmp != input:
            return tmp

    return input