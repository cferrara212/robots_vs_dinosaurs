
class Dinosaur:
    def __init__(self,name,attack_power,health):
        self.name = name
        self.attack_power = attack_power
        self.health = health

    def attack_robot(self,target):
        damage = self.attack_power
        target.health -= damage

