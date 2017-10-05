#!/usr/bin/env python3

"""
Copyright 2017 Jocelyn Falempe kdj0c@djinvi.net

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

"""
This scripts helps to generate the json files for a faction.
It takes a libreoffice calc ".ods" file, and generate the list
of weapons, and units.
The libreoffice calc file can be done with just copy/paste from the original pdf,
and a few "manual" operation
"""

import os
import json

def format_weapon(w):
    s = '{{ "range" : {:<2}, "attacks" : {:<2}, "ap" : {:<2}, "special" : {}}}'.format(w['range'], w['attacks'], w['ap'], json.dumps(w['special']))
    return s

def main():
    jsonFile = "Tao/equipments.json"

    with open(jsonFile, "r") as f:
        data = json.loads(f.read())

    os.rename(jsonFile,jsonFile + "~")

    weapons = data['weapons']
    wargear = data['wargear']

    with open(jsonFile, "w") as f:
        f.write('{"weapons" : {\n')
        f.write(",\n".join(['{:<30} : '.format('"' + w + '"') + format_weapon(weapons[w]) for w in sorted(weapons)]))
        f.write('\n}, "wargear" : {\n')
        f.write(",\n".join(['{:<30} : '.format('"' + w + '"') + json.dumps(wargear[w]) for w in sorted(wargear)]))
        f.write('\n}}\n')


if __name__ == "__main__":
    # execute only if run as a script
    main()
