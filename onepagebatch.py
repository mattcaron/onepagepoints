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

# Calculate the cost of an upgrade on a unit
# If the upgrade is only for one model, set the unit count to 1
# remove equipment, add new equipment and calculate the new cost.
def calculate_upgrade_cost(unit, to_remove, to_add, all):
    print('to_remove {0}'.format(to_remove))
    print('to_add {0}'.format(to_add))

    new_unit = copy.copy(unit)
    if not all:
        new_unit.SetCount(1)

    prev_cost = new_unit.cost

    new_unit.RemoveWeapon([getWeapon(w) for w in to_remove.get('weapons', [])])
    new_unit.RemoveSpecial(to_remove.get('special', []))

    for upgrade in to_add:
        add_unit = copy.copy(new_unit)
        add_unit.AddWeapon([getWeapon(w) for w in upgrade.get('weapons', [])])
        add_unit.AddSpecial(upgrade.get('special', []))
        up_cost = add_unit.cost - prev_cost
        if 'cost' in upgrade:
            upgrade['cost'].append(up_cost)
        else:
            upgrade['cost'] = [up_cost]

def calculate_upgrade_group_cost(unit, upgrade_group):
    for upgrade_batch in upgrade_group:
        all = upgrade_batch.get('all', False)
        to_remove = upgrade_batch.get('remove', {})
        to_add = upgrade_batch['add']
        calculate_upgrade_cost(unit, to_remove, to_add, all)

def getWeapon(name):
    global weapons
    for w in weapons:
        if w.name == name:
            return w
    print('Error weapon {0} Not found !'.format(name))
    return None

def calculate_unit_cost(junit, jupgrades):
    global weapons

    unit_weapon = [getWeapon(w) for w in junit['equipment']]

    unit = Unit(junit['name'], junit['count'], junit['quality'], junit['defense'], unit_weapon, junit['special'])

    up = junit['upgrades']
    for upgrade_group in junit['upgrades']:
        if upgrade_group in jupgrades:
            calculate_upgrade_group_cost(unit, jupgrades[upgrade_group])
        else:
            print("Missing upgrade_group {0} in upgrades.json".format(upgrade_group))


def main():
    global weapons

    faction = "Tao"

    with open(os.path.join(faction, "weapons.json"), "r") as f:
        jweapons = json.loads(f.read())

    weapons = [Weapon(w, jweapons[w]['range'], jweapons[w]['attacks'], jweapons[w]['ap'], jweapons[w]['special']) for w in jweapons]

    with open(os.path.join(faction, "units1.json"), "r") as f:
        junits = json.loads(f.read())

    with open(os.path.join(faction, "upgrades1.json"), "r") as f:
        jupgrades = json.loads(f.read())

    for junit in junits:
        calculate_unit_cost(junit, jupgrades)

    print(jupgrades)


if __name__ == "__main__":
    # execute only if run as a script
    main()
