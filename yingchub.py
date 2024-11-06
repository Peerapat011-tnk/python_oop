import random
winrate = int(0)
looserate = int(0)
dranwrate = int(0)
while True:
    a = random.choice(["ค้อน","กระดาษ","กรรไกร"])
    print("-------------------------")
    print("โปรแกรมเป่ายิ้งฉุบ\n")
    print("เลือก ค้อน กระดาษ กรรไกร ออกเกม\n")
    print(a)
    Aws = str(input("คุณเลือก : "))
    print("-------------------------")
    if Aws == a :
        dranwrate += 1
        print("เสมอ")
    elif Aws == "ค้อน" and a == "กระดาษ" :
        looserate += 1
        print("แพ้")
    elif Aws == "กระดาษ" and a == "กรรไกร" :
        looserate += 1
        print("แพ้")
    elif Aws == "กรรไกร" and a == "ค้อน" :
        looserate += 1
        print("แพ้")
    elif Aws == "ออกเกม":
        break
    else :
        winrate += 1
        print("ชนะ")
    print("*-----------------------*")
print(f"จำนวนชนะ : {winrate}")
print(f"จำนวนแพ้ : {looserate}")
print(f"จำนวนเสมอ : {dranwrate}")
print(f"จำนวนที่เล่นทั้งหมด : {dranwrate+winrate+dranwrate}")