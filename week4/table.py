N = int(input("Enternum : "))
for i in range(1,25,1):
    if i*N/2 %2 != 0:
        print(f"{N} x {i} = {i*N}")