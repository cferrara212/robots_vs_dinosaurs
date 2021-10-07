from robot import Robot
from dinosaur import Dinosaur
from weapon import Weapon
from fleet import Fleet
from herd import Herd


energy_sword = Weapon('sword',2)
blaster = Weapon('blaster', 10)
katar = Weapon('katar', 6)

robot_one = Robot('rowdy',180,energy_sword)
robot_two = Robot('dino smasher',75, blaster)
robot_three = Robot('ninja',95, katar)


dino_one = Dinosaur('rex',2,180)
dino_two = Dinosaur('raptor',10,75)
dino_three= Dinosaur('steg',6,95)


fleet_one = Fleet()

heard_one = Herd()

fleet_one.add_robot('rowdy')
fleet_one.add_robot('dino smasher')
fleet_one.add_robot('ninja')

heard_one.add_dinosaur('rex')
heard_one.add_dinosaur('raptor')
heard_one.add_dinosaur('steg')


robot_one.attack_dino(dino_one)
dino_one.attack_robot(robot_one)
print(dino_one.health)
