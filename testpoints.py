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

from onepagepoints import Weapon, WarGear, Unit

# due to rounding error, check if a == b (+-1)
def equalround(a, b):
    if a - b < 2 and b - a < 2:
        return True
    return False


# N attacks should cost N times the cost of the single attack weapon
def test_Weapon_attacks():
    knife = Weapon('Dummy', 12, 1, 0)
    knife.Cost(12, 4)
    dknife = Weapon('Dknife', 12, 2, 0)
    assert (equalround(knife.Cost(12, 4) * 2, dknife.Cost(12, 4)))

# check that 5+ quality weapon is twice the cost of 6+
def test_Weapon_quality():
    knife = Weapon('Dummy', 12, 12, 8)
    assert (equalround(knife.Cost(12, 6) * 2, knife.Cost(12, 5)))


# Rending is like AP(8) if quality is 6+
def test_Weapon_rending():
    knife = Weapon('Dummy', 12, 12, 8)
    rknife = Weapon('Dummy', 12, 12, 0, ['Rending'])
    assert (equalround(knife.Cost(12, 6), rknife.Cost(12, 6)))

# Cost of linked weapon is like having +1 in quality
def test_Weapon_linked():
    knife = Weapon('Dummy', 12, 12, 8)
    rknife = Weapon('Dummy', 12, 12, 8, ['Linked'])
    assert (equalround(knife.Cost(12, 4), rknife.Cost(12, 5)))


def test_Unit_count():
    unit = Unit()
    unit2 = Unit(count=2)
    assert(unit.cost * 2 == unit2.cost)
