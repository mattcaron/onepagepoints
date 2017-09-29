# onepagepoints
small python 3.7 script to calculate units points for onepagerule Grimdark Future

It needs some tweaks. compared to onepagerule points, this algorithm lower the weapon cost, and increase the cost of high defense, high toughness units.

# Install

Tested only with python 3.7 on Archlinux. It should work everywhere you can run python.
You need to install pyexcel_ods3 to run onepagebatch.py, and parse the libreoffice ods files.

# Files details

 * onepagepoints.py : library to calculate individual cost of weapons/units, also a main() to do unit tests
 * onepagebatch.py : script which read libreoffice calc sheets (created from the onepagerule's pdf), and add the point cost
 * tao_spec.ods : example ods file with the Tao Coalition

# Example of output for Tao coalition :
Battlesuit Captain [1] 85 pts
 * 20 pts Suit Fists (A4, AP(1))
 * ambush, flying, hero, tough(3)
 * defense 57 pts, attack 20 pts, other 8 pts

Grunt Captain [1] 70 pts
 * 7 pts Pulse Rifle (30", A1, AP(1))
 * 8 pts Ritual Dagger (A3, AP(0))
 * hero, tough(3), volley fire
 * defense 25 pts, attack 15 pts, other 30 pts

Sage [1] 50 pts
 * 8 pts Sacred Spear (A3, AP(0))
 * hero, inspiring, tough(3)
 * defense 12 pts, attack 8 pts, other 30 pts

Grunt Squad [5] 75 pts
 * 8 pts Pulse Shotguns (12", A2, AP(1))
 * good shot
 * defense 7 pts, attack 8 pts, other 0 pts

Spotter Squad [5] 85 pts
 * 10 pts Pulse Carbines (18", A2, AP(1))
 * good shot, scout
 * defense 5 pts, attack 10 pts, other 2 pts

Stealth Suits [3] 135 pts
 * 21 pts Gatling Carbines (18", A4, AP(1))
 * ambush, good shot, scout, stealth
 * defense 12 pts, attack 21 pts, other 12 pts

Battle Suits [3] 195 pts
 * 8 pts Suit Fists (A2, AP(1))
 * ambush, flying, tough(3)
 * defense 51 pts, attack 8 pts, other 6 pts

Sniper Drones [3] 42 pts
 * 7 pts Pulse Rifles (30", A1, AP(1))
 * ambush, flying, good shot
 * defense 6 pts, attack 7 pts, other 1 pts

Gun Drones [5] 115 pts
 * 15 pts Linked Pulse Carbines (18", A2, AP(1), linked)
 * ambush, flying, good shot
 * defense 6 pts, attack 15 pts, other 2 pts

Jackals [5] 45 pts
 * 4 pts Assault Rifles (24", A1, AP(0))
 * scout, strider
 * defense 4 pts, attack 4 pts, other 1 pts

Jackal Hounds [5] 70 pts
 * 8 pts Claws (A3, AP(0))
 * fast, scout, strider
 * defense 4 pts, attack 8 pts, other 2 pts

Jackal Beast Riders [3] 144 pts
 * 19 pts Autocannons (48", A2, AP(3))
 * scout, strider, tough(3)
 * defense 23 pts, attack 19 pts, other 6 pts

Locusts [5] 60 pts
 * 5 pts Neutron Carbines (18", A1, AP(1))
 * ambush, flying
 * defense 6 pts, attack 5 pts, other 1 pts

Hover Transport [1] 148 pts
 * 24 pts Gatling Carbine (18", A4, AP(1))
 * 16 pts Linked Pulse Carbines (18", A2, AP(1), linked)
 * 16 pts Linked Pulse Carbines (18", A2, AP(1), linked)
 * 12 pts Monster Stomp (A0, AP(0), impact(3))
 * fast, strider, tough(3), transport(11), vehicle, fear
 * defense 75 pts, attack 68 pts, other 5 pts

Hover Tank [1] 302 pts
 * 63 pts Railgun (48", A1, AP(6), deadly)
 * 16 pts Linked Pulse Carbines (18", A2, AP(1), linked)
 * 16 pts Linked Pulse Carbines (18", A2, AP(1), linked)
 * 12 pts Monster Stomp (A0, AP(0), impact(3))
 * fast, strider, tough(6), vehicle, fear
 * defense 190 pts, attack 107 pts, other 5 pts

Hover Attack Bike [1] 131 pts
 * 24 pts Gatling Carbine (18", A4, AP(1))
 * 16 pts Linked Pulse Carbines (18", A2, AP(1), linked)
 * 16 pts Linked Pulse Carbines (18", A2, AP(1), linked)
 * 12 pts Monster Stomp (A0, AP(0), impact(3))
 * fast, strider, tough(3), vehicle, fear
 * defense 58 pts, attack 68 pts, other 5 pts

Heavy Stealth Suit [1] 172 pts
 * 14 pts Heavy Suit Fists (A3, AP(2))
 * 30 pts Linked Flamethrower (12", A6, AP(0), linked)
 * 24 pts Ion Carbine (18", A1, AP(3), blast(3))
 * 9 pts Monster Stomp (A0, AP(0), impact(3))
 * ambush, flying, tough(3), stealth, vehicle, fear
 * defense 74 pts, attack 77 pts, other 21 pts

Heavy Battle Suit [1] 146 pts
 * 6 pts Suit Fists (A2, AP(1))
 * 12 pts Linked Plasma Rifle (24", A1, AP(3), linked)
 * 55 pts Linked Heavy Rail Rifle (48", A1, AP(4), deadly, linked)
 * 8 pts Monster Stomp (A0, AP(0), impact(3))
 * tough(3), vehicle, fear
 * defense 60 pts, attack 81 pts, other 5 pts

Razor Fighter [1] 141 pts
 * 21 pts Gatling Carbine (18", A4, AP(1))
 * 61 pts Ion Tailgun (30", A1, AP(3), blast(6))
 * 8 pts Monster Stomp (A0, AP(0), impact(3))
 * flyer, tough(3), vehicle, fear
 * defense 46 pts, attack 90 pts, other 5 pts

Sun Bomber [1] 183 pts
 * 23 pts Missile Pod (36", A2, AP(3))
 * 19 pts Pulse Bombs (6", A1, AP(1), blast(6))
 * 41 pts Linked Ion Rifle (30", A1, AP(3), blast(3), linked)
 * 41 pts Linked Ion Rifle (30", A1, AP(3), blast(3), linked)
 * 8 pts Monster Stomp (A0, AP(0), impact(3))
 * flyer, tough(3), vehicle, fear
 * defense 46 pts, attack 132 pts, other 5 pts

Tide Titan [1] 341 pts
 * 11 pts Titan Stomp (A3, AP(2))
 * 12 pts Linked Plasma Rifle (24", A1, AP(3), linked)
 * 76 pts Heavy Gatling Carbine (36", A8, AP(2))
 * 8 pts Monster Stomp (A0, AP(0), impact(3))
 * 45 pts Titan Stomp (A6, AP(2), autohit)
 * titan, tough(6), vehicle, fear
 * defense 184 pts, attack 152 pts, other 5 pts

Surge Titan [1] 670 pts
 * 11 pts Titan Stomp (A3, AP(2))
 * 28 pts Linked Flamethrower (12", A6, AP(0), linked)
 * 134 pts Cluster Rockets (48", A14, AP(1))
 * 92 pts Pulse Cannon (24", A2, AP(6), blast(3))
 * 38 pts Linked Smart Missiles (30", A4, AP(1), indirect, linked)
 * 21 pts Destroyer Missiles (48", A1, AP(4), deadly, limited)
 * 21 pts Destroyer Missiles (48", A1, AP(4), deadly, limited)
 * 21 pts Destroyer Missiles (48", A1, AP(4), deadly, limited)
 * 21 pts Destroyer Missiles (48", A1, AP(4), deadly, limited)
 * 8 pts Monster Stomp (A0, AP(0), impact(3))
 * 45 pts Titan Stomp (A6, AP(2), autohit)
 * titan, tough(9), vehicle, fear
 * defense 225 pts, attack 440 pts, other 5 pts
