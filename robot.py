from weapon import Weapon
class Robot: 
    def __init__(self,name,health, weapon):
        self.name = name
        self.health = health
        self.weapon = weapon
    
    def attack_dino(self,target):
        damage = self.weapon.attack_power
        target.health -= damage

