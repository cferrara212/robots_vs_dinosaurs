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

