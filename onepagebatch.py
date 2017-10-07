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
import argparse


def getEquipment(name):
    global equipments

    if name in equipments:
        return equipments[name]

    if name.endswith('s'):
        singular = name[:-1]
        if singular in equipments:
            return equipments[singular]

    print('Error equipment {0} Not found !'.format(name))
    return None


def getEquipments(names):
    return [getEquipment(name) for name in names]


def getUnit(junit):
    global equipments

    unit_equipments = getEquipments(junit['equipment'])

    return Unit(junit['name'], junit['count'], junit['quality'], junit['defense'], unit_equipments, junit['special'])


def points(n):
    if n == 0:
        return "Free"
    if n == 1:
        return "1 pt"
    return '{} pts'.format(n)


# Calculate the cost of an upgrade on a unit
# If the upgrade is only for one model, set the unit count to 1
# remove equipment, add new equipment and calculate the new cost.
def calculate_upgrade_cost(unit, to_remove, to_add, all):
    new_unit = copy.copy(unit)
    if not all:
        new_unit.SetCount(1)

    prev_cost = new_unit.cost

    new_unit.RemoveEquipment(getEquipments(to_remove))

    costs = []
    for upgrade in to_add:
        add_unit = copy.copy(new_unit)
        add_unit.AddEquipment(getEquipments(upgrade))

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
    with open(outfile, 'w') as f:
        for junit in junits:
            unit = getUnit(junit)
            equ = "\\newline ".join([str(equ) for equ in unit.equipments])
            sp = ", ".join(unit.specialRules)
            up = ", ".join(junit['upgrades'])
            line = '{0};{1};{2};{3};{4};{5};{6};{7}\n'.format(unit.name, unit.count, unit.quality, unit.basedefense, equ, sp, up, points(unit.cost))
            f.write(line)


# an upgrade group cost is calculated for all units who have access to this
# upgrade group, so calculate the mean
# will transform [[11, 13], [7, 10]] in [9, 12]
def calculate_mean_upgrade_cost(costs):
    count = len(costs)
    ret = [0] * len(costs[0])
    for cu in costs:
        for i, c in enumerate(cu):
            ret[i] += c / count

    ret = [int(round(c)) for c in ret]
    return ret


def write_upgrade_csv(jupgrades, upgradeFile):
    with open(upgradeFile, 'w') as f:
        for group, upgrades in jupgrades.items():
            f.write(group + ' | ')
            for up in upgrades:
                f.write(up['text'] + ';;' + group + '\n')
                cost = calculate_mean_upgrade_cost(up['cost'])
                for i, addEqu in enumerate(up['add']):
                    prettyEqu = [str(getEquipment(equ)) for equ in addEqu]
                    f.write('{0};{1};{2}\n'.format('\\newline '.join(prettyEqu), points(cost[i]), group))


def generateFaction():
    global equipments
    with open("equipments.json", "r") as f:
        jequipments = json.loads(f.read())

    weaponList = [Weapon(name, w['range'], w['attacks'], w['ap'], w['special']) for name, w in jequipments['weapons'].items()]
    weaponList += [Weapon('Linked ' + name, w['range'], w['attacks'], w['ap'], ['Linked'] + w['special']) for name, w in jequipments['weapons'].items() if 'Linked' not in w['special'] and w['range'] > 0]
    equipments = {equ.name: equ for equ in weaponList}

    warGearList = [WarGear(name, wargear['special'], getEquipments(wargear['weapons'])) for name, wargear in jequipments['wargear'].items()]
    equipments = {equ.name: equ for equ in warGearList + weaponList}

    allFiles = os.listdir(".")
    for i in range(1, 10):
        unitFile = 'units' + str(i) + '.json'
        upgradeFile = 'upgrades' + str(i) + '.json'
        if unitFile in allFiles and upgradeFile in allFiles:
            print('page {}'.format(i))
            with open(unitFile, "r") as f:
                junits = json.loads(f.read())
            with open(upgradeFile, "r") as f:
                jupgrades = json.loads(f.read())

            for junit in junits:
                calculate_unit_cost(junit, jupgrades)

            write_unit_csv(junits, unitFile[:-4] + 'csv')
            write_upgrade_csv(jupgrades, upgradeFile[:-4] + 'csv')


def main():
    parser = argparse.ArgumentParser(description='This script will compute the Unit costs and upgrade costs for a faction, and write the .csv files for LaTeX')
    parser.add_argument('path', metavar='path', type=str, nargs='+',
                        help='path to the faction (should contain at list equipments.json, units1.json, upgrades1.json)')

    args = parser.parse_args()

    current_dir = os.getcwd()
    for faction in args.path:
        print("Building faction {}".format(faction))
        os.chdir(faction)
        generateFaction()
        os.chdir(current_dir)


if __name__ == "__main__":
    # execute only if run as a script
    main()
