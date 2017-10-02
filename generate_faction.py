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

from pyexcel_ods3 import get_data, save_data
import json
from collections import OrderedDict

# Parse the equipment list to find characteristics of individual weapons
def parse_equipment(equipment):
    nested = 0
    weapons_raw = []
    weapons = []
    namestart = 0
    for index, char in enumerate(equipment):
        if char == '(':
            if nested == 0:
                start = index
            nested += 1
        elif char == ')':
            nested -= 1
            if nested == 0:
                weapons_raw.append((equipment[namestart:start].strip(' ,'),equipment[start + 1:index]))
                namestart = index + 1

    for w in weapons_raw:
        name = w[0]
        wprange = 0
        armorPiercing= 0
        attacks = 0
        special = []
        count = 1

        for c in w[1].split(','):
            c = c.strip()
            if c.endswith('"'):
                wprange = int(c[:-1])
            elif c.startswith('AP'):
                armorPiercing = int(c[3:-1])
            elif c.startswith('A') and c[1:].isdigit():
                attacks = int(c[1:])
            else:
                special.append(c.lower().strip())

        if 'linked' in name.lower().split():
            if not 'linked' in special:
                special.append('linked')

        # check for 2x or Nx if the same wepon is preset twice or more
        firstword = name.lower().split()[0]
        if firstword.endswith('x'):
            if firstword[:-1].isdigit():
                count = int(firstword[:-1])
                # remove 2x from the name
                name = name[len(firstword) + 1:]

        new_weapon = [name, wprange, attacks, armorPiercing, special]
        for i in range(count):
            weapons.append(new_weapon)
    return weapons

def parse_upgrades(upgrades):
    return [up.strip() for up in upgrades.split(',')]

def parse_special(special):
    special = special.lower().split(',')
    # strip all whitespace
    return [sp.strip() for sp in special]

def main():

    column_order = ['name', 'count', 'qua', 'def', 'equipment', 'special', 'upgrades']

    data = get_data("Tao_spec.ods")

    alljweapons = {}
    unitpage = 1

    for sheet in data:
        alljunits = []
        for row in data[sheet][1:]:
            dunit = {}
            if len(row) < len(column_order):
                continue

            for i, col in enumerate(column_order):
                if col in ['name', 'equipment', 'special']:
                    dunit[col] = row[i]
                else:
                    dunit[col] = row[i]

            equipment = parse_equipment(dunit['equipment'])

            for e in equipment:
                key = '"' + e[0] + '"'
                if not key in alljweapons:
                    alljweapons[key] = OrderedDict([('range', e[1]),('attacks', e[2]),('ap', e[3]),('special', e[4])])

            equipment_name = [e[0] for e in equipment]
            ju = OrderedDict([('name', dunit['name']), ('count', dunit['count']), ('quality', dunit['qua']), ('defense', dunit['def']), ('equipment', equipment_name), ('special', parse_special(dunit['special'])), ('upgrades', parse_upgrades(dunit['upgrades']))])
            alljunits.append(ju)

        with open('units' + str(unitpage) + '.json', 'w') as f:
            f.write(json.dumps(alljunits, indent=2))

        alljunits = []
        unitpage += 1

    with open('weapons.json', 'w') as f:
        f.write('{\n')
        f.write(",\n".join(['{:<30} : '.format(k) + json.dumps(alljweapons[k]) for k in alljweapons]))
        f.write("\n}\n")

if __name__ == "__main__":
    # execute only if run as a script
    main()
