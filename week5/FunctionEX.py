def MyFunction(a,b):
    all = []
    for i in range (a,b+1):
            sum = i % 3 
            if sum == 0:
                continue
            else :
                 all.append(i)
    return all

