import FunctionEX2
PLUST = 0
MINUS = 0
P = 0
M = 0
while True:
    num = int(input("ENTER NUM : "))
    if num > 0:
        PLUST = FunctionEX2.Myfunction(num,MINUS,PLUST)
        print(PLUST)
    elif num < 0:
        MINUS = FunctionEX2.Myfunction(num,MINUS,PLUST)
        print(MINUS)
    else :
        print(f"ค่าบวกเท่ากับ {P} ค่าลบเท่ากับ{M}")
        break