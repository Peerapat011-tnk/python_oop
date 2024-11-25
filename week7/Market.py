try :
    buget = int(input("ใส่ยอดซื้อของคุณ  : "))
    if buget == 0 :
        raise ZeroDivisionError
    elif buget < 0 :
        raise Exception
    else :
        if buget >= 5000 :
            print(f"ยอดที่คุณต้องจ่ายคือ : {buget-buget*0.2} บาท")
        elif buget >= 2000 and buget <= 4999 :
            print(f"ยอดที่คุณต้องจ่ายคือ : {buget-buget*0.1} บาท")
        else :
            print("ยอดเงินของคุณต่ำเกินไป")


except ZeroDivisionError:
    print("ห้ามใส่ค่า 0")
except ValueError:
    print("ใส่เฉพาะตัวเลข")
except :
    print("ค่าไม่ถูกต้อง")
finally :
    print("จบ")