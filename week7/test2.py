try:
    num = int(input("ใส่เลข :"))
    if num <=0:
        raise ZeroDivisionError
    for i in range(1,13):
        print(f"{num} x {i} = {num*i}")

except ValueError:
    print("ใส่เฉพาะตัวเลข")
except ZeroDivisionError :
    print("ห้ามใส่ 0")