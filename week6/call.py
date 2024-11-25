import gun
gun1 = gun.Gun("M416",0)

while True:
    gun1.Fire()
    print(gun1.ammo)
    if gun1.ammo < 1:
        f = str(input("I need more bullet!!!! : "))
        if f == "yes":
            gun1.add_ammo(45)
        else :
            break