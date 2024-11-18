resume = {}
r = int(input("จำวนวนคน :"))
for i in range (1,r+1):
    print(f"กรุณากรอกชื่อคนที่ {i} :")
    resume["nickname"] = input("กรอกชื่อเล่น : ")
    resume["No"] = input("กรอกเลขที่ : ")
    resume["Hobby"] = input("กรอกงานอดิเรก : ")
    resume["Color"] = input("กรอกสีที่ชอบ : ")
    print(resume)