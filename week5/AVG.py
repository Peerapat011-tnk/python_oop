Stop = int(input("ป้อนกี่ตัว : "))
AllNum = []
for i in range (1,Stop):
    num = int(input(f"ป้อนตัวที่ {i} : "))
    AllNum.append(num)
print(f"ค่าเฉลี่ยของ {AllNum} คือ : {sum(AllNum)/len(AllNum)}")