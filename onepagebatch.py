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


from onepagepoints import *
import json
import os
import copy


def getEquipment(name):
    global equipments
    for equ in equipments:
        if equ.name == name:
            return equ
    print('Error equipment {0} Not found !'.format(name))
    return None


def getUnit(junit):
    global equipments

    unit_equipments = [getEquipment(equ) for equ in junit['equipment']]

    return Unit(junit['name'], junit['count'], junit['quality'], junit['defense'], unit_equipments, junit['special'])


# Calculate the cost of an upgrade on a unit
# If the upgrade is only for one model, set the unit count to 1
# remove equipment, add new equipment and calculate the new cost.
def calculate_upgrade_cost(unit, to_remove, to_add, all):
    new_unit = copy.copy(unit)
    if not all:
        new_unit.SetCount(1)

    prev_cost = new_unit.cost

    new_unit.RemoveEquipment([getEquipment(w) for w in to_remove])

    costs = []
    for upgrade in to_add:
        add_unit = copy.copy(new_unit)
        add_unit.AddEquipment([getEquipment(w) for w in upgrade])

        up_cost = add_unit.cost - prev_cost
        costs.append(up_cost)
    return costs


def calculate_upgrade_group_cost(unit, upgrade_group):
    for upgrade_batch in upgrade_group:
        all = upgrade_batch.get('all', False)
        to_remove = upgrade_batch.get('remove', {})
        to_add = upgrade_batch['add']
        costs = calculate_upgrade_cost(unit, to_remove, to_add, all)
        if 'cost' in upgrade_batch:
            upgrade_batch['cost'].append(costs)
        else:
            upgrade_batch['cost'] = [costs]


def calculate_unit_cost(junit, jupgrades):

    unit = getUnit(junit)

    up = junit['upgrades']
    for upgrade_group in junit['upgrades']:
        if upgrade_group in jupgrades:
            calculate_upgrade_group_cost(unit, jupgrades[upgrade_group])
        else:
            print("Missing upgrade_group {0} in upgrades.json".format(upgrade_group))


def write_unit_csv(junits, outfile):

    units = [getUnit(junit) for junit in junits]

    with open(outfile, 'w') as f:
        for junit in junits:
            unit = getUnit(junit)
            equ = "\\newline ".join([str(equ) for equ in unit.equipments])
            sp = ", ".join(unit.specialRules)
            up = ", ".join(junit['upgrades'])
            line = '{0};{1};{2};{3};{4};{5};{6};{7}\n'.format(unit.name, unit.count, unit.quality, unit.basedefense, equ, sp, up, unit.cost)
            f.write(line)


def main():
    global equipments

    faction = "Tao"

    with open(os.path.join(faction, "equipments.json"), "r") as f:
        jequipments = json.loads(f.read())

    equipments = [Weapon(name, w['range'], w['attacks'], w['ap'], w['special']) for name, w in jequipments['weapons'].items()]
    equipments += [WarGear(name, rules) for name, rules in jequipments['wargear'].items()]

    with open(os.path.join(faction, "units1.json"), "r") as f:
        junits = json.loads(f.read())

    with open(os.path.join(faction, "upgrades1.json"), "r") as f:
        jupgrades = json.loads(f.read())

    for junit in junits:
        calculate_unit_cost(junit, jupgrades)

    write_unit_csv(junits, 'units.csv')

    print(jupgrades)


if __name__ == "__main__":
    # execute only if run as a script
    main()
