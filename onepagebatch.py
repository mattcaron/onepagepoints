#!/usr/bin/env python

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


from onepagepoints import *
from pyexcel_ods3 import get_data, save_data

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
            if c.endswith('”'):
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

        new_weapon = Weapon(name, wprange, attacks, armorPiercing, special)
        for i in range(count):
            weapons.append(new_weapon)
    return weapons

def parse_special(special):
    special = special.lower().split(',')
    # strip all whitespace
    return [sp.strip() for sp in special]

def main():

    column_order = ['name', 'count', 'qua', 'def', 'equipment', 'special']

    data = get_data("Tao_spec.ods")

    for sheet in data:
        for row in data[sheet][1:]:
            dunit = {}
            if len(row) < len(column_order):
                continue

            for i, col in enumerate(column_order):
                dunit[col] = row[i]

            weapons = parse_equipment(dunit['equipment'])
            special = parse_special(dunit['special'])

            unit = Unit(dunit['name'], dunit['count'], dunit['qua'], dunit['def'], weapons, special)
            print(unit)

            if len(row) == 8:
                row.append(unit.cost)
            else:
                row[8] = unit.cost

    save_data("Tao_spec_new.ods", data)

if __name__ == "__main__":
    # execute only if run as a script
    main()
