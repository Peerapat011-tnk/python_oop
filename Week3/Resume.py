year = int(input("โปรดกรอกชั้นปี\n"))
name = str(input("โปรดกรอกชื่อเล่น \n"))
h = float(input("โปรดกรอกส่วนสูง\n"))
w = float(input("โปรดกรอกน้ำหนัก\n"))
fname = str(input("โปรดกรอกชื่อจริง"))
age = int(input("โปรดกรอกอายุ"))
code = int(input("โปรดกรอกรหัสนักศึกษา"))



print ("ชื่อ : "+fname+" อายุ: "+str(age)+" ปี")
print ("รหัสประจำตัวนักเรียน: "+str(code)+"ระดับชั้น: "+str(year))
print ("ชื่อเล่น "+name)
print ("ส่วนสูง: "+str(h)+" เซนติเมตร "+"น้ำหนัก: "+str(w)+" กิโลกรัม\n")
print ("ส่วนสูง + น้ำหนัก = ",h+w)



