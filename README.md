# onepagepoints
small python 3.7 script to calculate units points for onepagerule Grimdark Future

It needs some tweaks. compared to onepagerule points, this algorithm lower the weapon cost, and increase the cost of High defense, high toughness units.

tested only with python 3.7 on Archlinux. should work everywhere you can run python.
you need to install pyexcel_ods3 to run onepagebatch.py, and parse the libreoffice ods files.

onepagepoints.py : library to calculate individual cost of weapons/units
onepagebatch.py : script which read libreoffice calc sheets (created from the onepagerule's pdf), and add the point cost

tao_spec.ods : example ods file with the Tao Coalition



example of output for Tao coalition :

Battlesuit Captain [1] 79 pts
	20 pts Suit Fists (A4, AP(1))
	ambush, flying, hero, tough(3)
	defense 52 pts, attack 20 pts, other 7 pts

Grunt Captain [1] 65 pts
	7 pts Pulse Rifle (30", A1, AP(1))
	7 pts Ritual Dagger (A3, AP(0))
	hero, tough(3), volley fire
	defense 21 pts, attack 14 pts, other 30 pts

Sage [1] 44 pts
	7 pts Sacred Spear (A3, AP(0))
	hero, inspiring, tough(3)
	defense 7 pts, attack 7 pts, other 30 pts

Grunt Squad [5] 70 pts
	8 pts Pulse Shotguns (12", A2, AP(1))
	good shot
	defense 6 pts, attack 8 pts, other 0 pts

Spotter Squad [5] 70 pts
	10 pts Pulse Carbines (18", A2, AP(1))
	good shot, scout
	defense 3 pts, attack 10 pts, other 1 pts

Stealth Suits [3] 120 pts
	20 pts Gatling Carbines (18", A4, AP(1))
	ambush, good shot, scout, stealth
	defense 10 pts, attack 20 pts, other 10 pts

Battle Suits [3] 174 pts
	7 pts Suit Fists (A2, AP(1))
	ambush, flying, tough(3)
	defense 46 pts, attack 7 pts, other 5 pts

Sniper Drones [3] 36 pts
	7 pts Pulse Rifles (30", A1, AP(1))
	ambush, flying, good shot
	defense 4 pts, attack 7 pts, other 1 pts

Gun Drones [5] 95 pts
	14 pts Linked Pulse Carbines (18", A2, AP(1), linked)
	ambush, flying, good shot
	defense 4 pts, attack 14 pts, other 1 pts

Jackals [5] 25 pts
	3 pts Assault Rifles (24", A1, AP(0))
	scout, strider
	defense 2 pts, attack 3 pts, other 0 pts

Jackal Hounds [5] 55 pts
	8 pts Claws (A3, AP(0))
	fast, scout, strider
	defense 2 pts, attack 8 pts, other 1 pts

Jackal Beast Riders [3] 126 pts
	18 pts Autocannons (48", A2, AP(3))
	scout, strider, tough(3)
	defense 19 pts, attack 18 pts, other 5 pts

Locusts [5] 45 pts
	5 pts Neutron Carbines (18", A1, AP(1))
	ambush, flying
	defense 4 pts, attack 5 pts, other 0 pts

Hover Transport [1] 140 pts
	23 pts Gatling Carbine (18", A4, AP(1))
	15 pts Linked Pulse Carbines (18", A2, AP(1), linked)
	15 pts Linked Pulse Carbines (18", A2, AP(1), linked)
	12 pts Monster Stomp (A0, AP(0), impact(3))
	fast, strider, tough(3), transport(11), vehicle, fear
	defense 70 pts, attack 65 pts, other 5 pts

Hover Tank [1] 289 pts
	63 pts Railgun (48", A1, AP(6), deadly)
	15 pts Linked Pulse Carbines (18", A2, AP(1), linked)
	15 pts Linked Pulse Carbines (18", A2, AP(1), linked)
	12 pts Monster Stomp (A0, AP(0), impact(3))
	fast, strider, tough(6), vehicle, fear
	defense 179 pts, attack 105 pts, other 5 pts

Hover Attack Bike [1] 123 pts
	23 pts Gatling Carbine (18", A4, AP(1))
	15 pts Linked Pulse Carbines (18", A2, AP(1), linked)
	15 pts Linked Pulse Carbines (18", A2, AP(1), linked)
	12 pts Monster Stomp (A0, AP(0), impact(3))
	fast, strider, tough(3), vehicle, fear
	defense 53 pts, attack 65 pts, other 5 pts

Heavy Stealth Suit [1] 163 pts
	13 pts Heavy Suit Fists (A3, AP(2))
	30 pts Linked Flamethrower (12", A6, AP(0), linked)
	23 pts Ion Carbine (18", A1, AP(3), blast(3))
	9 pts Monster Stomp (A0, AP(0), impact(3))
	ambush, flying, tough(3), stealth, vehicle, fear
	defense 69 pts, attack 75 pts, other 19 pts

Heavy Battle Suit [1] 139 pts
	6 pts Suit Fists (A2, AP(1))
	11 pts Linked Plasma Rifle (24", A1, AP(3), linked)
	55 pts Linked Heavy Rail Rifle (48", A1, AP(4), deadly, linked)
	7 pts Monster Stomp (A0, AP(0), impact(3))
	tough(3), vehicle, fear
	defense 55 pts, attack 79 pts, other 5 pts

Razor Fighter [1] 134 pts
	20 pts Gatling Carbine (18", A4, AP(1))
	60 pts Ion Tailgun (30", A1, AP(3), blast(6))
	7 pts Monster Stomp (A0, AP(0), impact(3))
	flyer, tough(3), vehicle, fear
	defense 42 pts, attack 87 pts, other 5 pts

Sun Bomber [1] 174 pts
	22 pts Missile Pod (36", A2, AP(3))
	18 pts Pulse Bombs (6", A1, AP(1), blast(6))
	40 pts Linked Ion Rifle (30", A1, AP(3), blast(3), linked)
	40 pts Linked Ion Rifle (30", A1, AP(3), blast(3), linked)
	7 pts Monster Stomp (A0, AP(0), impact(3))
	flyer, tough(3), vehicle, fear
	defense 42 pts, attack 127 pts, other 5 pts

Tide Titan [1] 330 pts
	11 pts Titan Stomp (A3, AP(2))
	11 pts Linked Plasma Rifle (24", A1, AP(3), linked)
	76 pts Heavy Gatling Carbine (36", A8, AP(2))
	7 pts Monster Stomp (A0, AP(0), impact(3))
	44 pts Titan Stomp (A6, AP(2), autohit)
	titan, tough(6), vehicle, fear
	defense 176 pts, attack 149 pts, other 5 pts

Surge Titan [1] 648 pts
	11 pts Titan Stomp (A3, AP(2))
	27 pts Linked Flamethrower (12", A6, AP(0), linked)
	133 pts Cluster Rockets (48", A14, AP(1))
	91 pts Pulse Cannon (24", A2, AP(6), blast(3))
	37 pts Linked Smart Missiles (30", A4, AP(1), indirect, linked)
	20 pts Destroyer Missiles (48", A1, AP(4), deadly, limited)
	20 pts Destroyer Missiles (48", A1, AP(4), deadly, limited)
	20 pts Destroyer Missiles (48", A1, AP(4), deadly, limited)
	20 pts Destroyer Missiles (48", A1, AP(4), deadly, limited)
	7 pts Monster Stomp (A0, AP(0), impact(3))
	44 pts Titan Stomp (A6, AP(2), autohit)
	titan, tough(9), vehicle, fear
	defense 213 pts, attack 430 pts, other 5 pts
