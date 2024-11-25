class Gun:
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

gun1 = Gun("M416",0)

while True:
    gun1.Fire()
    print(gun1.ammo)
    if gun1.ammo < 1:
        f = str(input("I need more bullet!!!! : "))
        if f == "yes":
            gun1.add_ammo(45)
        else :
            break

