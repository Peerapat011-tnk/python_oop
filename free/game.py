import random
Hitrate = random.randint(1,100)
Damage = int()

class Player:
    def __init__(self,pname,php,pdamage):
        self.pname = pname
        self.php = php
        self.pdamage = pdamage
        

class Sword:
    def __init__(self,name,ammo):
        self.name = name
        self.ammo = ammo
    def add_ammo(self,ammo):
        self.ammo += ammo
    def Fire(self):
        if self.ammo > 0:
            self.ammo -= 1
        else :
            print("กระสุนหมด")
