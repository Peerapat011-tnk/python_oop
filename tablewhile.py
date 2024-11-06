N = int(input("Enternum : "))
i = 1
while i <= 24 :
    if i*N/2 %2 != 0:
        print(f"{N} x {i} = {i*N}")
    i+=1