print("area calculator")

print ("คำนวณพื้นที่ สี่ดหลี่ยมจตุรัส")
Width = int(input("ใส่ความยาวด้าน : "))
area = (Width*Width)
print (f"พื้นที่สี่เหลี่ยมจตุรัสนี้ คือ {area}")

print ("คำนวณพื้นที่ สี่เหลี่ยมผืนผ้า")
Width = int(input("ใส่ความกว้าง : "))
Height = int(input("ใส่ความสูง : "))
area = (Width*Height)
print (f"พื้นที่สี่เหลี่ยมผืนผ้า คือ {area}")

print ("คำนวณพื้นที่ วงกลม")
r = int(input("ใส่ความยาวรองรัศมี : "))
area = (3.14*r**2)
print (f"พื้นที่สี่เหลี่ยมผืนผ้า คือ {area}")