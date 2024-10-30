print ("เกรด")
score = int(input("ใส่คะแนน :"))

if score < 0 or score > 100 :
    print ("กรอกคะแนนที่ถูกต้อง")

elif score < 50  :
    print ("สอบตก")
    ans = str(input("คุณอยากแก้หรือไม่ ถ้าใช้ กด Y ไม่ กด N :"))
    if ans == "Y":
        
        print (f"คะแนนของคุณที่ขาดคือ {50 - score} คะแนน")
    else :
        print ("ขอให้โชคดี")

elif score < 60 :
    print ("เกรด 1")
elif score < 70 :
    print ("เกรด 2")
elif score < 80 :

    print ("เกรด 3")
elif score < 100 :

    print ("เกรด 4")
    
else :
    print("ERROR")