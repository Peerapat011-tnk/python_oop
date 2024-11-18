import FunctionEX2
PLUST = 0
MINUS = 0
while True:
    num = int(input("ENTER NUM : "))
    if num > 0:
        PLUST = FunctionEX2.Myfunction(num,PLUST,MINUS)
        print(PLUST)
    elif num < 0:
        MINUS = FunctionEX2.Myfunction(num,PLUST,MINUS)
        print(MINUS)
    else :
        print(f"ค่าบวกเท่ากับ {PLUST} ค่าลบเท่ากับ{MINUS}")
        break