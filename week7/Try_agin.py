all = 0

while True:
    try :
        price = str(input("กรอกราคาสินค้า or exit: "))

        if price == "exit":
            print(f"ยอดรวมทั้งหมด {all} บาท")
        elif int(price) == 0:
            raise ZeroDivisionError
        elif int(price) < 0 :
            raise Exception
        else :
            all += int(price)

    except ValueError :
        print("กรุณากรอกตัวเลขเท่านั้น")
    except ZeroDivisionError:
        print("ราคาสินค้าต้องมากกว่า 0")
    except :
        print("ราคาสินค้าต้องไม่ติดลบ")

    
