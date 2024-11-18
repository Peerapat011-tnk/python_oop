import random
def PRS(Ans):
    while True:
        a = random.choice(["ค้อน","กระดาษ","กรรไกร"])
        print("โปรแกรมเป่ายิ้งฉุบ\n")
        print("ระบบออก : ",a)
        
        if Ans == "exit":
            break
        elif Ans == "กรรไกร" and a == "กระดาษ" :
            print("คุณชนะ")
        elif Ans == "ค้อน" and a == "กรรไกร" :
            print("คุณชนะ")
        elif Ans == "กระดาษ" and a == "ค้อน" :
            print("คุณชนะ")
        else :
            print("คุณแพ้")
    
Ans = input("คุณเลือกออก : ")
PRS(Ans)

