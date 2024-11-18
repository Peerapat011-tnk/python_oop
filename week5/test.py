INPUT = int(input(""))
MINUS = 0
PLUST = 0
while True:
    if INPUT == 0:
        break
    elif INPUT < 0:
        MINUS += INPUT
    elif INPUT > 0:
        PLUST += INPUT
   
