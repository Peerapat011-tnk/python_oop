import random
def PRS():
    while True:
        a = random.choice(["ค้อน","กระดาษ","กรรไกร"])
        print("โปรแกรมเป่ายิ้งฉุบ\n")
        print("ระบบออก : ",a)
        Ans = input("คุณเลือกออก : ")
        if Ans == "exit":
            break
        elif Ans == "กรรไกร" and a == "กระดาษ" :
            print("คุณชนะ")
        elif Ans == "ค้อน" and a == "กรรไกร" :
            print("คุณชนะ")
        elif Ans == "กระดาษ" and a == "ค้อน" :
            print("คุณชนะ")
        elif Ans == a :
            print("เสมอ")
        else :
            print("คุณแพ้")
    

PRS()

